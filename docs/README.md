# MusicKit Documentation

This documentation consolidates the Apple MusicKit framework reference into organized, comprehensive guides. The content has been systematically organized from Apple's official MusicKit documentation to provide developers with a structured, searchable reference for building music-enabled applications.

## Overview

MusicKit is Apple's framework for integrating iOS, iPadOS, macOS, tvOS, watchOS, and visionOS applications with Apple Music. This consolidated documentation provides:

- **Comprehensive API Reference**: All MusicKit types, protocols, and methods organized by functionality
- **Structured Guides**: Getting started tutorials and framework overview
- **Cross-Referenced Content**: Related components linked throughout the documentation
- **Complete Type Definitions**: Swift declarations, properties, methods, and usage examples

**Source**: All content consolidated from [Apple Developer Documentation](https://developer.apple.com/documentation/musickit)
**Total Documentation**: 31 comprehensive files covering 4,208+ lines of detailed reference material

## Getting Started

### Essential Guides
- **[MusicKit Overview](guides/MusicKitOverview.md)** - Complete framework introduction including availability, key concepts, and integration patterns
- **[Getting Started Guide](guides/GettingStarted.md)** - Step-by-step setup instructions, authorization flow, and basic implementation examples

### Quick Setup Checklist
1. Add `NSAppleMusicUsageDescription` to your app's Info.plist
2. Configure MusicKit App Service in Apple Developer portal
3. Request user authorization with `MusicAuthorization`
4. Check subscription status with `MusicSubscription`
5. Begin searching, requesting, or playing music content

## Core Types

The fundamental music item types that represent content in the Apple Music catalog:

- **[Album](core-types/Album.md)** - Albums with tracks, artwork, release information, and editorial content
- **[Artist](core-types/Artist.md)** - Recording artists with biographical information, genres, and associated content
- **[Song](core-types/Song.md)** - Individual songs with metadata, playback parameters, and relationships
- **[Playlist](core-types/Playlist.md)** - User and editorial playlists with track collections and curation details
- **[MusicVideo](core-types/MusicVideo.md)** - Music videos with video-specific metadata and playback information
- **[Track](core-types/Track.md)** - Generic track type encompassing songs and music videos
- **[Station](core-types/Station.md)** - Radio stations with streaming and editorial information
- **[Genre](core-types/Genre.md)** - Music genres with hierarchical relationships
- **[Curator](core-types/Curator.md)** - Editorial curators and their associated content
- **[RadioShow](core-types/RadioShow.md)** - Radio show programs and episodes
- **[RecordLabel](core-types/RecordLabel.md)** - Music record labels and their catalog

## API Layer

Request and response types for interacting with Apple Music services:

- **[Catalog Search API](api-layer/CatalogSearchAPI.md)** - Search the Apple Music catalog with `MusicCatalogSearchRequest` and handle `MusicCatalogSearchResponse`
- **[Catalog Resource API](api-layer/CatalogResourceAPI.md)** - Fetch specific catalog items with `MusicCatalogResourceRequest` and resource responses
- **[Catalog Charts API](api-layer/CatalogChartsAPI.md)** - Access music charts with `MusicCatalogChartsRequest` for trending content
- **[Library API](api-layer/LibraryAPI.md)** - Manage user's music library with requests, responses, and modification operations
- **[Personal Recommendations API](api-layer/PersonalRecommendationsAPI.md)** - Get personalized music recommendations based on user preferences
- **[Recently Played API](api-layer/RecentlyPlayedAPI.md)** - Access user's recently played music history and listening patterns
- **[Data Request API](api-layer/DataRequestAPI.md)** - Make arbitrary Apple Music API requests with `MusicDataRequest`

## Protocols

Protocol definitions that extend functionality across MusicKit types:

- **[Filter Protocols](protocols/FilterProtocols.md)** - Comprehensive filtering capabilities including `MusicCatalogSearchable`, `MusicLibrarySearchable`, and various filter types
- **[Request Protocols](protocols/RequestProtocols.md)** - Base protocols for API requests including `MusicDataRequest` and `MusicPropertyContainer`
- **[Sort Protocols](protocols/SortProtocols.md)** - Sorting capabilities for catalog and library content with `MusicLibrarySortOrder` and related types
- **[Playback Protocols](protocols/PlaybackProtocols.md)** - Playback-related protocols including `PlayableMusicItem` and playlist management
- **[Utility Protocols](protocols/UtilityProtocols.md)** - Supporting protocols for music item identification and relationships

## Services

Core service classes for MusicKit functionality:

- **[Music Library](services/MusicLibrary.md)** - Complete user library management including `MusicLibrary` class and collection operations
- **[Authorization](services/Authorization.md)** - User permission management with `MusicAuthorization` and subscription checking
- **[Token Management](services/TokenManagement.md)** - Developer token handling, automatic generation, and authentication flows
- **[Music Players](services/MusicPlayers.md)** - Audio playback with `ApplicationMusicPlayer`, `SystemMusicPlayer`, and queue management

## Utilities

Supporting types, enumerations, and utility classes:

- **[Core Data Types](utilities/CoreDataTypes.md)** - Fundamental data structures including `MusicItemID`, `PlayParameters`, and collection types
- **[Property Management](utilities/PropertyManagement.md)** - Property loading, partial objects, and data fetching optimization
- **[Enumerations](utilities/Enumerations.md)** - Key enumerations for authorization status, subscription types, and player states
- **[Support Types](utilities/SupportTypes.md)** - Additional supporting types and type aliases

## Quick Reference

### Common Tasks

| Task | Primary Types | Key Methods |
|------|---------------|-------------|
| **Search Music** | `MusicCatalogSearchRequest` | `response()` |
| **Get Specific Items** | `MusicCatalogResourceRequest` | `response()` |
| **User Authorization** | `MusicAuthorization` | `request()`, `currentStatus` |
| **Play Music** | `ApplicationMusicPlayer` | `play()`, `queue` |
| **Library Management** | `MusicLibrary` | `search()`, `add()` |
| **Recommendations** | `MusicPersonalRecommendationsRequest` | `response()` |

### Key Protocols by Use Case

- **Search & Discovery**: `MusicCatalogSearchable`, `MusicLibrarySearchable`
- **Playback**: `PlayableMusicItem`, `MusicPlayer`
- **Filtering**: `MusicCatalogFilterable`, `MusicLibraryFilterable`
- **Sorting**: `MusicLibrarySortOrder`

### Platform Availability
- **iOS**: 15.0+
- **iPadOS**: 15.0+
- **macOS**: 12.0+
- **tvOS**: 15.0+
- **watchOS**: 8.0+
- **visionOS**: 1.0+
- **Mac Catalyst**: 15.0+

## Navigation Tips

- Each file includes **complete Swift declarations** with all properties and methods
- **Source links** are provided to original Apple documentation
- **Cross-references** link related types and protocols
- **Code examples** demonstrate real-world usage patterns
- **Availability information** shows platform and version requirements

## Documentation Structure

This consolidated documentation was systematically generated from Apple's official MusicKit documentation, organized into logical groupings:

- **31 comprehensive files** covering all MusicKit functionality
- **Consistent formatting** with Swift declarations, descriptions, and examples
- **Complete cross-referencing** between related components
- **Source attribution** for all content

For the most up-to-date information, always refer to [Apple's official MusicKit documentation](https://developer.apple.com/documentation/musickit).