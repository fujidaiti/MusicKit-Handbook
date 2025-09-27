# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrary/error

- [MusicKit](/documentation/musickit)
- [MusicLibrary](/documentation/musickit/musiclibrary)
- MusicLibrary.Error

Enumeration

# MusicLibrary.Error

An error that the music library can throw upon accessing, manipulating, or requesting data from the user’s music library.

iOS 16.1+iPadOS 16.1+Mac Catalyst 17.0+macOS 14.0+tvOS 16.1+visionOS 1.0+watchOS 9.1+

```
enum Error
```

## [Topics](/documentation/musickit/musiclibrary/error#topics)

### [Enumeration Cases](/documentation/musickit/musiclibrary/error#Enumeration-Cases)

[`case addToPlaylistFailed`](/documentation/musickit/musiclibrary/error/addtoplaylistfailed)

An error that indicates a failure in the process of adding an item to a playlist.

[`case createPlaylistFailed`](/documentation/musickit/musiclibrary/error/createplaylistfailed)

An error that indicates a failure in the process of creating a playlist.

[`case editPlaylistFailed`](/documentation/musickit/musiclibrary/error/editplaylistfailed)

An error that indicates a failure in the process of editing a playlist.

[`case itemAlreadyAdded`](/documentation/musickit/musiclibrary/error/itemalreadyadded)

An error indicating that the item attempting to be added to the user’s music library is already in the library.

[`case permissionDenied`](/documentation/musickit/musiclibrary/error/permissiondenied)

An error that occurs when the user doesn’t consent for the current app to access their Apple Music library.

[`case playlistNotInLibrary`](/documentation/musickit/musiclibrary/error/playlistnotinlibrary)

An error indicating that the playlist attempting to be added to is not in the user’s library.

[`case unableToAddItem`](/documentation/musickit/musiclibrary/error/unabletoadditem)

An error indicating that the item attempting to be added to the user’s music library cannot be added.

[`case unknown`](/documentation/musickit/musiclibrary/error/unknown)

An error indicating the ocurrence of an unknown or unexpected error.

## [Relationships](/documentation/musickit/musiclibrary/error#relationships)

### [Conforms To](/documentation/musickit/musiclibrary/error#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Error`](/documentation/Swift/Error)
- [`Hashable`](/documentation/Swift/Hashable)
- [`LocalizedError`](/documentation/Foundation/LocalizedError)
- [`RawRepresentable`](/documentation/Swift/RawRepresentable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
