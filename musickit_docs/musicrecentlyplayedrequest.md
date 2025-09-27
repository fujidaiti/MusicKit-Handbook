# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicrecentlyplayedrequest

- [MusicKit](/documentation/musickit)
- MusicRecentlyPlayedRequest

Structure

# MusicRecentlyPlayedRequest

A request that your app uses to fetch items the user has recently played.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicRecentlyPlayedRequest<MusicItemType> where MusicItemType : MusicRecentlyPlayedRequestable, MusicItemType : Decodable
```

## [Topics](/documentation/musickit/musicrecentlyplayedrequest#topics)

### [Initializers](/documentation/musickit/musicrecentlyplayedrequest#Initializers)

[`init()`](/documentation/musickit/musicrecentlyplayedrequest/init())

Creates a request for items the user has recently played.

### [Instance Properties](/documentation/musickit/musicrecentlyplayedrequest#Instance-Properties)

[`var limit: Int?`](/documentation/musickit/musicrecentlyplayedrequest/limit)

A limit for the number of items to return in the response that contains items the user has recently played.

[`var offset: Int?`](/documentation/musickit/musicrecentlyplayedrequest/offset)

An offet for the request.

### [Instance Methods](/documentation/musickit/musicrecentlyplayedrequest#Instance-Methods)

[`func response() async throws -> MusicRecentlyPlayedResponse<MusicItemType>`](/documentation/musickit/musicrecentlyplayedrequest/response())

Fetches items the user has recently played.
