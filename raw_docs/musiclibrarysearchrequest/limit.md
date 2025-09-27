# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysearchrequest/limit

- [MusicKit](/documentation/musickit)
- [MusicLibrarySearchRequest](/documentation/musickit/musiclibrarysearchrequest)
- limit

Instance Property

# limit

A limit for the number of items to return in the library search response.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
var limit: Int
```

## [Discussion](/documentation/musickit/musiclibrarysearchrequest/limit#discussion)

The default value for this limit is 50.

If the application sets the limit to 0, the framework returns all matching items
in the user’s music library.
