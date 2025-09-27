# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/libraryplaylistsortproperties

- [MusicKit](/documentation/musickit)
- LibraryPlaylistSortProperties

Protocol

# LibraryPlaylistSortProperties

Playlist properties your app uses to sort results for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibraryPlaylistSortProperties
```

## [Topics](/documentation/musickit/libraryplaylistsortproperties#topics)

### [Instance Properties](/documentation/musickit/libraryplaylistsortproperties#Instance-Properties)

[`var lastPlayedDate: Date?`](/documentation/musickit/libraryplaylistsortproperties/lastplayeddate)

The date when the user last played the playlist on this device.

**Required**

[`var libraryAddedDate: Date?`](/documentation/musickit/libraryplaylistsortproperties/libraryaddeddate)

The date when the user added the playlist to the library.

**Required**

[`var name: String`](/documentation/musickit/libraryplaylistsortproperties/name)

The name of the playlist.

**Required**
