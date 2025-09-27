# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/librarytrackfilter

- [MusicKit](/documentation/musickit)
- LibraryTrackFilter

Protocol

# LibraryTrackFilter

Track properties your app uses as a filter for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibraryTrackFilter
```

## [Topics](/documentation/musickit/librarytrackfilter#topics)

### [Instance Properties](/documentation/musickit/librarytrackfilter#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/librarytrackfilter/albumtitle)

The title of the album the track appears on.

**Required**

[`var albums: MusicItemCollection<Album>?`](/documentation/musickit/librarytrackfilter/albums)

The track’s associated albums.

**Required**

[`var artistName: String?`](/documentation/musickit/librarytrackfilter/artistname)

The artist’s name.

**Required**

[`var artists: MusicItemCollection<Artist>?`](/documentation/musickit/librarytrackfilter/artists)

The track’s associated artists.

**Required**

[`var genres: MusicItemCollection<Genre>?`](/documentation/musickit/librarytrackfilter/genres)

The track’s associated genres.

**Required**

[`var id: MusicItemID`](/documentation/musickit/librarytrackfilter/id)

The unique identifier for the track.

**Required**

[`var title: String`](/documentation/musickit/librarytrackfilter/title)

The title of the track.

**Required**
