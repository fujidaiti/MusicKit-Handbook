# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/librarysongfilter

- [MusicKit](/documentation/musickit)
- LibrarySongFilter

Protocol

# LibrarySongFilter

Song properties your app uses as a filter for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibrarySongFilter
```

## [Topics](/documentation/musickit/librarysongfilter#topics)

### [Instance Properties](/documentation/musickit/librarysongfilter#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/librarysongfilter/albumtitle)

The title of the album the song appears on.

**Required**

[`var albums: MusicItemCollection<Album>?`](/documentation/musickit/librarysongfilter/albums)

The song’s associated albums.

**Required**

[`var artistName: String?`](/documentation/musickit/librarysongfilter/artistname)

The artist’s name.

**Required**

[`var artists: MusicItemCollection<Artist>?`](/documentation/musickit/librarysongfilter/artists)

The song’s associated artists.

**Required**

[`var composerName: String?`](/documentation/musickit/librarysongfilter/composername)

The name of the song’s composer.

**Required**

[`var genres: MusicItemCollection<Genre>?`](/documentation/musickit/librarysongfilter/genres)

The song’s associated genres.

**Required**

[`var id: MusicItemID`](/documentation/musickit/librarysongfilter/id)

The unique identifier for the song.

**Required**

[`var title: String`](/documentation/musickit/librarysongfilter/title)

The title of the song.

**Required**
