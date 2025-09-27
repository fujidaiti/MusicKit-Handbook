# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/librarymusicvideosortproperties

- [MusicKit](/documentation/musickit)
- LibraryMusicVideoSortProperties

Protocol

# LibraryMusicVideoSortProperties

Music video properties your app uses to sort results for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibraryMusicVideoSortProperties
```

## [Topics](/documentation/musickit/librarymusicvideosortproperties#topics)

### [Instance Properties](/documentation/musickit/librarymusicvideosortproperties#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/librarymusicvideosortproperties/albumtitle)

The title of the album the music video appears on.

**Required**

[`var artistName: String?`](/documentation/musickit/librarymusicvideosortproperties/artistname)

The artist’s name.

**Required**

[`var duration: TimeInterval?`](/documentation/musickit/librarymusicvideosortproperties/duration)

The duration of the music video.

**Required**

[`var lastPlayedDate: Date?`](/documentation/musickit/librarymusicvideosortproperties/lastplayeddate)

The date when the user last played the music video on this device.

**Required**

[`var libraryAddedDate: Date?`](/documentation/musickit/librarymusicvideosortproperties/libraryaddeddate)

The date when the user added the music video to the library.

**Required**

[`var playCount: Int?`](/documentation/musickit/librarymusicvideosortproperties/playcount)

The number of times the user played the music video.

**Required**

[`var title: String`](/documentation/musickit/librarymusicvideosortproperties/title)

The title of the music video.

**Required**

[`var trackNumber: Int?`](/documentation/musickit/librarymusicvideosortproperties/tracknumber)

The music video’s number in the album’s track list.

**Required**
