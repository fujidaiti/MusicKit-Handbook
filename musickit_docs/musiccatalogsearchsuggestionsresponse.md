# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsresponse

- [MusicKit](/documentation/musickit)
- MusicCatalogSearchSuggestionsResponse

Structure

# MusicCatalogSearchSuggestionsResponse

An object that contains results for a catalog search suggestions request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicCatalogSearchSuggestionsResponse
```

## [Topics](/documentation/musickit/musiccatalogsearchsuggestionsresponse#topics)

### [Structures](/documentation/musickit/musiccatalogsearchsuggestionsresponse#Structures)

[`struct Suggestion`](/documentation/musickit/musiccatalogsearchsuggestionsresponse/suggestion)

An item that represents a suggestion in the search suggestions response.

### [Instance Properties](/documentation/musickit/musiccatalogsearchsuggestionsresponse#Instance-Properties)

[`let suggestions: [MusicCatalogSearchSuggestionsResponse.Suggestion]`](/documentation/musickit/musiccatalogsearchsuggestionsresponse/suggestions)

A collection of suggested terms.

[`let topResults: MusicItemCollection<MusicCatalogSearchSuggestionsResponse.TopResult>`](/documentation/musickit/musiccatalogsearchsuggestionsresponse/topresults)

A collection of top results.

### [Type Aliases](/documentation/musickit/musiccatalogsearchsuggestionsresponse#Type-Aliases)

[`typealias TopResult`](/documentation/musickit/musiccatalogsearchsuggestionsresponse/topresult)

A type alias for an item that represents one of the top results in a catalog search suggestions response.

## [Relationships](/documentation/musickit/musiccatalogsearchsuggestionsresponse#relationships)

### [Conforms To](/documentation/musickit/musiccatalogsearchsuggestionsresponse#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
