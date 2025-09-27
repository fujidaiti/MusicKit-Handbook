# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicsubscription/error

- [MusicKit](/documentation/musickit)
- [MusicSubscription](/documentation/musickit/musicsubscription)
- MusicSubscription.Error

Enumeration

# MusicSubscription.Error

An error that MusicKit can throw upon requesting the current music subscription of the user.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
enum Error
```

## [Topics](/documentation/musickit/musicsubscription/error#topics)

### [Enumeration Cases](/documentation/musickit/musicsubscription/error#Enumeration-Cases)

[`case permissionDenied`](/documentation/musickit/musicsubscription/error/permissiondenied)

An error indicating that the user doesn’t consent for your app to access their Apple Music data.

[`case privacyAcknowledgementRequired`](/documentation/musickit/musicsubscription/error/privacyacknowledgementrequired)

An error indicating that the user needs to acknowledge the most-recent privacy policy for Apple Music.

[`case unknown`](/documentation/musickit/musicsubscription/error/unknown)

An error indicating the ocurrence of an unknown or unexpected error.

## [Relationships](/documentation/musickit/musicsubscription/error#relationships)

### [Conforms To](/documentation/musickit/musicsubscription/error#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Error`](/documentation/Swift/Error)
- [`Hashable`](/documentation/Swift/Hashable)
- [`LocalizedError`](/documentation/Foundation/LocalizedError)
- [`RawRepresentable`](/documentation/Swift/RawRepresentable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
