# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/librarysongsortproperties

- [MusicKit](/documentation/musickit)
- LibrarySongSortProperties

Protocol

# LibrarySongSortProperties

Song properties your app uses to sort results for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibrarySongSortProperties
```

## [Topics](/documentation/musickit/librarysongsortproperties#topics)

### [Instance Properties](/documentation/musickit/librarysongsortproperties#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/librarysongsortproperties/albumtitle)

The title of the album the song appears on.

**Required**

[`var artistName: String?`](/documentation/musickit/librarysongsortproperties/artistname)

The artist’s name.

**Required**

[`var composerName: String?`](/documentation/musickit/librarysongsortproperties/composername)

The name of the song’s composer.

**Required**

[`var discNumber: Int?`](/documentation/musickit/librarysongsortproperties/discnumber)

The disc number of the song.

**Required**

[`var duration: TimeInterval?`](/documentation/musickit/librarysongsortproperties/duration)

The duration of the song.

**Required**

[`var lastPlayedDate: Date?`](/documentation/musickit/librarysongsortproperties/lastplayeddate)

The date when the user last played the song on this device.

**Required**

[`var libraryAddedDate: Date?`](/documentation/musickit/librarysongsortproperties/libraryaddeddate)

The date when the user added the song to the library.

**Required**

[`var playCount: Int?`](/documentation/musickit/librarysongsortproperties/playcount)

The number of times the user played the song.

**Required**

[`var title: String`](/documentation/musickit/librarysongsortproperties/title)

The title of the song.

**Required**

[`var trackNumber: Int?`](/documentation/musickit/librarysongsortproperties/tracknumber)

The song’s number in the album’s track list.

**Required**
