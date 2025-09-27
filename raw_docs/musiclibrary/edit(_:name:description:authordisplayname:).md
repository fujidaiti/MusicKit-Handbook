# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrary/edit(_:name:description:authordisplayname:)

- [MusicKit](/documentation/musickit)
- [MusicLibrary](/documentation/musickit/musiclibrary)
- edit(\_:name:description:authorDisplayName:)

Instance Method

# edit(\_:name:description:authorDisplayName:)

Edits a playlist that your app has created.

iOS 16.0+iPadOS 16.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
@discardableResult
func edit(
    _ playlist: Playlist,
    name: String? = nil,
    description: String? = nil,
    authorDisplayName: String? = nil
) async throws -> Playlist
```

## [Return Value](/documentation/musickit/musiclibrary/edit(_:name:description:authordisplayname:)#return-value)

The edited playlist.

## [Discussion](/documentation/musickit/musiclibrary/edit(_:name:description:authordisplayname:)#discussion)

This function will throw an error if your app attempts to edit a playlist that
another app created.
