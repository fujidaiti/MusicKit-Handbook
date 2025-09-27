# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musictokenrequestoptions

- [MusicKit](/documentation/musickit)
- MusicTokenRequestOptions

Structure

# MusicTokenRequestOptions

Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicTokenRequestOptions
```

## [Topics](/documentation/musickit/musictokenrequestoptions#topics)

### [Type Properties](/documentation/musickit/musictokenrequestoptions#Type-Properties)

[`static let ignoreCache: MusicTokenRequestOptions`](/documentation/musickit/musictokenrequestoptions/ignorecache)

An option that indicates the token provider needs to discard any cached token and generate a new token.

## [Relationships](/documentation/musickit/musictokenrequestoptions#relationships)

### [Conforms To](/documentation/musickit/musictokenrequestoptions#conforms-to)

- [`Equatable`](/documentation/Swift/Equatable)
- [`ExpressibleByArrayLiteral`](/documentation/Swift/ExpressibleByArrayLiteral)
- [`OptionSet`](/documentation/Swift/OptionSet)
- [`RawRepresentable`](/documentation/Swift/RawRepresentable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
- [`SetAlgebra`](/documentation/Swift/SetAlgebra)

## [See Also](/documentation/musickit/musictokenrequestoptions#see-also)

### [Token management](/documentation/musickit/musictokenrequestoptions#Token-management)

[`typealias MusicTokenProvider`](/documentation/musickit/musictokenprovider)

An object that music requests use to access Apple Music API.

[`protocol MusicDeveloperTokenProvider`](/documentation/musickit/musicdevelopertokenprovider)

A set of methods that music requests use to access Apple Music API.

[`class MusicUserTokenProvider`](/documentation/musickit/musicusertokenprovider)

A class that music requests use to fetch user tokens your app requires to access Apple Music API.

[`enum MusicTokenRequestError`](/documentation/musickit/musictokenrequesterror)

An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.

[`class DefaultMusicTokenProvider`](/documentation/musickit/defaultmusictokenprovider)

The default token provider that music requests use to access Apple Music API.
