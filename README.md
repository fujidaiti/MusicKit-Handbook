# Apple MusicKit Documentation Scraper

This Python script extracts the entire Apple MusicKit documentation from the Apple Developer website and converts it to markdown files while preserving the original structure.

## Features

- **Complete Documentation Extraction**: Crawls all MusicKit documentation pages from `https://developer.apple.com/documentation/musickit`
- **Markdown Conversion**: Converts HTML content to clean markdown format
- **Progress Tracking**: Real-time progress updates with ETA calculations
- **Robust Error Handling**: Continues scraping even if individual pages fail
- **Rate Limiting**: Respectful crawling with built-in delays
- **Cross-Platform**: Supports both Firefox and Safari WebDrivers

## Requirements

Install the required dependencies:

```bash
pip install selenium beautifulsoup4 markdownify requests webdriver-manager
```

### WebDriver Requirements

The scraper will automatically try to use:
1. **Firefox** (preferred) - Automatically downloads GeckoDriver
2. **Safari** (macOS fallback) - Requires enabling "Allow Remote Automation" in Safari's Develop menu

## Usage

### Basic Usage

```bash
python musickit_scraper.py
```

### Advanced Usage

You can customize the scraper by modifying the initialization parameters in the script:

```python
scraper = MusicKitDocScraper(
    base_url="https://developer.apple.com/documentation/musickit",
    output_dir="raw_docs"
)
```

## Output Structure

The scraper creates the following directory structure:

```
raw_docs/
├── README.md                 # Index of all scraped pages
├── index.md                  # Main MusicKit documentation page
├── musickit_scraper.log      # Detailed scraping log
└── [subdirectories]/         # Organized by URL structure
    └── [page_name].md        # Individual documentation pages
```

### Output Files

- **Markdown Files**: Each documentation page is saved as a `.md` file with:
  - Original title as heading
  - Source URL reference
  - Content converted from HTML to markdown
- **README.md**: Auto-generated index with links to all scraped pages
- **Log File**: Detailed logging of the scraping process with timestamps

## Features in Detail

### Progress Tracking
- Real-time progress updates showing current page being processed
- ETA calculations based on average processing time
- Statistics on pages processed, time elapsed, and estimated completion time

### Error Handling
- Failed URLs are logged but don't stop the scraping process
- Automatic retry mechanisms for network issues
- Graceful handling of missing content

### Content Processing
- Extracts main content areas from documentation pages
- Preserves code blocks, links, and formatting
- Converts HTML tables and lists to markdown equivalents

### URL Management
- Intelligent link discovery and filtering
- Deduplication to avoid processing the same page twice
- Scope limiting to MusicKit documentation only

## Configuration Options

The scraper includes several configurable options:

```python
# Markdown conversion settings
md_options = {
    'heading_style': 'ATX',      # Use # for headings
    'bullets': '-',              # Use - for bullet points
    'code_language': '',         # Default code block language
    'wrap': True,                # Enable text wrapping
    'wrap_width': 80            # Wrap at 80 characters
}

# Performance settings
max_time_samples = 10           # Pages to use for ETA calculation
implicit_wait = 10              # WebDriver wait time (seconds)
rate_limit_delay = 1            # Delay between requests (seconds)
```

## Logging

The scraper provides detailed logging:

- **Console Output**: Real-time progress and status updates
- **Log File**: Complete log saved to `musickit_scraper.log`
- **Progress Information**: Page counts, processing times, and ETAs

## Example Output

```
2024-01-01 12:00:00 - INFO - Starting MusicKit documentation scrape at 12:00 PM...
2024-01-01 12:00:05 - INFO - [1/50 - 2.0%] Processing: index
2024-01-01 12:00:05 - INFO -     Avg: 5.2s/page | ETA: 12:04 PM (4m remaining)
2024-01-01 12:00:10 - INFO - ✓ Saved: index.md (5.1s)
2024-01-01 12:00:10 - INFO - Found 15 new pages to scrape
```

## Troubleshooting

### WebDriver Issues
- **Firefox**: Ensure Firefox is installed and up-to-date
- **Safari**: Enable "Allow Remote Automation" in Safari > Develop menu
- **Permissions**: Check that the script has permission to control your browser

### Common Issues
- **Slow Performance**: The scraper includes built-in rate limiting to be respectful to Apple's servers
- **Memory Usage**: For large documentation sets, monitor system memory usage
- **Network Issues**: The scraper will retry failed requests and log errors

## Legal Notes

This tool is designed for personal use and educational purposes. Please:
- Respect Apple's terms of service
- Use reasonable rate limiting (built into the scraper)
- Don't overload Apple's servers
- Consider caching results to avoid repeated scraping

## License

This scraper is provided as-is for educational and personal use.