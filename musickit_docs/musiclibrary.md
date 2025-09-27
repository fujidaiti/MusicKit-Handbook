# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrary

- [MusicKit](/documentation/musickit)
- MusicLibrary

Class

# MusicLibrary

An object your app uses to access the user’s music library.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
class MusicLibrary
```

## [Topics](/documentation/musickit/musiclibrary#topics)

### [Instance Methods](/documentation/musickit/musiclibrary#Instance-Methods)

[`func add<MusicItemType>(MusicItemType) async throws`](/documentation/musickit/musiclibrary/add(_:))

Adds an item to the user’s music library.

[`func add<MusicItemType>(MusicItemType, to: Playlist) async throws -> Playlist`](/documentation/musickit/musiclibrary/add(_:to:))

Adds an item to the end of an existing playlist.

[`func createPlaylist(name: String, description: String?, authorDisplayName: String?) async throws -> Playlist`](/documentation/musickit/musiclibrary/createplaylist(name:description:authordisplayname:))

Creates a playlist in the user’s music library.

[`func createPlaylist<S, MusicPlaylistAddableType>(name: String, description: String?, authorDisplayName: String?, items: S) async throws -> Playlist`](/documentation/musickit/musiclibrary/createplaylist(name:description:authordisplayname:items:))

Creates a playlist in the user’s music library.

[`func edit(Playlist, name: String?, description: String?, authorDisplayName: String?) async throws -> Playlist`](/documentation/musickit/musiclibrary/edit(_:name:description:authordisplayname:))

Edits a playlist that your app has created.

[`func edit<S, MusicPlaylistAddableType>(Playlist, name: String?, description: String?, authorDisplayName: String?, items: S) async throws -> Playlist`](/documentation/musickit/musiclibrary/edit(_:name:description:authordisplayname:items:))

Edits a playlist that your app has created including items to rebuild the list of entries.

### [Type Properties](/documentation/musickit/musiclibrary#Type-Properties)

[`static let shared: MusicLibrary`](/documentation/musickit/musiclibrary/shared)

A shared object that allows your app to modify the user’s music library.

### [Enumerations](/documentation/musickit/musiclibrary#Enumerations)

[`enum Error`](/documentation/musickit/musiclibrary/error)

An error that the music library can throw upon accessing, manipulating, or requesting data from the user’s music library.
