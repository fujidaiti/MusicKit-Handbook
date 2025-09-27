# Sort Protocols

> Source: Multiple Apple MusicKit documentation pages

These protocols define the properties that your app can use to sort results for various types of library requests in MusicKit. Each protocol provides specific sorting criteria for different music item types.

## Overview

The sort protocols enable developers to specify sorting criteria when making library requests for different types of music content. These protocols define the available properties that can be used to order results, such as title, artist name, date added to library, play count, and other relevant metadata.

## Protocols

### LibraryAlbumSortProperties
- **Swift Declaration**: `protocol LibraryAlbumSortProperties`
- **Purpose**: Album properties your app uses to sort results for a library request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/libraryalbumsortproperties)
- **Properties**:
  - `var artistName: String` - The artist's name (Required)
  - `var lastPlayedDate: Date?` - The date when the user last played the album on this device (Required)
  - `var libraryAddedDate: Date?` - The date when the user added the album to the library (Required)
  - `var releaseDate: Date?` - The release date (or expected prerelease date) for the album (Required)
  - `var title: String` - The title of the album (Required)
  - `var trackCount: Int` - The number of tracks for the album (Required)

### LibraryArtistSortProperties
- **Swift Declaration**: `protocol LibraryArtistSortProperties`
- **Purpose**: Artist properties your app uses to sort results for a library request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/libraryartistsortproperties)
- **Properties**:
  - `var albumCount: Int?` - The number of albums from this artist (Required)
  - `var libraryAddedDate: Date?` - The date when the user added the artist to the library (Required)
  - `var name: String` - The name of the artist (Required)

### LibraryGenreSortProperties
- **Swift Declaration**: `protocol LibraryGenreSortProperties`
- **Purpose**: Genre properties your app uses to sort results for a library request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/librarygenresortproperties)
- **Properties**:
  - `var libraryAddedDate: Date?` - The date when the user added the genre to the library (Required)
  - `var name: String` - The localized name of the genre (Required)

### LibraryMusicVideoSortProperties
- **Swift Declaration**: `protocol LibraryMusicVideoSortProperties`
- **Purpose**: Music video properties your app uses to sort results for a library request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/librarymusicvideosortproperties)
- **Properties**:
  - `var albumTitle: String?` - The title of the album the music video appears on (Required)
  - `var artistName: String?` - The artist's name (Required)
  - `var duration: TimeInterval?` - The duration of the music video (Required)
  - `var lastPlayedDate: Date?` - The date when the user last played the music video on this device (Required)
  - `var libraryAddedDate: Date?` - The date when the user added the music video to the library (Required)
  - `var playCount: Int?` - The number of times the user played the music video (Required)
  - `var title: String` - The title of the music video (Required)
  - `var trackNumber: Int?` - The music video's number in the album's track list (Required)

### LibraryPlaylistEntrySortProperties
- **Swift Declaration**: `protocol LibraryPlaylistEntrySortProperties`
- **Purpose**: Playlist entry properties your app uses to sort results for a library request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/libraryplaylistentrysortproperties)
- **Properties**: Documentation does not specify individual properties for this protocol.

### LibraryPlaylistSortProperties
- **Swift Declaration**: `protocol LibraryPlaylistSortProperties`
- **Purpose**: Playlist properties your app uses to sort results for a library request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/libraryplaylistsortproperties)
- **Properties**:
  - `var lastPlayedDate: Date?` - The date when the user last played the playlist on this device (Required)
  - `var libraryAddedDate: Date?` - The date when the user added the playlist to the library (Required)
  - `var name: String` - The name of the playlist (Required)

### LibrarySongSortProperties
- **Swift Declaration**: `protocol LibrarySongSortProperties`
- **Purpose**: Song properties your app uses to sort results for a library request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/librarysongsortproperties)
- **Properties**:
  - `var albumTitle: String?` - The title of the album the song appears on (Required)
  - `var artistName: String?` - The artist's name (Required)
  - `var composerName: String?` - The name of the song's composer (Required)
  - `var discNumber: Int?` - The disc number of the song (Required)
  - `var duration: TimeInterval?` - The duration of the song (Required)
  - `var lastPlayedDate: Date?` - The date when the user last played the song on this device (Required)
  - `var libraryAddedDate: Date?` - The date when the user added the song to the library (Required)
  - `var playCount: Int?` - The number of times the user played the song (Required)
  - `var title: String` - The title of the song (Required)
  - `var trackNumber: Int?` - The song's number in the album's track list (Required)

### LibraryTrackSortProperties
- **Swift Declaration**: `protocol LibraryTrackSortProperties`
- **Purpose**: Track properties your app uses to sort results for a library request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/librarytracksortproperties)
- **Properties**:
  - `var albumTitle: String?` - The title of the album the track appears on (Required)
  - `var artistName: String?` - The artist's name (Required)
  - `var discNumber: Int?` - The disc number of the track (Required)
  - `var duration: TimeInterval?` - The duration of the track (Required)
  - `var lastPlayedDate: Date?` - The date when the user last played the track on this device (Required)
  - `var libraryAddedDate: Date?` - The date when the user added the track to the library (Required)
  - `var playCount: Int?` - The number of times the user played the track (Required)
  - `var title: String` - The title of the track (Required)
  - `var trackNumber: Int?` - The track's number in the album's track list (Required)