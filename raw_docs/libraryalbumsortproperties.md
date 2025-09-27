# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/libraryalbumsortproperties

- [MusicKit](/documentation/musickit)
- LibraryAlbumSortProperties

Protocol

# LibraryAlbumSortProperties

Album properties your app uses to sort results for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibraryAlbumSortProperties
```

## [Topics](/documentation/musickit/libraryalbumsortproperties#topics)

### [Instance Properties](/documentation/musickit/libraryalbumsortproperties#Instance-Properties)

[`var artistName: String`](/documentation/musickit/libraryalbumsortproperties/artistname)

The artist’s name.

**Required**

[`var lastPlayedDate: Date?`](/documentation/musickit/libraryalbumsortproperties/lastplayeddate)

The date when the user last played the album on this device.

**Required**

[`var libraryAddedDate: Date?`](/documentation/musickit/libraryalbumsortproperties/libraryaddeddate)

The date when the user added the album to the library.

**Required**

[`var releaseDate: Date?`](/documentation/musickit/libraryalbumsortproperties/releasedate)

The release date (or expected prerelease date) for the album.

**Required**

[`var title: String`](/documentation/musickit/libraryalbumsortproperties/title)

The title of the album.

**Required**

[`var trackCount: Int`](/documentation/musickit/libraryalbumsortproperties/trackcount)

The number of tracks for the album.

**Required**
