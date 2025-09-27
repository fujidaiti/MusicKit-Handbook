# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicpersonalrecommendationsrequest

- [MusicKit](/documentation/musickit)
- MusicPersonalRecommendationsRequest

Structure

# MusicPersonalRecommendationsRequest

A request that your app uses to fetch music recommendations based on the user’s library and listening history.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicPersonalRecommendationsRequest
```

## [Topics](/documentation/musickit/musicpersonalrecommendationsrequest#topics)

### [Initializers](/documentation/musickit/musicpersonalrecommendationsrequest#Initializers)

[`init()`](/documentation/musickit/musicpersonalrecommendationsrequest/init())

Creates a request to fetch default personal recommendations for the user.

[`init<S>(refreshing: S)`](/documentation/musickit/musicpersonalrecommendationsrequest/init(refreshing:))

Creates a request to fetch default personal recommendations for the user.

### [Instance Properties](/documentation/musickit/musicpersonalrecommendationsrequest#Instance-Properties)

[`var limit: Int?`](/documentation/musickit/musicpersonalrecommendationsrequest/limit)

A limit for the number of recommendations to return in the personal recommendations response.

[`var offset: Int?`](/documentation/musickit/musicpersonalrecommendationsrequest/offset)

An offet for the request.

### [Instance Methods](/documentation/musickit/musicpersonalrecommendationsrequest#Instance-Methods)

[`func response() async throws -> MusicPersonalRecommendationsResponse`](/documentation/musickit/musicpersonalrecommendationsrequest/response())

Fetches the music recommendations based on the user’s library and listening history.

## [Relationships](/documentation/musickit/musicpersonalrecommendationsrequest#relationships)

### [Conforms To](/documentation/musickit/musicpersonalrecommendationsrequest#conforms-to)

- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
