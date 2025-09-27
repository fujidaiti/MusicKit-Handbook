# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/track

- [MusicKit](/documentation/musickit)
- Track

Enumeration

# Track

A music item that represents a track.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
enum Track
```

## [Topics](/documentation/musickit/track#topics)

### [Enumeration Cases](/documentation/musickit/track#Enumeration-Cases)

[`case musicVideo(MusicVideo)`](/documentation/musickit/track/musicvideo(_:))

A track that corresponds to a music video.

[`case song(Song)`](/documentation/musickit/track/song(_:))

A track that corresponds to a song.

### [Instance Properties](/documentation/musickit/track#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/track/albumtitle)

The title of the album the track appears on.

[`var albums: MusicItemCollection<Album>?`](/documentation/musickit/track/albums)

The track’s associated albums.

[`var artistName: String`](/documentation/musickit/track/artistname)

The artist’s name.

[`var artistURL: URL?`](/documentation/musickit/track/artisturl)

The artist’s URL.

[`var artists: MusicItemCollection<Artist>?`](/documentation/musickit/track/artists)

The track’s associated artists.

[`var artwork: Artwork?`](/documentation/musickit/track/artwork)

The artwork for the track.

[`var contentRating: ContentRating?`](/documentation/musickit/track/contentrating)

The rating of the content.

[`var discNumber: Int?`](/documentation/musickit/track/discnumber)

The disc number of the track.

[`var duration: TimeInterval?`](/documentation/musickit/track/duration)

The duration of the track.

[`var editorialNotes: EditorialNotes?`](/documentation/musickit/track/editorialnotes)

The editorial notes for the track.

[`var genreNames: [String]`](/documentation/musickit/track/genrenames)

The names of the track’s associated genres.

[`var genres: MusicItemCollection<Genre>?`](/documentation/musickit/track/genres)

The track’s associated genres.

[`var id: MusicItemID`](/documentation/musickit/track/id)

The unique identifier for the track.

[`var isrc: String?`](/documentation/musickit/track/isrc)

The International Standard Recording Code (ISRC) for the track.

[`var lastPlayedDate: Date?`](/documentation/musickit/track/lastplayeddate)

The date when the user last played the track on this device.

[`var libraryAddedDate: Date?`](/documentation/musickit/track/libraryaddeddate)

The date when the user added the track to the library.

[`var playCount: Int?`](/documentation/musickit/track/playcount)

The number of times the user played the track.

[`var playParameters: PlayParameters?`](/documentation/musickit/track/playparameters)

The parameters to use to play the track.

[`var previewAssets: [PreviewAsset]?`](/documentation/musickit/track/previewassets)

The preview assets for the track.

[`var releaseDate: Date?`](/documentation/musickit/track/releasedate)

The release date (or expected for pre-release) of the track.

[`var title: String`](/documentation/musickit/track/title)

The title of the track.

[`var trackNumber: Int?`](/documentation/musickit/track/tracknumber)

The track’s number in the album’s track list.

[`var url: URL?`](/documentation/musickit/track/url)

The URL for the track.

[`var workName: String?`](/documentation/musickit/track/workname)

For classical music only, the name of the associated work.

### [Default Implementations](/documentation/musickit/track#Default-Implementations)

[API Reference

MusicLibraryRequestable Implementations](/documentation/musickit/track/musiclibraryrequestable-implementations)

## [Relationships](/documentation/musickit/track#relationships)

### [Conforms To](/documentation/musickit/track#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`MusicItem`](/documentation/musickit/musicitem)
- [`MusicLibraryAddable`](/documentation/musickit/musiclibraryaddable)
- [`MusicLibraryRequestable`](/documentation/musickit/musiclibraryrequestable)
- [`MusicPlaylistAddable`](/documentation/musickit/musicplaylistaddable)
- [`MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)
- [`MusicRecentlyPlayedRequestable`](/documentation/musickit/musicrecentlyplayedrequestable)
- [`PlayableMusicItem`](/documentation/musickit/playablemusicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/track#see-also)

### [Music Items](/documentation/musickit/track#Music-Items)

[`struct Album`](/documentation/musickit/album)

A music item that represents an album.

[`struct Artist`](/documentation/musickit/artist)

A music item that represents an artist.

[`struct Curator`](/documentation/musickit/curator)

A music item that represents a curator.

[`struct Genre`](/documentation/musickit/genre)

A music item that represents a genre.

[`struct MusicVideo`](/documentation/musickit/musicvideo)

A music item that represents a music video.

[`struct Playlist`](/documentation/musickit/playlist)

A music item that represents a playlist.

[`struct RadioShow`](/documentation/musickit/radioshow)

A music item that represents a radio show.

[`struct RecordLabel`](/documentation/musickit/recordlabel)

A music item that represents a record label.

[`struct Song`](/documentation/musickit/song)

A music item that represents a song.

[`struct Station`](/documentation/musickit/station)

A music item that represents a station.
