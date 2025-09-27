# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsrequest

- [MusicKit](/documentation/musickit)
- MusicCatalogSearchSuggestionsRequest

Structure

# MusicCatalogSearchSuggestionsRequest

A request that your app uses to fetch suggestions from the Apple Music catalog using a search term.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicCatalogSearchSuggestionsRequest
```

## [Topics](/documentation/musickit/musiccatalogsearchsuggestionsrequest#topics)

### [Initializers](/documentation/musickit/musiccatalogsearchsuggestionsrequest#Initializers)

[`init(term: String, includingTopResultsOfTypes: [any MusicCatalogSearchable.Type])`](/documentation/musickit/musiccatalogsearchsuggestionsrequest/init(term:includingtopresultsoftypes:))

Creates a catalog search suggestions request for a specified search term along with a list of types to include when fetching top results.

### [Instance Properties](/documentation/musickit/musiccatalogsearchsuggestionsrequest#Instance-Properties)

[`var limit: Int?`](/documentation/musickit/musiccatalogsearchsuggestionsrequest/limit)

A limit for the number of items to return in the catalog search suggestions response.

[`let term: String`](/documentation/musickit/musiccatalogsearchsuggestionsrequest/term)

The search term for the request.

[`var typesForTopResults: [any MusicCatalogSearchable.Type]`](/documentation/musickit/musiccatalogsearchsuggestionsrequest/typesfortopresults)

The list of requested types for top results.

### [Instance Methods](/documentation/musickit/musiccatalogsearchsuggestionsrequest#Instance-Methods)

[`func response() async throws -> MusicCatalogSearchSuggestionsResponse`](/documentation/musickit/musiccatalogsearchsuggestionsrequest/response())

Fetches suggestions of the requested catalog searchable types that match the search term of the request.
