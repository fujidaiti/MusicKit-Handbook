# Utility Protocols

> Source: Multiple Apple MusicKit documentation pages

These protocols provide fundamental functionality and utility features for working with music items in MusicKit. They define basic requirements, property management capabilities, and filter value types for music library operations.

## Overview

The utility protocols form the foundation of MusicKit's type system. They enable basic music item functionality, asynchronous property loading, and provide type constraints for filtering library requests. These protocols are typically inherited by more specific music item types and provide essential capabilities for working with music data.

## Protocols

### MusicItem
- **Swift Declaration**: `protocol MusicItem : Sendable`
- **Purpose**: A protocol with basic requirements for music items.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musicitem)
- **Properties**:
  - `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the music item (Required)
- **Methods**:
  - `func with([PartialMusicAsyncProperty<Self>]) async throws -> Self` - Loads a new instance of the music item that includes the specified properties
  - `func with(PartialMusicAsyncProperty<Self>..., preferredSource: MusicPropertySource) async throws -> Self` - Loads a new instance of the music item that includes the specified properties
  - `func with([PartialMusicAsyncProperty<Self>], preferredSource: MusicPropertySource) async throws -> Self` - Loads a new instance of the music item that includes the specified properties
- **Inherits From**: Sendable, SendableMetatype
- **Used By**: All MusicKit music item types including Album, Artist, Curator, Genre, MusicVideo, Playlist, RadioShow, RecordLabel, Song, Station, Track, and many others

### MusicPropertyContainer
- **Swift Declaration**: `protocol MusicPropertyContainer`
- **Purpose**: A protocol for music items that allow loading additional properties that you can fetch asynchronously.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musicpropertycontainer)
- **Methods**:
  - `func with([PartialMusicAsyncProperty<Self>]) async throws -> Self` - Loads a new instance of the music item that includes the specified properties (Required, Default implementation provided)
  - `func with([PartialMusicAsyncProperty<Self>], preferredSource: MusicPropertySource) async throws -> Self` - Loads a new instance of the music item that includes the specified properties (Required)
  - `func with(PartialMusicAsyncProperty<Self>..., preferredSource: MusicPropertySource) async throws -> Self` - Loads a new instance of the music item that includes the specified properties (Required)
- **Used By**: Album, Artist, Curator, Genre, MusicPlayer.Queue.Entry.Item, MusicVideo, Playlist, Playlist.Entry, Playlist.Entry.Item, RadioShow, RecordLabel, Song, Station, Track

### MusicLibraryRequestFilterValueEquatable
- **Swift Declaration**: `protocol MusicLibraryRequestFilterValueEquatable`
- **Purpose**: A protocol for types of values your app can use with equality filters when fetching items using a music library request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiclibraryrequestfiltervalueequatable)
- **Properties/Methods**: No specific properties or methods defined in the protocol
- **Used By**: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid) conforms to this protocol, enabling equality-based filtering in library requests

### MusicLibraryRequestFilterValueMembershipComparable
- **Swift Declaration**: `protocol MusicLibraryRequestFilterValueMembershipComparable`
- **Purpose**: A protocol for types of values your app can use with membership filters when fetching items using a music library request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiclibraryrequestfiltervaluemembershipcomparable)
- **Properties/Methods**: No specific properties or methods defined in the protocol
- **Used By**: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid) conforms to this protocol, enabling membership-based filtering in library requests