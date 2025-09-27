# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrary/createplaylist(name:description:authordisplayname:)

- [MusicKit](/documentation/musickit)
- [MusicLibrary](/documentation/musickit/musiclibrary)
- createPlaylist(name:description:authorDisplayName:)

Instance Method

# createPlaylist(name:description:authorDisplayName:)

Creates a playlist in the user’s music library.

iOS 16.0+iPadOS 16.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
@discardableResult
func createPlaylist(
    name: String,
    description: String? = nil,
    authorDisplayName: String? = nil
) async throws -> Playlist
```

## [Parameters](/documentation/musickit/musiclibrary/createplaylist(name:description:authordisplayname:)#parameters)

`name`
:   The name of the playlist.

`description`
:   An optional description of the playlist.

`authorDisplayName`
:   The display name of the author for the playlist. A `nil` value will result in
    the framework using your app’s name instead.

## [Return Value](/documentation/musickit/musiclibrary/createplaylist(name:description:authordisplayname:)#return-value)

The newly created playlist.
