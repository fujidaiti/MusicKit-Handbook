# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicauthorization

- [MusicKit](/documentation/musickit)
- MusicAuthorization

Structure

# MusicAuthorization

A type that allows you to request the user’s informed consent for your app to access their music data.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicAuthorization
```

## [Topics](/documentation/musickit/musicauthorization#topics)

### [Type Properties](/documentation/musickit/musicauthorization#Type-Properties)

[`static var currentStatus: MusicAuthorization.Status`](/documentation/musickit/musicauthorization/currentstatus)

The authorization status the user sets for accessing MusicKit.

### [Type Methods](/documentation/musickit/musicauthorization#Type-Methods)

[`static func request() async -> MusicAuthorization.Status`](/documentation/musickit/musicauthorization/request())

Asks the user for permission for the current app to access MusicKit.

### [Enumerations](/documentation/musickit/musicauthorization#Enumerations)

[`enum Status`](/documentation/musickit/musicauthorization/status)

A value that indicates the authorization status the user sets for the current app to access their Apple Music data.
