# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/libraryalbumfilter

- [MusicKit](/documentation/musickit)
- LibraryAlbumFilter

Protocol

# LibraryAlbumFilter

Album properties your app uses as a filter for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibraryAlbumFilter
```

## [Topics](/documentation/musickit/libraryalbumfilter#topics)

### [Instance Properties](/documentation/musickit/libraryalbumfilter#Instance-Properties)

[`var artistName: String`](/documentation/musickit/libraryalbumfilter/artistname)

The artist’s name.

**Required**

[`var artists: MusicItemCollection<Artist>?`](/documentation/musickit/libraryalbumfilter/artists)

The album’s associated artists.

**Required**

[`var genres: MusicItemCollection<Genre>?`](/documentation/musickit/libraryalbumfilter/genres)

The genres for the album.

**Required**

[`var id: MusicItemID`](/documentation/musickit/libraryalbumfilter/id)

The unique identifier for the album.

**Required**

[`var isCompilation: Bool?`](/documentation/musickit/libraryalbumfilter/iscompilation)

A Boolean value that indicates whether the album is a compilation.

**Required**

[`var title: String`](/documentation/musickit/libraryalbumfilter/title)

The title of the album.

**Required**
