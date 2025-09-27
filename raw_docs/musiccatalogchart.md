# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogchart

- [MusicKit](/documentation/musickit)
- MusicCatalogChart

Structure

# MusicCatalogChart

An object that contains popular items in the Apple Music catalog.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicCatalogChart<MusicItemType> where MusicItemType : MusicCatalogChartRequestable
```

## [Topics](/documentation/musickit/musiccatalogchart#topics)

### [Instance Properties](/documentation/musickit/musiccatalogchart#Instance-Properties)

[`let id: String`](/documentation/musickit/musiccatalogchart/id)

The unique identifier for the catalog chart.

[`let items: MusicItemCollection<MusicItemType>`](/documentation/musickit/musiccatalogchart/items)

The items for the catalog chart.

[`let kind: MusicCatalogChartKind`](/documentation/musickit/musiccatalogchart/kind)

The kind of catalog chart.

[`let title: String`](/documentation/musickit/musiccatalogchart/title)

The title for the catalog chart.

## [Relationships](/documentation/musickit/musiccatalogchart#relationships)

### [Conforms To](/documentation/musickit/musiccatalogchart#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
