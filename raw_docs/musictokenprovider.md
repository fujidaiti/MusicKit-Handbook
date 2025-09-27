# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musictokenprovider

- [MusicKit](/documentation/musickit)
- MusicTokenProvider

Type Alias

# MusicTokenProvider

An object that music requests use to access Apple Music API.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
typealias MusicTokenProvider = MusicUserTokenProvider & MusicDeveloperTokenProvider
```

## [Discussion](/documentation/musickit/musictokenprovider#discussion)

A token provider for MusicKit needs to be a subclass of
[`MusicUserTokenProvider`](/documentation/musickit/musicusertokenprovider) which
conforms to the
[`MusicDeveloperTokenProvider`](/documentation/musickit/musicdevelopertokenprovider)
protocol.

## [See Also](/documentation/musickit/musictokenprovider#see-also)

### [Token management](/documentation/musickit/musictokenprovider#Token-management)

[`protocol MusicDeveloperTokenProvider`](/documentation/musickit/musicdevelopertokenprovider)

A set of methods that music requests use to access Apple Music API.

[`class MusicUserTokenProvider`](/documentation/musickit/musicusertokenprovider)

A class that music requests use to fetch user tokens your app requires to access Apple Music API.

[`struct MusicTokenRequestOptions`](/documentation/musickit/musictokenrequestoptions)

Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.

[`enum MusicTokenRequestError`](/documentation/musickit/musictokenrequesterror)

An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.

[`class DefaultMusicTokenProvider`](/documentation/musickit/defaultmusictokenprovider)

The default token provider that music requests use to access Apple Music API.
