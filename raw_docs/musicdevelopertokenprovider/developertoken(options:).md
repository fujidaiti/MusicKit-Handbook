# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicdevelopertokenprovider/developertoken(options:)

- [MusicKit](/documentation/musickit)
- [MusicDeveloperTokenProvider](/documentation/musickit/musicdevelopertokenprovider)
- developerToken(options:)

Instance Method

# developerToken(options:)

Fetches and returns a developer token for Apple Music API.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
func developerToken(options: MusicTokenRequestOptions) async throws -> String
```

**Required**

## [Discussion](/documentation/musickit/musicdevelopertokenprovider/developertoken(options:)#discussion)

If you opt to create a custom implementation of the
[`MusicDeveloperTokenProvider`](/documentation/musickit/musicdevelopertokenprovider)
protocol, make sure to discard any cached developer token if the `options`
parameter contains
[`ignoreCache`](/documentation/musickit/musictokenrequestoptions/ignorecache).

You can add the newly generated token to an in-memory or persistent cache for
faster access upon subsequent requests for this token.
