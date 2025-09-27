# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicdatarequest/error

- [MusicKit](/documentation/musickit)
- [MusicDataRequest](/documentation/musickit/musicdatarequest)
- MusicDataRequest.Error

Structure

# MusicDataRequest.Error

An error that the Apple Music API returns.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct Error
```

## [Topics](/documentation/musickit/musicdatarequest/error#topics)

### [Instance Properties](/documentation/musickit/musicdatarequest/error#Instance-Properties)

[`let code: Int`](/documentation/musickit/musicdatarequest/error/code)

The specific code for the underlying cause of the error.

[`let detailText: String`](/documentation/musickit/musicdatarequest/error/detailtext)

Additional detailed information about the cause of the error.

[`let id: String`](/documentation/musickit/musicdatarequest/error/id)

The identifier for the error.

[`let originalResponse: MusicDataResponse`](/documentation/musickit/musicdatarequest/error/originalresponse)

The original response that contains the error.

[`let source: MusicDataRequest.Error.Source?`](/documentation/musickit/musicdatarequest/error/source-swift.property)

The source of the error.

[`let status: Int`](/documentation/musickit/musicdatarequest/error/status)

The HTTP status code for the error.

[`let title: String`](/documentation/musickit/musicdatarequest/error/title)

A developer-friendly title for the error.

### [Enumerations](/documentation/musickit/musicdatarequest/error#Enumerations)

[`enum Source`](/documentation/musickit/musicdatarequest/error/source-swift.enum)

A representation of the source of an error from Apple Music API.

## [Relationships](/documentation/musickit/musicdatarequest/error#relationships)

### [Conforms To](/documentation/musickit/musicdatarequest/error#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Error`](/documentation/Swift/Error)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
