# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicdatarequest/currentcountrycode

- [MusicKit](/documentation/musickit)
- [MusicDataRequest](/documentation/musickit/musicdatarequest)
- currentCountryCode

Type Property

# currentCountryCode

Fetches the current country code for the user’s Apple Music account.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
static var currentCountryCode: String { get async throws }
```

## [Discussion](/documentation/musickit/musicdatarequest/currentcountrycode#discussion)

The current country code may be useful to construct the URL for a
[`MusicDataRequest`](/documentation/musickit/musicdatarequest) because a typical
catalog endpoint for Apple Music API requires the inclusion of a country code in
the path of the corresponding URL.
