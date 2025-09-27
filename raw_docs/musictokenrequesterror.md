# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musictokenrequesterror

- [MusicKit](/documentation/musickit)
- MusicTokenRequestError

Enumeration

# MusicTokenRequestError

An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
enum MusicTokenRequestError
```

## [Topics](/documentation/musickit/musictokenrequesterror#topics)

### [Enumeration Cases](/documentation/musickit/musictokenrequesterror#Enumeration-Cases)

[`case developerTokenRequestFailed`](/documentation/musickit/musictokenrequesterror/developertokenrequestfailed)

An error that indicates a failure in the process of fetching a developer token for the current app.

[`case permissionDenied`](/documentation/musickit/musictokenrequesterror/permissiondenied)

An error that occurs when the user doesn’t consent for the current app to access their Apple Music data.

[`case privacyAcknowledgementRequired`](/documentation/musickit/musictokenrequesterror/privacyacknowledgementrequired)

An error that occurs when the user needs to acknowledge the most recent privacy policy.

[`case unknown`](/documentation/musickit/musictokenrequesterror/unknown)

An error indicating the ocurrence of an unknown or unexpected error.

[`case userNotSignedIn`](/documentation/musickit/musictokenrequesterror/usernotsignedin)

An error that occurs when the user isn’t signed in with an Apple Music account.

[`case userTokenRequestFailed`](/documentation/musickit/musictokenrequesterror/usertokenrequestfailed)

An error that indicates a failure in the process of fetching a user token.

[`case userTokenRevoked`](/documentation/musickit/musictokenrequesterror/usertokenrevoked)

An error that occurs when the user revokes permission for the current app to access their Apple Music data.

## [Relationships](/documentation/musickit/musictokenrequesterror#relationships)

### [Conforms To](/documentation/musickit/musictokenrequesterror#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Error`](/documentation/Swift/Error)
- [`Hashable`](/documentation/Swift/Hashable)
- [`LocalizedError`](/documentation/Foundation/LocalizedError)
- [`RawRepresentable`](/documentation/Swift/RawRepresentable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/musictokenrequesterror#see-also)

### [Token management](/documentation/musickit/musictokenrequesterror#Token-management)

[`typealias MusicTokenProvider`](/documentation/musickit/musictokenprovider)

An object that music requests use to access Apple Music API.

[`protocol MusicDeveloperTokenProvider`](/documentation/musickit/musicdevelopertokenprovider)

A set of methods that music requests use to access Apple Music API.

[`class MusicUserTokenProvider`](/documentation/musickit/musicusertokenprovider)

A class that music requests use to fetch user tokens your app requires to access Apple Music API.

[`struct MusicTokenRequestOptions`](/documentation/musickit/musictokenrequestoptions)

Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.

[`class DefaultMusicTokenProvider`](/documentation/musickit/defaultmusictokenprovider)

The default token provider that music requests use to access Apple Music API.
