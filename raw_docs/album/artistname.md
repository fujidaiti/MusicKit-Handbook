# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/album/artistname

- [MusicKit](/documentation/musickit)
- [Album](/documentation/musickit/album)
- artistName

Instance Property

# artistName

The artist’s name.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
var artistName: String { get }
```

## [Discussion](/documentation/musickit/album/artistname#discussion)

You can find more precise information about this album’s artists in the
[`artists`](/documentation/musickit/album/artists) relationship, which, unlike
[`artistName`](/documentation/musickit/album/artistname), requires that you load
it explicitly using the
[`with(_:)`](/documentation/musickit/musicpropertycontainer/with(_:)) method, as
in the following example:

```
    let detailedAlbum = try await album.with([.artists])
    let firstArtist = album.artists?.first
```
