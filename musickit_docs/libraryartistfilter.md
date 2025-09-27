# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/libraryartistfilter

- [MusicKit](/documentation/musickit)
- LibraryArtistFilter

Protocol

# LibraryArtistFilter

Artist properties your app uses as a filter for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibraryArtistFilter
```

## [Topics](/documentation/musickit/libraryartistfilter#topics)

### [Instance Properties](/documentation/musickit/libraryartistfilter#Instance-Properties)

[`var genres: MusicItemCollection<Genre>?`](/documentation/musickit/libraryartistfilter/genres)

The artist’s associated genres.

**Required**

[`var id: MusicItemID`](/documentation/musickit/libraryartistfilter/id)

The unique identifier for the artist.

**Required**

[`var name: String`](/documentation/musickit/libraryartistfilter/name)

The name of the artist.

**Required**

[`var playlists: MusicItemCollection<Playlist>?`](/documentation/musickit/libraryartistfilter/playlists)

The artist’s associated playlists.

**Required**
