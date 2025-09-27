# Core Data Types

> Source: Multiple Apple MusicKit documentation pages

This section contains the fundamental data types used throughout MusicKit for representing basic music item information, identifiers, collections, artwork, editorial content, and preview assets.

## MusicItemID
- **Swift Declaration**: `@frozen struct MusicItemID`
- **Purpose**: An object that represents a unique identifier for a music item.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicitemid)
- **Properties**:
  - Represents a unique identifier as a string-backed value
- **Methods**:
  - `init(String)`: Creates a music item identifier with a string
- **Usage**: Used throughout MusicKit to uniquely identify songs, albums, artists, playlists, and other music content. Provides type-safe identification that can be used for fetching specific music items from the catalog or library.
- **Conforms To**: `Copyable`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `ExpressibleByStringLiteral`, `Hashable`, `MusicLibraryRequestFilterValueEquatable`, `MusicLibraryRequestFilterValueMembershipComparable`, `RawRepresentable`, `Sendable`

## MusicItemCollection
- **Swift Declaration**: `struct MusicItemCollection<MusicItemType> where MusicItemType : MusicItem`
- **Purpose**: A collection of music items with support for pagination and batch fetching.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicitemcollection)
- **Properties**:
  - `hasNextBatch: Bool`: A Boolean value that indicates whether the collection has information that allows it to fetch a subsequent batch of items
  - `title: String?`: An optional title for the collection
- **Methods**:
  - `init<S>(S)`: Initialize with a sequence of music items
  - `nextBatch(limit: Int?) async throws -> MusicItemCollection<MusicItemType>?`: Fetches the next batch of items asynchronously
  - `static func += (inout MusicItemCollection<MusicItemType>, MusicItemCollection<MusicItemType>)`: Appends contents of a collection representing a next batch
- **Usage**: Used to represent collections of music items returned from catalog searches, library requests, and relationship queries. Supports efficient pagination for large result sets and provides collection semantics for working with groups of music items.
- **Conforms To**: `BidirectionalCollection`, `Collection`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `ExpressibleByArrayLiteral`, `Hashable`, `RandomAccessCollection`, `Sendable`, `Sequence`

## Artwork
- **Swift Declaration**: `struct Artwork`
- **Purpose**: An object that represents artwork for a music item, including image metadata and color information.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/artwork)
- **Properties**:
  - `alternateText: String?`: A textual description for the image
  - `backgroundColor: CGColor?`: The average background color of the image
  - `maximumHeight: Int`: The maximum height available for the image
  - `maximumWidth: Int`: The maximum width available for the image
  - `primaryTextColor: CGColor?`: The primary text color to use when displaying the background color
  - `quaternaryTextColor: CGColor?`: The final posttertiary text color to use when displaying the background color
  - `secondaryTextColor: CGColor?`: The secondary text color to use when displaying the background color
  - `tertiaryTextColor: CGColor?`: The tertiary text color to use when displaying the background color
- **Methods**:
  - `url(width: Int, height: Int) -> URL?`: Returns a URL to request the image asset for a specified width and height
- **Usage**: Used throughout MusicKit to represent artwork for albums, songs, artists, playlists, and other music content. Provides both image URLs and color palette information for creating visually cohesive user interfaces.
- **Conforms To**: `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`

## ArtworkImage
- **Swift Declaration**: `@MainActor @preconcurrency struct ArtworkImage`
- **Purpose**: A SwiftUI view that displays the image for a music item's artwork with automatic placeholder handling.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/artworkimage)
- **Properties**:
  - Backed by an `Artwork` instance
- **Methods**:
  - `init(Artwork, height: CGFloat)`: Creates an instance with a specified height
  - `init(Artwork, width: CGFloat)`: Creates an instance with a specified width
  - `init(Artwork, width: CGFloat, height: CGFloat)`: Creates an instance with a specified width and height
- **Usage**: Use in SwiftUI interfaces to display artwork images. Automatically handles loading states by displaying a placeholder with a solid color that matches the artwork's background color while the image data is loading.
- **Conforms To**: `Sendable`, `View`

## EditorialNotes
- **Swift Declaration**: `struct EditorialNotes`
- **Purpose**: An object that represents editorial notes and descriptive text content for music items.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/editorialnotes)
- **Properties**:
  - `name: String?`: The name for the editorial notes
  - `short: String?`: Abbreviated notes that display inline or when the content appears alongside other content
  - `standard: String?`: Notes that appear when the content displays prominently
  - `tagline: String?`: The tag line for the editorial notes
- **Methods**: None specified
- **Usage**: Used to provide descriptive text content for albums, playlists, artists, and other music items. Different note types (short, standard, tagline) are appropriate for different UI contexts and display sizes.
- **Conforms To**: `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`

## PreviewAsset
- **Swift Declaration**: `struct PreviewAsset`
- **Purpose**: An object that represents a preview for music and video resources, providing URLs for preview content.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/previewasset)
- **Properties**:
  - `artwork: Artwork?`: The preview artwork for the associated preview music video
  - `hlsURL: URL?`: The HLS preview URL for the content
  - `url: URL?`: The preview URL for the content
- **Methods**: None specified
- **Usage**: Used to provide preview content for songs, music videos, and other playable items. Offers both standard URL and HLS streaming options for different playback scenarios.
- **Conforms To**: `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`

## PlayParameters
- **Swift Declaration**: `struct PlayParameters`
- **Purpose**: An opaque object that represents parameters to initiate playback of a playable music item using a music player.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/playparameters)
- **Properties**:
  - Opaque structure - internal properties not exposed
- **Methods**: None specified
- **Usage**: Used with MusicKit players (ApplicationMusicPlayer, SystemMusicPlayer) to initiate playback of music items. Acts as an opaque token that encapsulates all necessary playback information for a specific music item.
- **Conforms To**: `Copyable`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`