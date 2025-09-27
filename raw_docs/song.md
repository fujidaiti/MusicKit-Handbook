# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/song

- [MusicKit](/documentation/musickit)
- Song

Structure

# Song

A music item that represents a song.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct Song
```

## [Topics](/documentation/musickit/song#topics)

### [Instance Properties](/documentation/musickit/song#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/song/albumtitle)

The title of the album the song appears on.

[`var albums: MusicItemCollection<Album>?`](/documentation/musickit/song/albums)

The song’s associated albums.

[`var artistName: String`](/documentation/musickit/song/artistname)

The artist’s name.

[`var artistURL: URL?`](/documentation/musickit/song/artisturl)

The artist’s URL.

[`var artists: MusicItemCollection<Artist>?`](/documentation/musickit/song/artists)

The song’s associated artists.

[`var artwork: Artwork?`](/documentation/musickit/song/artwork)

The artwork for the song.

[`var attribution: String?`](/documentation/musickit/song/attribution)

For classical music only, the name of the artist or composer to attribute to the song.

[`var audioVariants: [AudioVariant]?`](/documentation/musickit/song/audiovariants)

The variants that indicate the quality of audio available for the song.

[`var composerName: String?`](/documentation/musickit/song/composername)

The name of the song’s composer.

[`var composers: MusicItemCollection<Artist>?`](/documentation/musickit/song/composers)

The song’s composers.

[`var contentRating: ContentRating?`](/documentation/musickit/song/contentrating)

The rating of the content.

[`var discNumber: Int?`](/documentation/musickit/song/discnumber)

The number of the disc the song appears on.

[`var duration: TimeInterval?`](/documentation/musickit/song/duration)

The duration of the song.

[`var editorialNotes: EditorialNotes?`](/documentation/musickit/song/editorialnotes)

The editorial notes for the song.

[`var genreNames: [String]`](/documentation/musickit/song/genrenames)

The names of the song’s associated genres.

[`var genres: MusicItemCollection<Genre>?`](/documentation/musickit/song/genres)

The song’s associated genres.

[`var hasLyrics: Bool`](/documentation/musickit/song/haslyrics)

A Boolean value that indicates whether the song has lyrics available in the catalog. If true, the song has lyrics available; otherwise, it doesn’t.

[`let id: MusicItemID`](/documentation/musickit/song/id)

The unique identifier for the song.

[`var isAppleDigitalMaster: Bool?`](/documentation/musickit/song/isappledigitalmaster)

A Boolean value that indicates whether the song is an Apple Digital Master.

[`var isrc: String?`](/documentation/musickit/song/isrc)

The International Standard Recording Code (ISRC) for the song.

[`var lastPlayedDate: Date?`](/documentation/musickit/song/lastplayeddate)

The date when the user last played the song on this device.

[`var libraryAddedDate: Date?`](/documentation/musickit/song/libraryaddeddate)

The date when the user added the song to the library.

[`var movementCount: Int?`](/documentation/musickit/song/movementcount)

For classical music only, the movement count of this song.

[`var movementName: String?`](/documentation/musickit/song/movementname)

For classical music only, the movement name of this song.

[`var movementNumber: Int?`](/documentation/musickit/song/movementnumber)

For classical music only, the movement number of this song.

[`var musicVideos: MusicItemCollection<MusicVideo>?`](/documentation/musickit/song/musicvideos)

The song’s associated music videos.

[`var playCount: Int?`](/documentation/musickit/song/playcount)

The number of times the user played the song.

[`var playParameters: PlayParameters?`](/documentation/musickit/song/playparameters)

The parameters to use to play the song.

[`var previewAssets: [PreviewAsset]?`](/documentation/musickit/song/previewassets)

The preview assets for the song.

[`var releaseDate: Date?`](/documentation/musickit/song/releasedate)

The release date (or expected prerelease date) for the song.

[`var station: Station?`](/documentation/musickit/song/station)

The song’s associated station.

[`var title: String`](/documentation/musickit/song/title)

The title of the song.

[`var trackNumber: Int?`](/documentation/musickit/song/tracknumber)

The song’s number in the album’s track list.

[`var url: URL?`](/documentation/musickit/song/url)

The URL for the song.

[`var workName: String?`](/documentation/musickit/song/workname)

For classical music only, the name of the associated work.

### [Default Implementations](/documentation/musickit/song#Default-Implementations)

[API Reference

FilterableMusicItem Implementations](/documentation/musickit/song/filterablemusicitem-implementations)

[API Reference

MusicLibraryRequestable Implementations](/documentation/musickit/song/musiclibraryrequestable-implementations)

## [Relationships](/documentation/musickit/song#relationships)

### [Conforms To](/documentation/musickit/song#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`FilterableMusicItem`](/documentation/musickit/filterablemusicitem)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`MusicCatalogChartRequestable`](/documentation/musickit/musiccatalogchartrequestable)
- [`MusicCatalogSearchable`](/documentation/musickit/musiccatalogsearchable)
- [`MusicItem`](/documentation/musickit/musicitem)
- [`MusicLibraryAddable`](/documentation/musickit/musiclibraryaddable)
- [`MusicLibraryRequestable`](/documentation/musickit/musiclibraryrequestable)
- [`MusicLibrarySearchable`](/documentation/musickit/musiclibrarysearchable)
- [`MusicPlaylistAddable`](/documentation/musickit/musicplaylistaddable)
- [`MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)
- [`MusicRecentlyPlayedRequestable`](/documentation/musickit/musicrecentlyplayedrequestable)
- [`PlayableMusicItem`](/documentation/musickit/playablemusicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/song#see-also)

### [Music Items](/documentation/musickit/song#Music-Items)

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

[`struct Station`](/documentation/musickit/station)

A music item that represents a station.

[`enum Track`](/documentation/musickit/track)

A music item that represents a track.
