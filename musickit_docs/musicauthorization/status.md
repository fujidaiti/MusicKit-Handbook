# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicauthorization/status

- [MusicKit](/documentation/musickit)
- [MusicAuthorization](/documentation/musickit/musicauthorization)
- MusicAuthorization.Status

Enumeration

# MusicAuthorization.Status

A value that indicates the authorization status the user sets for the current app to access their Apple Music data.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
enum Status
```

## [Topics](/documentation/musickit/musicauthorization/status#topics)

### [Enumeration Cases](/documentation/musickit/musicauthorization/status#Enumeration-Cases)

[`case authorized`](/documentation/musickit/musicauthorization/status/authorized)

The user granted permission for the current app to use MusicKit.

[`case denied`](/documentation/musickit/musicauthorization/status/denied)

The user denied permission for the current app to use MusicKit.

[`case notDetermined`](/documentation/musickit/musicauthorization/status/notdetermined)

The user has yet to decide whether to authorize the current app to use MusicKit.

[`case restricted`](/documentation/musickit/musicauthorization/status/restricted)

Apps on this device can’t access MusicKit in a way that the user can’t change.

## [Relationships](/documentation/musickit/musicauthorization/status#relationships)

### [Conforms To](/documentation/musickit/musicauthorization/status#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`RawRepresentable`](/documentation/Swift/RawRepresentable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
