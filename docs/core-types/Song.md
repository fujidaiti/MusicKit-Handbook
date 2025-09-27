# Song

> Source: https://developer.apple.com/documentation/musickit/song

```swift
struct Song
```

A music item that represents a song.

## Properties

### Instance Properties

#### `var albumTitle: String?`

The title of the album the song appears on.

#### `var albums: MusicItemCollection<Album>?`

The song's associated albums.

#### `var artistName: String`

The artist's name.

#### `var artistURL: URL?`

The artist's URL.

#### `var artists: MusicItemCollection<Artist>?`

The song's associated artists.

#### `var artwork: Artwork?`

The artwork for the song.

#### `var attribution: String?`

For classical music only, the name of the artist or composer to attribute to the song.

#### `var audioVariants: [AudioVariant]?`

The variants that indicate the quality of audio available for the song.

#### `var composerName: String?`

The name of the song's composer.

#### `var composers: MusicItemCollection<Artist>?`

The song's composers.

#### `var contentRating: ContentRating?`

The rating of the content.

**Discussion**

A nil value means no rating is available for this song.

#### `var discNumber: Int?`

The number of the disc the song appears on.

#### `var duration: TimeInterval?`

The duration of the song.

#### `var editorialNotes: EditorialNotes?`

The editorial notes for the song.

#### `var genreNames: [String]`

The names of the song's associated genres.

#### `var genres: MusicItemCollection<Genre>?`

The song's associated genres.

#### `var hasLyrics: Bool`

A Boolean value that indicates whether the song has lyrics available in the catalog. If true, the song has lyrics available; otherwise, it doesn't.

#### `let id: MusicItemID`

The unique identifier for the song.

#### `var isAppleDigitalMaster: Bool?`

A Boolean value that indicates whether the song is an Apple Digital Master.

**Discussion**

Apple Digital Masters start from 24-bit files and are optimized to bring the best-sounding audio to Apple products.

#### `var isrc: String?`

The International Standard Recording Code (ISRC) for the song.

#### `var lastPlayedDate: Date?`

The date when the user last played the song on this device.

#### `var libraryAddedDate: Date?`

The date when the user added the song to the library.

#### `var movementCount: Int?`

For classical music only, the movement count of this song.

#### `var movementName: String?`

For classical music only, the movement name of this song.

#### `var movementNumber: Int?`

For classical music only, the movement number of this song.

#### `var musicVideos: MusicItemCollection<MusicVideo>?`

The song's associated music videos.

#### `var playCount: Int?`

The number of times the user played the song.

#### `var playParameters: PlayParameters?`

The parameters to use to play the song.

#### `var previewAssets: [PreviewAsset]?`

The preview assets for the song.

#### `var releaseDate: Date?`

The release date (or expected prerelease date) for the song.

#### `var station: Station?`

The song's associated station.

#### `var title: String`

The title of the song.

#### `var trackNumber: Int?`

The song's number in the album's track list.

#### `var url: URL?`

The URL for the song.

#### `var workName: String?`

For classical music only, the name of the associated work.

## Relationships

### Conforms To

- [`FilterableMusicItem`](../protocols/FilterProtocols.md#filterablemusicitem)
- [`MusicCatalogChartRequestable`](../protocols/RequestProtocols.md#musiccatalogchartrequestable)
- [`MusicCatalogSearchable`](../protocols/RequestProtocols.md#musiccatalogsearchable)
- [`MusicItem`](../protocols/UtilityProtocols.md#musicitem)
- [`MusicLibraryAddable`](../protocols/PlaybackProtocols.md#musiclibraryaddable)
- [`MusicLibraryRequestable`](../protocols/RequestProtocols.md#musiclibraryrequestable)
- [`MusicLibrarySearchable`](../protocols/RequestProtocols.md#musiclibrarysearchable)
- [`MusicPlaylistAddable`](../protocols/PlaybackProtocols.md#musicplaylistaddable)
- [`MusicPropertyContainer`](../protocols/UtilityProtocols.md#musicpropertycontainer)
- [`MusicRecentlyPlayedRequestable`](../protocols/RequestProtocols.md#musicrecentlyplayedrequestable)
- [`PlayableMusicItem`](../protocols/PlaybackProtocols.md#playablemusicitem)

## See Also

### Music Items

- [`struct Album`](Album.md) - A music item that represents an album.
- [`struct Artist`](Artist.md) - A music item that represents an artist.
- [`struct Curator`](Curator.md) - A music item that represents a curator.
- [`struct Genre`](Genre.md) - A music item that represents a genre.
- [`struct MusicVideo`](MusicVideo.md) - A music item that represents a music video.
- [`struct Playlist`](Playlist.md) - A music item that represents a playlist.
- [`struct RadioShow`](RadioShow.md) - A music item that represents a radio show.
- [`struct RecordLabel`](RecordLabel.md) - A music item that represents a record label.
- [`struct Station`](Station.md) - A music item that represents a station.
- [`enum Track`](Track.md) - A music item that represents a track.