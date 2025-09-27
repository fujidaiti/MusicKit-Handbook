# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogsearchrequest

- [MusicKit](/documentation/musickit)
- MusicCatalogSearchRequest

Structure

# MusicCatalogSearchRequest

A request that your app uses to fetch items from the Apple Music catalog using a search term.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicCatalogSearchRequest
```

## [Topics](/documentation/musickit/musiccatalogsearchrequest#topics)

### [Initializers](/documentation/musickit/musiccatalogsearchrequest#Initializers)

[`init(term: String, types: [any MusicCatalogSearchable.Type])`](/documentation/musickit/musiccatalogsearchrequest/init(term:types:))

Creates a catalog search request for a specified search term and list of catalog searchable types.

### [Instance Properties](/documentation/musickit/musiccatalogsearchrequest#Instance-Properties)

[`var includeTopResults: Bool`](/documentation/musickit/musiccatalogsearchrequest/includetopresults)

A Boolean value that indicates whether to request top search results.

[`var limit: Int?`](/documentation/musickit/musiccatalogsearchrequest/limit)

A limit for the number of items to return in the catalog search response.

[`var offset: Int?`](/documentation/musickit/musiccatalogsearchrequest/offset)

An offet for the request.

[`let term: String`](/documentation/musickit/musiccatalogsearchrequest/term)

The search term for the request.

[`var types: [any MusicCatalogSearchable.Type]`](/documentation/musickit/musiccatalogsearchrequest/types)

The list of requested catalog searchable types.

### [Instance Methods](/documentation/musickit/musiccatalogsearchrequest#Instance-Methods)

[`func response() async throws -> MusicCatalogSearchResponse`](/documentation/musickit/musiccatalogsearchrequest/response())

Fetches items of the requested catalog searchable types that match the search term of the request.

## [See Also](/documentation/musickit/musiccatalogsearchrequest#see-also)

### [Catalog Search](/documentation/musickit/musiccatalogsearchrequest#Catalog-Search)

[`struct MusicCatalogSearchResponse`](/documentation/musickit/musiccatalogsearchresponse)

An object that contains results for a catalog search request.

[`protocol MusicCatalogSearchable`](/documentation/musickit/musiccatalogsearchable)

A protocol for music items that your app can fetch by using a catalog search request.
