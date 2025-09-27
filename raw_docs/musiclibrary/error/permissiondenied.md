# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrary/error/permissiondenied

- [MusicKit](/documentation/musickit)
- [MusicLibrary](/documentation/musickit/musiclibrary)
- - [MusicLibrary](/documentation/musickit/musiclibrary)
- [MusicLibrary.Error](/documentation/musickit/musiclibrary/error)
- MusicLibrary.Error.permissionDenied

Case

# MusicLibrary.Error.permissionDenied

An error that occurs when the user doesn’t consent for the current app to access their Apple Music library.

iOS 16.1+iPadOS 16.1+Mac Catalyst 17.0+macOS 14.0+tvOS 16.1+visionOS 1.0+watchOS 9.1+

```
case permissionDenied
```

## [Discussion](/documentation/musickit/musiclibrary/error/permissiondenied#discussion)

Apps using MusicKit need to request prior informed consent from the user to
access their Apple Music library by calling
[`request()`](/documentation/musickit/musicauthorization/request()) at the
appropriate point in the app flow, right before needing to use other APIs from
MusicKit.
