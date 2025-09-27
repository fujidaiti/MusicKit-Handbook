# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogsearchresponse/topresult

- [MusicKit](/documentation/musickit)
- [MusicCatalogSearchResponse](/documentation/musickit/musiccatalogsearchresponse)
- MusicCatalogSearchResponse.TopResult

Enumeration

# MusicCatalogSearchResponse.TopResult

An item that represents one of the top results in a catalog search response.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
enum TopResult
```

## [Topics](/documentation/musickit/musiccatalogsearchresponse/topresult#topics)

### [Enumeration Cases](/documentation/musickit/musiccatalogsearchresponse/topresult#Enumeration-Cases)

[`case album(Album)`](/documentation/musickit/musiccatalogsearchresponse/topresult/album(_:))

An item that corresponds to an album.

[`case artist(Artist)`](/documentation/musickit/musiccatalogsearchresponse/topresult/artist(_:))

An item that corresponds to an artist.

[`case curator(Curator)`](/documentation/musickit/musiccatalogsearchresponse/topresult/curator(_:))

An item that corresponds to a curator.

[`case musicVideo(MusicVideo)`](/documentation/musickit/musiccatalogsearchresponse/topresult/musicvideo(_:))

An item that corresponds to a music video.

[`case playlist(Playlist)`](/documentation/musickit/musiccatalogsearchresponse/topresult/playlist(_:))

An item that corresponds to a playlist.

[`case radioShow(RadioShow)`](/documentation/musickit/musiccatalogsearchresponse/topresult/radioshow(_:))

An item that corresponds to a radio show.

[`case recordLabel(RecordLabel)`](/documentation/musickit/musiccatalogsearchresponse/topresult/recordlabel(_:))

An item that corresponds to a record label.

[`case song(Song)`](/documentation/musickit/musiccatalogsearchresponse/topresult/song(_:))

An item that corresponds to a song.

[`case station(Station)`](/documentation/musickit/musiccatalogsearchresponse/topresult/station(_:))

An item that corresponds to a station.

### [Instance Properties](/documentation/musickit/musiccatalogsearchresponse/topresult#Instance-Properties)

[`var artwork: Artwork?`](/documentation/musickit/musiccatalogsearchresponse/topresult/artwork)

The artwork of this top result for catalog search.

[`var id: MusicItemID`](/documentation/musickit/musiccatalogsearchresponse/topresult/id)

The unique identifier of this top result for catalog search.

[`var title: String`](/documentation/musickit/musiccatalogsearchresponse/topresult/title)

The title of this top result for catalog search.

## [Relationships](/documentation/musickit/musiccatalogsearchresponse/topresult#relationships)

### [Conforms To](/documentation/musickit/musiccatalogsearchresponse/topresult#conforms-to)

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
