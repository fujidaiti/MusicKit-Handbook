# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysearchresponse/topresult

- [MusicKit](/documentation/musickit)
- [MusicLibrarySearchResponse](/documentation/musickit/musiclibrarysearchresponse)
- MusicLibrarySearchResponse.TopResult

Enumeration

# MusicLibrarySearchResponse.TopResult

An item that represents one of the top results in a library search response.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
enum TopResult
```

## [Topics](/documentation/musickit/musiclibrarysearchresponse/topresult#topics)

### [Enumeration Cases](/documentation/musickit/musiclibrarysearchresponse/topresult#Enumeration-Cases)

[`case album(Album)`](/documentation/musickit/musiclibrarysearchresponse/topresult/album(_:))

An item that corresponds to an album.

[`case artist(Artist)`](/documentation/musickit/musiclibrarysearchresponse/topresult/artist(_:))

An item that corresponds to an artist.

[`case musicVideo(MusicVideo)`](/documentation/musickit/musiclibrarysearchresponse/topresult/musicvideo(_:))

An item that corresponds to a music video.

[`case playlist(Playlist)`](/documentation/musickit/musiclibrarysearchresponse/topresult/playlist(_:))

An item that corresponds to a playlist.

[`case song(Song)`](/documentation/musickit/musiclibrarysearchresponse/topresult/song(_:))

An item that corresponds to a song.

### [Instance Properties](/documentation/musickit/musiclibrarysearchresponse/topresult#Instance-Properties)

[`var artwork: Artwork?`](/documentation/musickit/musiclibrarysearchresponse/topresult/artwork)

The artwork of this top result for library search.

[`var id: MusicItemID`](/documentation/musickit/musiclibrarysearchresponse/topresult/id)

The unique identifier of this item.

[`var title: String`](/documentation/musickit/musiclibrarysearchresponse/topresult/title)

The title of this top result for library search.

## [Relationships](/documentation/musickit/musiclibrarysearchresponse/topresult#relationships)

### [Conforms To](/documentation/musickit/musiclibrarysearchresponse/topresult#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`MusicItem`](/documentation/musickit/musicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
