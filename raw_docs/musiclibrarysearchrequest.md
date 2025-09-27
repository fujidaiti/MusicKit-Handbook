# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysearchrequest

- [MusicKit](/documentation/musickit)
- MusicLibrarySearchRequest

Structure

# MusicLibrarySearchRequest

A request that your app uses to fetch items from user’s library using a search term.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicLibrarySearchRequest
```

## [Topics](/documentation/musickit/musiclibrarysearchrequest#topics)

### [Initializers](/documentation/musickit/musiclibrarysearchrequest#Initializers)

[`init(term: String, types: [any MusicLibrarySearchable.Type])`](/documentation/musickit/musiclibrarysearchrequest/init(term:types:))

Creates a library search request for a specified search term and list of library searchable types.

### [Instance Properties](/documentation/musickit/musiclibrarysearchrequest#Instance-Properties)

[`var includeTopResults: Bool`](/documentation/musickit/musiclibrarysearchrequest/includetopresults)

A Boolean value that indicates whether to request top search results.

[`var limit: Int`](/documentation/musickit/musiclibrarysearchrequest/limit)

A limit for the number of items to return in the library search response.

[`let term: String`](/documentation/musickit/musiclibrarysearchrequest/term)

The search term for the request.

[`var types: [any MusicLibrarySearchable.Type]`](/documentation/musickit/musiclibrarysearchrequest/types)

The list of requested library searchable types.

### [Instance Methods](/documentation/musickit/musiclibrarysearchrequest#Instance-Methods)

[`func response() async throws -> MusicLibrarySearchResponse`](/documentation/musickit/musiclibrarysearchrequest/response())

Fetches items of the requested library searchable types that match the search term of the request.

## [Relationships](/documentation/musickit/musiclibrarysearchrequest#relationships)

### [Conforms To](/documentation/musickit/musiclibrarysearchrequest#conforms-to)

- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
