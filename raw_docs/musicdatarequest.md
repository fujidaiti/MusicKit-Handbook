# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicdatarequest

- [MusicKit](/documentation/musickit)
- MusicDataRequest

Structure

# MusicDataRequest

A request for loading data from an arbitrary Apple Music API endpoint.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicDataRequest
```

## [Topics](/documentation/musickit/musicdatarequest#topics)

### [Structures](/documentation/musickit/musicdatarequest#Structures)

[`struct Error`](/documentation/musickit/musicdatarequest/error)

An error that the Apple Music API returns.

### [Initializers](/documentation/musickit/musicdatarequest#Initializers)

[`init(urlRequest: URLRequest)`](/documentation/musickit/musicdatarequest/init(urlrequest:))

Creates a data request with a URL request.

### [Instance Properties](/documentation/musickit/musicdatarequest#Instance-Properties)

[`let urlRequest: URLRequest`](/documentation/musickit/musicdatarequest/urlrequest)

The URL request for the data request.

### [Instance Methods](/documentation/musickit/musicdatarequest#Instance-Methods)

[`func response() async throws -> MusicDataResponse`](/documentation/musickit/musicdatarequest/response())

Fetches data from the Apple Music API endpoint that the URL request defines.

### [Type Properties](/documentation/musickit/musicdatarequest#Type-Properties)

[`static var currentCountryCode: String`](/documentation/musickit/musicdatarequest/currentcountrycode)

Fetches the current country code for the user’s Apple Music account.

[`static var tokenProvider: any MusicUserTokenProvider & MusicDeveloperTokenProvider`](/documentation/musickit/musicdatarequest/tokenprovider)

The shared token provider for fetching tokens that Apple Music API requires.

## [Relationships](/documentation/musickit/musicdatarequest#relationships)

### [Conforms To](/documentation/musickit/musicdatarequest#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/musicdatarequest#see-also)

### [General Purpose Data Request](/documentation/musickit/musicdatarequest#General-Purpose-Data-Request)

[`struct MusicDataResponse`](/documentation/musickit/musicdataresponse)

An object containing results for a data request.
