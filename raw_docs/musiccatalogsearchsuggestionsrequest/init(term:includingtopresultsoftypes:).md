# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsrequest/init(term:includingtopresultsoftypes:)

- [MusicKit](/documentation/musickit)
- [MusicCatalogSearchSuggestionsRequest](/documentation/musickit/musiccatalogsearchsuggestionsrequest)
- init(term:includingTopResultsOfTypes:)

Initializer

# init(term:includingTopResultsOfTypes:)

Creates a catalog search suggestions request for a specified search term along with a list of types to include when fetching top results.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
init(
    term: String,
    includingTopResultsOfTypes types: [any MusicCatalogSearchable.Type] = []
)
```

## [Discussion](/documentation/musickit/musiccatalogsearchsuggestionsrequest/init(term:includingtopresultsoftypes:)#discussion)

By default, top results are not fetched.
