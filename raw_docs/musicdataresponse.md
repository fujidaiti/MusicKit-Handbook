# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicdataresponse

- [MusicKit](/documentation/musickit)
- MusicDataResponse

Structure

# MusicDataResponse

An object containing results for a data request.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicDataResponse
```

## [Topics](/documentation/musickit/musicdataresponse#topics)

### [Instance Properties](/documentation/musickit/musicdataresponse#Instance-Properties)

[`let data: Data`](/documentation/musickit/musicdataresponse/data)

The raw data returned by the Apple Music API endpoint for the originating data request.

[`let urlResponse: HTTPURLResponse`](/documentation/musickit/musicdataresponse/urlresponse)

The URL response returned by the Apple Music API endpoint for the originating data request.

## [Relationships](/documentation/musickit/musicdataresponse#relationships)

### [Conforms To](/documentation/musickit/musicdataresponse#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/musicdataresponse#see-also)

### [General Purpose Data Request](/documentation/musickit/musicdataresponse#General-Purpose-Data-Request)

[`struct MusicDataRequest`](/documentation/musickit/musicdatarequest)

A request for loading data from an arbitrary Apple Music API endpoint.
