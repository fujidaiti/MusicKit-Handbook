# Enumerations

> Source: Multiple Apple MusicKit documentation pages

This section contains enumerations used throughout MusicKit to represent content ratings, audio quality variants, property sources, and recently played items.

## ContentRating
- **Swift Declaration**: `enum ContentRating`
- **Purpose**: The rating of the content that potentially plays while playing a resource.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/contentrating)
- **Cases**:
  - `case clean`: Content that is marked as clean/family-friendly
  - `case explicit`: Content that contains explicit language or themes
- **Usage**: Used to indicate the content rating for songs, albums, music videos, and other playable content. A nil value means no rating is available for the resource. This allows apps to filter content based on user preferences or parental controls.
- **Conforms To**: `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`

## AudioVariant
- **Swift Declaration**: `enum AudioVariant`
- **Purpose**: Variants that indicate the quality of audio available for an item.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/audiovariant)
- **Cases**:
  - `case dolbyAtmos`: Dolby Atmos is an immersive audio experience that surrounds you with sound from all sides, including above
  - `case dolbyAudio`: Dolby Audio is a surround sound format that includes Dolby 5.1 and 7.1
  - `case highResolutionLossless`: Hi-Res Lossless uses Apple Lossless Audio Codec (ALAC) for bit-for-bit accuracy up to 24-bit/192 kHz
  - `case lossless`: Lossless uses Apple Lossless Audio Codec (ALAC) for bit-for-bit accuracy up to 24-bit/48 kHz
  - `case lossyStereo`: Lossy stereo uses compression used to store sound data
  - `case spatialAudio`: Spatial audio is a fallback mode if the content is Dolby Atmos or Dolby Audio, but hardware capabilities don't support them
- **Usage**: Used to represent the available audio quality options for songs and albums. Apps can use this information to display audio quality badges, allow users to filter by quality, or determine the best quality to play based on device capabilities and user preferences.
- **Conforms To**: `CaseIterable`, `Copyable`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`

## MusicPropertySource
- **Swift Declaration**: `enum MusicPropertySource`
- **Purpose**: An enumeration that specifies which source to use when requesting properties and relationships.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicpropertysource)
- **Cases**:
  - `case catalog`: The source representing the Apple Music catalog
  - `case library`: The source representing the user's music library
- **Usage**: Used when fetching additional properties for music items to specify whether to prefer data from the Apple Music catalog or the user's personal music library. This allows apps to control whether they get global catalog information or user-specific library data for items that exist in both sources.
- **Conforms To**: `CaseIterable`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`

## RecentlyPlayedMusicItem
- **Swift Declaration**: `enum RecentlyPlayedMusicItem`
- **Purpose**: An item that represents an album, a playlist, or a station that the user has recently played.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/recentlyplayedmusicitem)
- **Cases**:
  - `case album(Album)`: An item that corresponds to an album
  - `case playlist(Playlist)`: An item that corresponds to a playlist
  - `case station(Station)`: An item that corresponds to a station
- **Properties**:
  - `artwork: Artwork?`: The artwork of this item
  - `id: MusicItemID`: The unique identifier of this item
  - `playParameters: PlayParameters?`: The parameters to use to play this item
  - `subtitle: String?`: The subtitle of this item
  - `title: String`: The title of this item
- **Usage**: Used to represent items in the user's recently played history. This enumeration provides a unified interface for working with different types of recently played content (albums, playlists, stations) while maintaining type safety and access to common properties like artwork and play parameters.
- **Conforms To**: `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Identifiable`, `MusicItem`, `MusicRecentlyPlayedRequestable`, `PlayableMusicItem`, `Sendable`