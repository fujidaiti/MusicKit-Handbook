# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicusertokenprovider

- [MusicKit](/documentation/musickit)
- MusicUserTokenProvider

Class

# MusicUserTokenProvider

A class that music requests use to fetch user tokens your app requires to access Apple Music API.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
class MusicUserTokenProvider
```

## [Topics](/documentation/musickit/musicusertokenprovider#topics)

### [Initializers](/documentation/musickit/musicusertokenprovider#Initializers)

[`init()`](/documentation/musickit/musicusertokenprovider/init())

Creates a user token provider.

### [Instance Methods](/documentation/musickit/musicusertokenprovider#Instance-Methods)

[`func userToken(for: String, options: MusicTokenRequestOptions) async throws -> String`](/documentation/musickit/musicusertokenprovider/usertoken(for:options:))

Fetches and returns a user token for Apple Music API.

## [Relationships](/documentation/musickit/musicusertokenprovider#relationships)

### [Inherited By](/documentation/musickit/musicusertokenprovider#inherited-by)

- [`DefaultMusicTokenProvider`](/documentation/musickit/defaultmusictokenprovider)

## [See Also](/documentation/musickit/musicusertokenprovider#see-also)

### [Token management](/documentation/musickit/musicusertokenprovider#Token-management)

[`typealias MusicTokenProvider`](/documentation/musickit/musictokenprovider)

An object that music requests use to access Apple Music API.

[`protocol MusicDeveloperTokenProvider`](/documentation/musickit/musicdevelopertokenprovider)

A set of methods that music requests use to access Apple Music API.

[`struct MusicTokenRequestOptions`](/documentation/musickit/musictokenrequestoptions)

Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.

[`enum MusicTokenRequestError`](/documentation/musickit/musictokenrequesterror)

An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.

[`class DefaultMusicTokenProvider`](/documentation/musickit/defaultmusictokenprovider)

The default token provider that music requests use to access Apple Music API.
