# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/librarytracksortproperties

- [MusicKit](/documentation/musickit)
- LibraryTrackSortProperties

Protocol

# LibraryTrackSortProperties

Track properties your app uses to sort results for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibraryTrackSortProperties
```

## [Topics](/documentation/musickit/librarytracksortproperties#topics)

### [Instance Properties](/documentation/musickit/librarytracksortproperties#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/librarytracksortproperties/albumtitle)

The title of the album the track appears on.

**Required**

[`var artistName: String?`](/documentation/musickit/librarytracksortproperties/artistname)

The artist’s name.

**Required**

[`var discNumber: Int?`](/documentation/musickit/librarytracksortproperties/discnumber)

The disc number of the track.

**Required**

[`var duration: TimeInterval?`](/documentation/musickit/librarytracksortproperties/duration)

The duration of the track.

**Required**

[`var lastPlayedDate: Date?`](/documentation/musickit/librarytracksortproperties/lastplayeddate)

The date when the user last played the track on this device.

**Required**

[`var libraryAddedDate: Date?`](/documentation/musickit/librarytracksortproperties/libraryaddeddate)

The date when the user added the track to the library.

**Required**

[`var playCount: Int?`](/documentation/musickit/librarytracksortproperties/playcount)

The number of times the user played the track.

**Required**

[`var title: String`](/documentation/musickit/librarytracksortproperties/title)

The title of the track.

**Required**

[`var trackNumber: Int?`](/documentation/musickit/librarytracksortproperties/tracknumber)

The track’s number in the album’s track list.

**Required**
