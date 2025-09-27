# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicpersonalrecommendation

- [MusicKit](/documentation/musickit)
- MusicPersonalRecommendation

Structure

# MusicPersonalRecommendation

An object that contains recommended items based on the user’s library and listening history.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicPersonalRecommendation
```

## [Topics](/documentation/musickit/musicpersonalrecommendation#topics)

### [Instance Properties](/documentation/musickit/musicpersonalrecommendation#Instance-Properties)

[`var albums: MusicItemCollection<Album>`](/documentation/musickit/musicpersonalrecommendation/albums)

The albums for the personal recommendation.

[`let id: MusicItemID`](/documentation/musickit/musicpersonalrecommendation/id)

The unique identifier for the personal recommendation.

[`var items: MusicItemCollection<MusicPersonalRecommendation.Item>`](/documentation/musickit/musicpersonalrecommendation/items)

The items for the personal recommendation.

[`let nextRefreshDate: Date?`](/documentation/musickit/musicpersonalrecommendation/nextrefreshdate)

The next date for refreshing the personal recommendation.

[`var playlists: MusicItemCollection<Playlist>`](/documentation/musickit/musicpersonalrecommendation/playlists)

The playlists for the personal recommendation.

[`let reason: String?`](/documentation/musickit/musicpersonalrecommendation/reason)

The reason for the personal recommendation.

[`var stations: MusicItemCollection<Station>`](/documentation/musickit/musicpersonalrecommendation/stations)

The stations for the personal recommendation.

[`let title: String?`](/documentation/musickit/musicpersonalrecommendation/title)

The title for the personal recommendation.

[`var types: [any MusicPersonalRecommendationItem.Type]`](/documentation/musickit/musicpersonalrecommendation/types)

The types of items in the personal recommendation.

### [Enumerations](/documentation/musickit/musicpersonalrecommendation#Enumerations)

[`enum Item`](/documentation/musickit/musicpersonalrecommendation/item)

An item that represents an album, a playlist, or a station for a personal recommendation.

## [Relationships](/documentation/musickit/musicpersonalrecommendation#relationships)

### [Conforms To](/documentation/musickit/musicpersonalrecommendation#conforms-to)

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
