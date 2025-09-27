# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysearchresponse

- [MusicKit](/documentation/musickit)
- MusicLibrarySearchResponse

Structure

# MusicLibrarySearchResponse

An object that contains results for a library search request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicLibrarySearchResponse
```

## [Topics](/documentation/musickit/musiclibrarysearchresponse#topics)

### [Instance Properties](/documentation/musickit/musiclibrarysearchresponse#Instance-Properties)

[`let albums: MusicItemCollection<Album>`](/documentation/musickit/musiclibrarysearchresponse/albums)

A collection of albums.

[`let artists: MusicItemCollection<Artist>`](/documentation/musickit/musiclibrarysearchresponse/artists)

A collection of artists.

[`let musicVideos: MusicItemCollection<MusicVideo>`](/documentation/musickit/musiclibrarysearchresponse/musicvideos)

A collection of music videos.

[`let playlists: MusicItemCollection<Playlist>`](/documentation/musickit/musiclibrarysearchresponse/playlists)

A collection of playlists.

[`let songs: MusicItemCollection<Song>`](/documentation/musickit/musiclibrarysearchresponse/songs)

A collection of songs.

[`let topResults: MusicItemCollection<MusicLibrarySearchResponse.TopResult>`](/documentation/musickit/musiclibrarysearchresponse/topresults)

A collection of top results.

### [Enumerations](/documentation/musickit/musiclibrarysearchresponse#Enumerations)

[`enum TopResult`](/documentation/musickit/musiclibrarysearchresponse/topresult)

An item that represents one of the top results in a library search response.

## [Relationships](/documentation/musickit/musiclibrarysearchresponse#relationships)

### [Conforms To](/documentation/musickit/musiclibrarysearchresponse#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
