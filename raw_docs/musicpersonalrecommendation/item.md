# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicpersonalrecommendation/item

- [MusicKit](/documentation/musickit)
- [MusicPersonalRecommendation](/documentation/musickit/musicpersonalrecommendation)
- MusicPersonalRecommendation.Item

Enumeration

# MusicPersonalRecommendation.Item

An item that represents an album, a playlist, or a station for a personal recommendation.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
enum Item
```

## [Topics](/documentation/musickit/musicpersonalrecommendation/item#topics)

### [Enumeration Cases](/documentation/musickit/musicpersonalrecommendation/item#Enumeration-Cases)

[`case album(Album)`](/documentation/musickit/musicpersonalrecommendation/item/album(_:))

An item that corresponds to an album.

[`case playlist(Playlist)`](/documentation/musickit/musicpersonalrecommendation/item/playlist(_:))

An item that corresponds to a playlist.

[`case station(Station)`](/documentation/musickit/musicpersonalrecommendation/item/station(_:))

An item that corresponds to a station.

### [Instance Properties](/documentation/musickit/musicpersonalrecommendation/item#Instance-Properties)

[`var artwork: Artwork?`](/documentation/musickit/musicpersonalrecommendation/item/artwork)

The artwork of this item.

[`var id: MusicItemID`](/documentation/musickit/musicpersonalrecommendation/item/id)

The unique identifier of this item.

[`var subtitle: String?`](/documentation/musickit/musicpersonalrecommendation/item/subtitle)

The subtitle of this item.

[`var title: String`](/documentation/musickit/musicpersonalrecommendation/item/title)

The title of this item.

## [Relationships](/documentation/musickit/musicpersonalrecommendation/item#relationships)

### [Conforms To](/documentation/musickit/musicpersonalrecommendation/item#conforms-to)

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
