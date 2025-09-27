# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogchartsrequest

- [MusicKit](/documentation/musickit)
- MusicCatalogChartsRequest

Structure

# MusicCatalogChartsRequest

A request that your app uses to fetch the most popular items in the Apple Music catalog.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicCatalogChartsRequest
```

## [Topics](/documentation/musickit/musiccatalogchartsrequest#topics)

### [Initializers](/documentation/musickit/musiccatalogchartsrequest#Initializers)

[`init(genre: Genre?, kinds: [MusicCatalogChartKind], types: [any MusicCatalogChartRequestable.Type])`](/documentation/musickit/musiccatalogchartsrequest/init(genre:kinds:types:))

Creates a catalog charts request for a specified genre and list of types to include in the catalog charts response.

### [Instance Properties](/documentation/musickit/musiccatalogchartsrequest#Instance-Properties)

[`var genre: Genre?`](/documentation/musickit/musiccatalogchartsrequest/genre)

The genre for the request.

[`var kinds: [MusicCatalogChartKind]`](/documentation/musickit/musiccatalogchartsrequest/kinds)

The kinds of requested catalog charts.

[`var limit: Int?`](/documentation/musickit/musiccatalogchartsrequest/limit)

A limit for the number of items to return in the catalog search response.

[`var offset: Int?`](/documentation/musickit/musiccatalogchartsrequest/offset)

An offet for the request.

[`var types: [any MusicCatalogChartRequestable.Type]`](/documentation/musickit/musiccatalogchartsrequest/types)

The list of requested types for the catalog charts response.

### [Instance Methods](/documentation/musickit/musiccatalogchartsrequest#Instance-Methods)

[`func response() async throws -> MusicCatalogChartsResponse`](/documentation/musickit/musiccatalogchartsrequest/response())

Fetches the most popular items of the requested types that match the genre and kinds for the request.

## [Relationships](/documentation/musickit/musiccatalogchartsrequest#relationships)

### [Conforms To](/documentation/musickit/musiccatalogchartsrequest#conforms-to)

- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
