#!/usr/bin/env python3
"""
Apple MusicKit Documentation Scraper

This script extracts the entire Apple MusicKit documentation from
https://developer.apple.com/documentation/musickit and converts it to
markdown files while preserving the original structure.
"""

import os
import time
import logging
from urllib.parse import urljoin, urlparse
from pathlib import Path
from typing import Set, List, Dict
from datetime import datetime, timedelta
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
from markdownify import markdownify
import requests


class MusicKitDocScraper:
    """Scraper for Apple MusicKit documentation."""

    def __init__(self, base_url: str = "https://developer.apple.com/documentation/musickit",
                 output_dir: str = "musickit_docs"):
        self.base_url = base_url
        self.base_domain = "developer.apple.com"
        self.output_dir = Path(output_dir)
        self.visited_urls: Set[str] = set()
        self.to_visit: List[str] = [base_url]
        self.failed_urls: List[str] = []

        # Time tracking for progress estimation
        self.start_time: datetime = None
        self.page_times: List[float] = []  # Processing time for each page
        self.max_time_samples = 10  # Use last 10 pages for average calculation

        # Initialize markdown converter settings
        self.md_options = {
            'heading_style': 'ATX',
            'bullets': '-',
            'code_language': '',
            'wrap': True,
            'wrap_width': 80
        }

        # Setup logging
        self._setup_logging()

        # Setup Selenium driver
        self.driver = None
        self._setup_driver()

        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('musickit_scraper.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def _setup_driver(self):
        """Setup WebDriver with appropriate options, trying Firefox first, then Safari."""
        try:
            # Try Firefox first
            self.logger.info("Attempting to use Firefox WebDriver...")
            firefox_options = FirefoxOptions()
            firefox_options.add_argument('--headless')  # Run in background
            firefox_options.add_argument('--window-size=1920,1080')

            service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service, options=firefox_options)
            self.driver.implicitly_wait(10)
            self.logger.info("Successfully initialized Firefox WebDriver")
            return
        except Exception as e:
            self.logger.warning(f"Firefox WebDriver failed: {e}")

        try:
            # Fallback to Safari (available on macOS)
            self.logger.info("Attempting to use Safari WebDriver...")
            safari_options = SafariOptions()
            self.driver = webdriver.Safari(options=safari_options)
            self.driver.implicitly_wait(10)
            self.logger.info("Successfully initialized Safari WebDriver")
            return
        except Exception as e:
            self.logger.error(f"Safari WebDriver failed: {e}")
            raise RuntimeError("Could not initialize any WebDriver. Please install Safari or Firefox.")

    def calculate_average_time_per_page(self) -> float:
        """Calculate average time per page using recent samples."""
        if not self.page_times:
            return 25.0  # Default estimate of 25 seconds per page

        # Use last N samples for more accurate recent performance
        recent_times = self.page_times[-self.max_time_samples:]
        return sum(recent_times) / len(recent_times)

    def format_duration(self, seconds: float) -> str:
        """Format duration in human-readable format."""
        if seconds < 60:
            return f"{seconds:.0f}s"
        elif seconds < 3600:
            minutes = seconds / 60
            return f"{minutes:.0f}m"
        else:
            hours = seconds / 3600
            minutes = (seconds % 3600) / 60
            return f"{hours:.0f}h {minutes:.0f}m"

    def format_time(self, dt: datetime) -> str:
        """Format datetime for display."""
        return dt.strftime("%I:%M %p").lstrip('0')

    def get_eta_info(self, remaining_pages: int) -> Dict[str, str]:
        """Calculate and format ETA information."""
        if not remaining_pages:
            return {}

        avg_time = self.calculate_average_time_per_page()
        remaining_seconds = remaining_pages * avg_time
        eta_datetime = datetime.now() + timedelta(seconds=remaining_seconds)

        elapsed_time = (datetime.now() - self.start_time).total_seconds() if self.start_time else 0

        return {
            'avg_time': f"{avg_time:.1f}s",
            'remaining_time': self.format_duration(remaining_seconds),
            'eta_time': self.format_time(eta_datetime),
            'elapsed_time': self.format_duration(elapsed_time)
        }

    def log_progress(self, current_page: int, total_discovered: int, remaining: int, url: str = None):
        """Log detailed progress information with ETA."""
        if total_discovered == 0:
            return

        progress_percent = (current_page / total_discovered) * 100
        eta_info = self.get_eta_info(remaining)

        if url:
            # Before processing page
            page_name = url.split('/')[-1] or 'index'
            if eta_info:
                self.logger.info(
                    f"[{current_page}/{total_discovered} - {progress_percent:.1f}%] Processing: {page_name}"
                )
                self.logger.info(
                    f"    Avg: {eta_info['avg_time']}/page | ETA: {eta_info['eta_time']} "
                    f"({eta_info['remaining_time']} remaining)"
                )
            else:
                self.logger.info(f"[{current_page}/{total_discovered}] Processing: {page_name}")
        else:
            # After processing page
            if eta_info:
                self.logger.info(
                    f"Progress: {current_page}/{total_discovered} ({progress_percent:.1f}%) | "
                    f"Remaining: {remaining} pages | ETA: {eta_info['eta_time']}"
                )

    def is_musickit_url(self, url: str) -> bool:
        """Check if URL is within MusicKit documentation scope."""
        if not url:
            return False

        parsed = urlparse(url)

        # Must be from Apple developer site
        if parsed.netloc != self.base_domain:
            return False

        # Must be within musickit documentation path
        if not parsed.path.startswith('/documentation/musickit'):
            return False

        # Exclude fragments and query params for comparison
        return True

    def normalize_url(self, url: str) -> str:
        """Normalize URL by removing fragments and query parameters."""
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

    def extract_links(self, soup: BeautifulSoup, current_url: str) -> List[str]:
        """Extract all valid MusicKit documentation links from the page."""
        links = []

        # Find all links on the page
        for link in soup.find_all('a', href=True):
            href = link['href']

            # Convert relative URLs to absolute
            absolute_url = urljoin(current_url, href)
            normalized_url = self.normalize_url(absolute_url)

            # Check if it's a valid MusicKit URL we haven't visited
            if (self.is_musickit_url(normalized_url) and
                normalized_url not in self.visited_urls and
                normalized_url not in links):
                links.append(normalized_url)

        return links

    def wait_for_content(self, timeout: int = 30) -> bool:
        """Wait for the page content to load."""
        try:
            # Wait for the main content area to be present
            WebDriverWait(self.driver, timeout).until(
                EC.any_of(
                    EC.presence_of_element_located((By.CLASS_NAME, "documentation-topic")),
                    EC.presence_of_element_located((By.CLASS_NAME, "api-reference")),
                    EC.presence_of_element_located((By.TAG_NAME, "main")),
                    EC.presence_of_element_located((By.CLASS_NAME, "content"))
                )
            )

            # Additional wait for dynamic content
            time.sleep(2)
            return True

        except Exception as e:
            self.logger.warning(f"Timeout waiting for content: {e}")
            return False

    def extract_page_content(self, url: str) -> Dict[str, str]:
        """Extract content from a single page."""
        page_start_time = time.time()

        try:
            # Load the page
            self.driver.get(url)

            # Wait for content to load
            if not self.wait_for_content():
                self.logger.warning(f"Content did not load properly for {url}")

            # Get page source and parse with BeautifulSoup
            html_content = self.driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract title
            title = ""
            title_element = soup.find('h1')
            if title_element:
                title = title_element.get_text(strip=True)
            else:
                # Fallback to page title
                title_tag = soup.find('title')
                if title_tag:
                    title = title_tag.get_text(strip=True)

            # Extract main content area
            content_element = soup.find('main') or soup.find(class_='content') or soup.body

            if content_element:
                # Convert to markdown using markdownify
                content_html = str(content_element)
                markdown_content = markdownify(content_html, **self.md_options)
            else:
                markdown_content = "No content found"
                self.logger.warning(f"No main content found for {url}")

            # Extract links for further crawling
            links = self.extract_links(soup, url)

            # Record processing time
            page_end_time = time.time()
            processing_time = page_end_time - page_start_time
            self.page_times.append(processing_time)

            return {
                'title': title,
                'content': markdown_content,
                'links': links,
                'url': url,
                'processing_time': processing_time
            }

        except Exception as e:
            self.logger.error(f"Error extracting content from {url}: {e}")
            self.failed_urls.append(url)

            # Still record time for failed pages
            page_end_time = time.time()
            processing_time = page_end_time - page_start_time
            self.page_times.append(processing_time)

            return {
                'title': 'Error',
                'content': f"Failed to extract content: {e}",
                'links': [],
                'url': url,
                'processing_time': processing_time
            }

    def get_file_path(self, url: str) -> Path:
        """Generate file path for the given URL."""
        parsed = urlparse(url)
        path_parts = [part for part in parsed.path.split('/') if part]

        # Remove 'documentation' and 'musickit' from path
        if 'documentation' in path_parts:
            path_parts.remove('documentation')
        if 'musickit' in path_parts:
            path_parts.remove('musickit')

        # If no path parts left, use index
        if not path_parts:
            return self.output_dir / "index.md"

        # Create directory structure
        if len(path_parts) > 1:
            dir_path = self.output_dir / Path(*path_parts[:-1])
            dir_path.mkdir(parents=True, exist_ok=True)
            return dir_path / f"{path_parts[-1]}.md"
        else:
            return self.output_dir / f"{path_parts[0]}.md"

    def save_content(self, page_data: Dict[str, str]):
        """Save page content to markdown file."""
        try:
            file_path = self.get_file_path(page_data['url'])

            # Prepare markdown content with metadata
            content = f"""# {page_data['title']}

> Source: {page_data['url']}

{page_data['content']}
"""

            # Write to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            self.logger.info(f"Saved content to: {file_path}")

        except Exception as e:
            self.logger.error(f"Error saving content for {page_data['url']}: {e}")

    def scrape(self):
        """Main scraping method."""
        self.start_time = datetime.now()
        self.logger.info(f"Starting MusicKit documentation scrape at {self.format_time(self.start_time)}...")

        try:
            while self.to_visit:
                url = self.to_visit.pop(0)

                if url in self.visited_urls:
                    continue

                self.visited_urls.add(url)

                # Calculate current progress stats
                total_discovered = len(self.visited_urls) + len(self.to_visit)
                current_page = len(self.visited_urls)

                # Show progress before processing
                self.log_progress(current_page, total_discovered, len(self.to_visit), url)

                # Extract content from the page
                page_data = self.extract_page_content(url)

                # Save the content
                self.save_content(page_data)

                # Log completion with timing
                processing_time = page_data.get('processing_time', 0)
                file_path = self.get_file_path(url)
                self.logger.info(f"✓ Saved: {file_path.relative_to(self.output_dir)} ({processing_time:.1f}s)")

                # Add new links to visit queue
                new_links_added = 0
                for link in page_data['links']:
                    if link not in self.visited_urls and link not in self.to_visit:
                        self.to_visit.append(link)
                        new_links_added += 1

                if new_links_added > 0:
                    self.logger.info(f"Found {new_links_added} new pages to scrape")

                # Rate limiting - be respectful
                time.sleep(1)

            # Final completion summary
            end_time = datetime.now()
            total_time = (end_time - self.start_time).total_seconds()
            avg_time = self.calculate_average_time_per_page()

            self.logger.info("=" * 60)
            self.logger.info("SCRAPING COMPLETED!")
            self.logger.info(f"✓ Total pages processed: {len(self.visited_urls)}")
            self.logger.info(f"✓ Total time: {self.format_duration(total_time)}")
            self.logger.info(f"✓ Average time per page: {avg_time:.1f}s")
            self.logger.info(f"✓ Started: {self.format_time(self.start_time)}")
            self.logger.info(f"✓ Finished: {self.format_time(end_time)}")

            if self.failed_urls:
                self.logger.warning(f"⚠️  Failed to process {len(self.failed_urls)} URLs:")
                for url in self.failed_urls:
                    self.logger.warning(f"  - {url}")

            self.logger.info("=" * 60)

        except KeyboardInterrupt:
            self.logger.info("Scraping interrupted by user")

        finally:
            self.cleanup()

    def cleanup(self):
        """Clean up resources."""
        if self.driver:
            self.driver.quit()

        # Create index file
        self.create_index()

    def create_index(self):
        """Create an index file with all scraped pages."""
        try:
            index_content = f"""# Apple MusicKit Documentation

This documentation was scraped from [Apple Developer Documentation](https://developer.apple.com/documentation/musickit).

## Scraped Pages ({len(self.visited_urls)} total)

"""

            # Sort URLs for better organization
            sorted_urls = sorted(self.visited_urls)

            for url in sorted_urls:
                file_path = self.get_file_path(url)
                relative_path = file_path.relative_to(self.output_dir)
                page_name = url.split('/')[-1] or 'index'
                index_content += f"- [{page_name}]({relative_path}) - {url}\n"

            # Write index file
            with open(self.output_dir / "README.md", 'w', encoding='utf-8') as f:
                f.write(index_content)

            self.logger.info("Created index file: README.md")

        except Exception as e:
            self.logger.error(f"Error creating index: {e}")


def main():
    """Main entry point."""
    scraper = MusicKitDocScraper()
    scraper.scrape()


if __name__ == "__main__":
    main()