# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/defaultmusictokenprovider

- [MusicKit](/documentation/musickit)
- DefaultMusicTokenProvider

Class

# DefaultMusicTokenProvider

The default token provider that music requests use to access Apple Music API.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
class DefaultMusicTokenProvider
```

## [Topics](/documentation/musickit/defaultmusictokenprovider#topics)

### [Initializers](/documentation/musickit/defaultmusictokenprovider#Initializers)

[`init()`](/documentation/musickit/defaultmusictokenprovider/init())

Creates a user token provider.

## [Relationships](/documentation/musickit/defaultmusictokenprovider#relationships)

### [Inherits From](/documentation/musickit/defaultmusictokenprovider#inherits-from)

- [`MusicUserTokenProvider`](/documentation/musickit/musicusertokenprovider)

### [Conforms To](/documentation/musickit/defaultmusictokenprovider#conforms-to)

- [`MusicDeveloperTokenProvider`](/documentation/musickit/musicdevelopertokenprovider)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/defaultmusictokenprovider#see-also)

### [Token management](/documentation/musickit/defaultmusictokenprovider#Token-management)

[`typealias MusicTokenProvider`](/documentation/musickit/musictokenprovider)

An object that music requests use to access Apple Music API.

[`protocol MusicDeveloperTokenProvider`](/documentation/musickit/musicdevelopertokenprovider)

A set of methods that music requests use to access Apple Music API.

[`class MusicUserTokenProvider`](/documentation/musickit/musicusertokenprovider)

A class that music requests use to fetch user tokens your app requires to access Apple Music API.

[`struct MusicTokenRequestOptions`](/documentation/musickit/musictokenrequestoptions)

Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.

[`enum MusicTokenRequestError`](/documentation/musickit/musictokenrequesterror)

An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.
