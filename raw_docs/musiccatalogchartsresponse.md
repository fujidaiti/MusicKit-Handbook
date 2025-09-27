# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogchartsresponse

- [MusicKit](/documentation/musickit)
- MusicCatalogChartsResponse

Structure

# MusicCatalogChartsResponse

An object that contains results for a catalog charts request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicCatalogChartsResponse
```

## [Topics](/documentation/musickit/musiccatalogchartsresponse#topics)

### [Instance Properties](/documentation/musickit/musiccatalogchartsresponse#Instance-Properties)

[`let albumCharts: [MusicCatalogChart<Album>]`](/documentation/musickit/musiccatalogchartsresponse/albumcharts)

A collection of charts that contain albums.

[`let musicVideoCharts: [MusicCatalogChart<MusicVideo>]`](/documentation/musickit/musiccatalogchartsresponse/musicvideocharts)

A collection of charts that contain music videos.

[`let playlistCharts: [MusicCatalogChart<Playlist>]`](/documentation/musickit/musiccatalogchartsresponse/playlistcharts)

A collection of charts that contain playlists.

[`let songCharts: [MusicCatalogChart<Song>]`](/documentation/musickit/musiccatalogchartsresponse/songcharts)

A collection of charts that contain songs.

## [Relationships](/documentation/musickit/musiccatalogchartsresponse#relationships)

### [Conforms To](/documentation/musickit/musiccatalogchartsresponse#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
