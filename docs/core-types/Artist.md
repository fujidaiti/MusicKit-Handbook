# Artist

> Source: https://developer.apple.com/documentation/musickit/artist

```swift
struct Artist
```

A music item that represents an artist.

## Properties

### Instance Properties

#### `var albums: MusicItemCollection<Album>? { get }`

The artist's associated albums.

#### `var appearsOnAlbums: MusicItemCollection<Album>? { get }`

A collection of albums from other artists that this artist appears on.

#### `var artwork: Artwork? { get }`

The artist artwork.

#### `var compilationAlbums: MusicItemCollection<Album>? { get }`

A collection of compilation albums that include tracks by the artist.

#### `var editorialNotes: EditorialNotes? { get }`

The notes about the artist that appear in the Music catalog.

#### `var featuredAlbums: MusicItemCollection<Album>? { get }`

A collection of featured albums of the artist.

#### `var featuredPlaylists: MusicItemCollection<Playlist>? { get }`

A collection of the artist's associated playlists.

#### `var fullAlbums: MusicItemCollection<Album>? { get }`

A collection of the artist's full-release albums.

#### `var genreNames: [String]? { get }`

The names of this artist's associated genres.

#### `var genres: MusicItemCollection<Genre>? { get }`

The artist's associated genres.

#### `let id: MusicItemID`

The unique identifier for the artist.

#### `var latestRelease: Album? { get }`

The artist's most recent album.

#### `var libraryAddedDate: Date? { get }`

The date when the user added the artist to the library.

#### `var liveAlbums: MusicItemCollection<Album>? { get }`

A collection of the artist's live albums.

#### `var musicVideos: MusicItemCollection<MusicVideo>? { get }`

The artist's associated music videos.

#### `var name: String { get }`

The name of the artist.

#### `var playlists: MusicItemCollection<Playlist>? { get }`

The artist's associated playlists.

#### `var similarArtists: MusicItemCollection<Artist>? { get }`

A collection of artists similar to this artist.

#### `var singles: MusicItemCollection<Album>? { get }`

A collection of the artist's associated albums in the *singles* category.

#### `var station: Station? { get }`

The artist's associated station.

#### `var topMusicVideos: MusicItemCollection<MusicVideo>? { get }`

A collection of the artist's top music videos.

#### `var topSongs: MusicItemCollection<Song>? { get }`

A collection of the artist's top songs.

#### `var url: URL? { get }`

The URL for the artist.

### Type Aliases

#### `typealias FilterType = ArtistFilter`

The associated type that contains the artist properties your app uses as a filter for a catalog resource request.

#### `typealias LibraryFilter = LibraryArtistFilter`

The associated type that contains the artist properties your app uses for a library request.

#### `typealias LibrarySortProperties = LibraryArtistSortProperties`

The associated type that contains the set of artist properties your app uses to sort results for a library request.

## Relationships

### Conforms To

- [`FilterableMusicItem`](../protocols/FilterProtocols.md#filterablemusicitem)
- [`MusicCatalogSearchable`](../protocols/RequestProtocols.md#musiccatalogsearchable)
- [`MusicItem`](../protocols/UtilityProtocols.md#musicitem)
- [`MusicLibraryRequestable`](../protocols/RequestProtocols.md#musiclibraryrequestable)
- [`MusicLibrarySearchable`](../protocols/RequestProtocols.md#musiclibrarysearchable)
- [`MusicLibrarySectionRequestable`](../protocols/RequestProtocols.md#musiclibrarysectionrequestable)
- [`MusicPropertyContainer`](../protocols/UtilityProtocols.md#musicpropertycontainer)

## See Also

### Music Items

[`struct Album`](Album.md) - A music item that represents an album.

[`struct Curator`](Curator.md) - A music item that represents a curator.

[`struct Genre`](Genre.md) - A music item that represents a genre.

[`struct MusicVideo`](MusicVideo.md) - A music item that represents a music video.

[`struct Playlist`](Playlist.md) - A music item that represents a playlist.

[`struct RadioShow`](RadioShow.md) - A music item that represents a radio show.

[`struct RecordLabel`](RecordLabel.md) - A music item that represents a record label.

[`struct Song`](Song.md) - A music item that represents a song.

[`struct Station`](Station.md) - A music item that represents a station.

[`enum Track`](Track.md) - A music item that represents a track.