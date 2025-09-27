# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/recentlyplayedmusicitem

- [MusicKit](/documentation/musickit)
- RecentlyPlayedMusicItem

Enumeration

# RecentlyPlayedMusicItem

An item that represents an album, a playlist, or a station that the user has recently played.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
enum RecentlyPlayedMusicItem
```

## [Topics](/documentation/musickit/recentlyplayedmusicitem#topics)

### [Enumeration Cases](/documentation/musickit/recentlyplayedmusicitem#Enumeration-Cases)

[`case album(Album)`](/documentation/musickit/recentlyplayedmusicitem/album(_:))

An item that corresponds to an album.

[`case playlist(Playlist)`](/documentation/musickit/recentlyplayedmusicitem/playlist(_:))

An item that corresponds to a playlist.

[`case station(Station)`](/documentation/musickit/recentlyplayedmusicitem/station(_:))

An item that corresponds to a station.

### [Instance Properties](/documentation/musickit/recentlyplayedmusicitem#Instance-Properties)

[`var artwork: Artwork?`](/documentation/musickit/recentlyplayedmusicitem/artwork)

The artwork of this item.

[`var id: MusicItemID`](/documentation/musickit/recentlyplayedmusicitem/id)

The unique identifier of this item.

[`var playParameters: PlayParameters?`](/documentation/musickit/recentlyplayedmusicitem/playparameters)

The parameters to use to play this item.

[`var subtitle: String?`](/documentation/musickit/recentlyplayedmusicitem/subtitle)

The subtitle of this item.

[`var title: String`](/documentation/musickit/recentlyplayedmusicitem/title)

The title of this item.

## [Relationships](/documentation/musickit/recentlyplayedmusicitem#relationships)

### [Conforms To](/documentation/musickit/recentlyplayedmusicitem#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`MusicItem`](/documentation/musickit/musicitem)
- [`MusicRecentlyPlayedRequestable`](/documentation/musickit/musicrecentlyplayedrequestable)
- [`PlayableMusicItem`](/documentation/musickit/playablemusicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
