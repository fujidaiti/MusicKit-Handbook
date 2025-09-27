# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicdevelopertokenprovider

- [MusicKit](/documentation/musickit)
- MusicDeveloperTokenProvider

Protocol

# MusicDeveloperTokenProvider

A set of methods that music requests use to access Apple Music API.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
protocol MusicDeveloperTokenProvider : Sendable
```

## [Topics](/documentation/musickit/musicdevelopertokenprovider#topics)

### [Instance Methods](/documentation/musickit/musicdevelopertokenprovider#Instance-Methods)

[`func developerToken(options: MusicTokenRequestOptions) async throws -> String`](/documentation/musickit/musicdevelopertokenprovider/developertoken(options:))

Fetches and returns a developer token for Apple Music API.

**Required**

## [Relationships](/documentation/musickit/musicdevelopertokenprovider#relationships)

### [Inherits From](/documentation/musickit/musicdevelopertokenprovider#inherits-from)

- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

### [Conforming Types](/documentation/musickit/musicdevelopertokenprovider#conforming-types)

- [`DefaultMusicTokenProvider`](/documentation/musickit/defaultmusictokenprovider)

## [See Also](/documentation/musickit/musicdevelopertokenprovider#see-also)

### [Token management](/documentation/musickit/musicdevelopertokenprovider#Token-management)

[`typealias MusicTokenProvider`](/documentation/musickit/musictokenprovider)

An object that music requests use to access Apple Music API.

[`class MusicUserTokenProvider`](/documentation/musickit/musicusertokenprovider)

A class that music requests use to fetch user tokens your app requires to access Apple Music API.

[`struct MusicTokenRequestOptions`](/documentation/musickit/musictokenrequestoptions)

Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.

[`enum MusicTokenRequestError`](/documentation/musickit/musictokenrequesterror)

An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.

[`class DefaultMusicTokenProvider`](/documentation/musickit/defaultmusictokenprovider)

The default token provider that music requests use to access Apple Music API.
