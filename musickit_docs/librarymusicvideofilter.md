# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/librarymusicvideofilter

- [MusicKit](/documentation/musickit)
- LibraryMusicVideoFilter

Protocol

# LibraryMusicVideoFilter

Music video properties your app uses as a filter for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibraryMusicVideoFilter
```

## [Topics](/documentation/musickit/librarymusicvideofilter#topics)

### [Instance Properties](/documentation/musickit/librarymusicvideofilter#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/librarymusicvideofilter/albumtitle)

The title of the album the music video appears on.

**Required**

[`var albums: MusicItemCollection<Album>?`](/documentation/musickit/librarymusicvideofilter/albums)

The music video’s associated albums.

**Required**

[`var artistName: String?`](/documentation/musickit/librarymusicvideofilter/artistname)

The artist’s name.

**Required**

[`var artists: MusicItemCollection<Artist>?`](/documentation/musickit/librarymusicvideofilter/artists)

The music video’s associated artists.

**Required**

[`var genres: MusicItemCollection<Genre>?`](/documentation/musickit/librarymusicvideofilter/genres)

The music video’s associated genres.

**Required**

[`var id: MusicItemID`](/documentation/musickit/librarymusicvideofilter/id)

The unique identifier for the music video.

**Required**

[`var title: String`](/documentation/musickit/librarymusicvideofilter/title)

The title of the music video.

**Required**
