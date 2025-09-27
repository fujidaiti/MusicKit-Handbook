# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogsearchable

- [MusicKit](/documentation/musickit)
- MusicCatalogSearchable

Protocol

# MusicCatalogSearchable

A protocol for music items that your app can fetch by using a catalog search request.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
protocol MusicCatalogSearchable : MusicItem
```

## [Relationships](/documentation/musickit/musiccatalogsearchable#relationships)

### [Inherits From](/documentation/musickit/musiccatalogsearchable#inherits-from)

- [`MusicItem`](/documentation/musickit/musicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

### [Conforming Types](/documentation/musickit/musiccatalogsearchable#conforming-types)

- [`Album`](/documentation/musickit/album)
- [`Artist`](/documentation/musickit/artist)
- [`Curator`](/documentation/musickit/curator)
- [`MusicVideo`](/documentation/musickit/musicvideo)
- [`Playlist`](/documentation/musickit/playlist)
- [`RadioShow`](/documentation/musickit/radioshow)
- [`RecordLabel`](/documentation/musickit/recordlabel)
- [`Song`](/documentation/musickit/song)
- [`Station`](/documentation/musickit/station)

## [See Also](/documentation/musickit/musiccatalogsearchable#see-also)

### [Catalog Search](/documentation/musickit/musiccatalogsearchable#Catalog-Search)

[`struct MusicCatalogSearchRequest`](/documentation/musickit/musiccatalogsearchrequest)

A request that your app uses to fetch items from the Apple Music catalog using a search term.

[`struct MusicCatalogSearchResponse`](/documentation/musickit/musiccatalogsearchresponse)

An object that contains results for a catalog search request.
