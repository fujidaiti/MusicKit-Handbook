# Album

> Source: https://developer.apple.com/documentation/musickit/album

```swift
struct Album
```

A music item that represents an album.

## Properties

### Instance Properties

#### `var appearsOn: MusicItemCollection<Playlist>? { get }`

A collection of playlists that include tracks from the album.

#### `var artistName: String { get }`

The artist's name.

**Discussion**

You can find more precise information about this album's artists in the `artists` relationship, which, unlike `artistName`, requires that you load it explicitly using the `with(_:)` method, as in the following example:

```swift
let detailedAlbum = try await album.with([.artists])
let firstArtist = album.artists?.first
```

#### `var artistURL: URL? { get }`

The artist's URL.

#### `var artists: MusicItemCollection<Artist>? { get }`

The album's associated artists.

#### `var artwork: Artwork? { get }`

The album artwork.

#### `var audioVariants: [AudioVariant]? { get }`

The variants that indicate the quality of audio available for the album.

#### `var contentRating: ContentRating? { get }`

The rating of the content.

**Discussion**

A nil value means no rating is available for this album.

#### `var copyright: String? { get }`

The copyright text for the album.

#### `var editorialNotes: EditorialNotes? { get }`

The notes about the album that appear in the Music app.

#### `var genreNames: [String] { get }`

The names of the album's associated genres.

#### `var genres: MusicItemCollection<Genre>? { get }`

The genres for the album.

#### `let id: MusicItemID`

The unique identifier for the album.

#### `var isAppleDigitalMaster: Bool? { get }`

A Boolean value that indicates whether the album is an Apple Digital Master.

**Discussion**

Apple Digital Masters start from 24-bit files and are optimized to bring the best-sounding audio to Apple products.

#### `var isCompilation: Bool? { get }`

A Boolean value that indicates whether the album is a compilation.

#### `var isComplete: Bool? { get }`

A Boolean value that indicates whether the album is complete.

**Discussion**

If true, the album is complete; otherwise, it's incomplete. An album is complete if it contains all its tracks and songs.

#### `var isSingle: Bool? { get }`

A Boolean value that indicates whether the album consists of a single song.

#### `var lastPlayedDate: Date? { get }`

The date when the user last played the album on this device.

#### `var libraryAddedDate: Date? { get }`

The date when the user added the album to the library.

#### `var otherVersions: MusicItemCollection<Album>? { get }`

A collection of other versions of the album.

#### `var playParameters: PlayParameters? { get }`

The parameters to use to play the tracks of the album.

#### `var recordLabelName: String? { get }`

The name of the album's record label.

#### `var recordLabels: MusicItemCollection<RecordLabel>? { get }`

The record labels for the album.

#### `var relatedAlbums: MusicItemCollection<Album>? { get }`

A collection of related albums.

#### `var relatedVideos: MusicItemCollection<MusicVideo>? { get }`

A collection of the album's music videos.

#### `var releaseDate: Date? { get }`

The release date (or expected prerelease date) for the album.

#### `var title: String { get }`

The title of the album.

#### `var trackCount: Int { get }`

The number of tracks for the album.

#### `var tracks: MusicItemCollection<Track>? { get }`

The tracks on the album.

#### `var upc: String? { get }`

The universal product code (UPC) for the album.

#### `var url: URL? { get }`

The URL for the album.

### Type Aliases

#### `typealias FilterType = AlbumFilter`

The associated type that contains the album properties your app uses as a filter for a catalog resource request.

#### `typealias LibraryFilter = LibraryAlbumFilter`

The associated type that contains the album properties your app uses for a library request.

#### `typealias LibrarySortProperties = LibraryAlbumSortProperties`

The associated type that contains the set of album properties your app uses to sort results for a library request.

## Relationships

### Conforms To

- [`FilterableMusicItem`](../protocols/FilterProtocols.md#filterablemusicitem)
- [`MusicCatalogChartRequestable`](../protocols/RequestProtocols.md#musiccatalogchartrequestable)
- [`MusicCatalogSearchable`](../protocols/RequestProtocols.md#musiccatalogsearchable)
- [`MusicItem`](../protocols/UtilityProtocols.md#musicitem)
- [`MusicLibraryAddable`](../protocols/PlaybackProtocols.md#musiclibraryaddable)
- [`MusicLibraryRequestable`](../protocols/RequestProtocols.md#musiclibraryrequestable)
- [`MusicLibrarySearchable`](../protocols/RequestProtocols.md#musiclibrarysearchable)
- [`MusicLibrarySectionRequestable`](../protocols/RequestProtocols.md#musiclibrarysectionrequestable)
- [`MusicPersonalRecommendationItem`](../protocols/RequestProtocols.md#musicpersonalrecommendationitem)
- [`MusicPlaylistAddable`](../protocols/PlaybackProtocols.md#musicplaylistaddable)
- [`MusicPropertyContainer`](../protocols/UtilityProtocols.md#musicpropertycontainer)
- [`PlayableMusicItem`](../protocols/PlaybackProtocols.md#playablemusicitem)

## See Also

### Music Items

[`struct Artist`](Artist.md) - A music item that represents an artist.

[`struct Curator`](Curator.md) - A music item that represents a curator.

[`struct Genre`](Genre.md) - A music item that represents a genre.

[`struct MusicVideo`](MusicVideo.md) - A music item that represents a music video.

[`struct Playlist`](Playlist.md) - A music item that represents a playlist.

[`struct RadioShow`](RadioShow.md) - A music item that represents a radio show.

[`struct RecordLabel`](RecordLabel.md) - A music item that represents a record label.

[`struct Song`](Song.md) - A music item that represents a song.

[`struct Station`](Station.md) - A music item that represents a station.

[`enum Track`](Track.md) - A music item that represents a track.