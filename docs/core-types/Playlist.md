# Playlist

> Source: https://developer.apple.com/documentation/musickit/playlist

```swift
struct Playlist
```

A music item that represents a playlist.

## Structures

### `struct Entry`

A music item that represents a playlist entry.

## Enumerations

### `enum Kind`

The available kinds of playlists.

```swift
enum Kind
```

#### Enumeration Cases

- `case editorial` - Indicates that the playlist was created by an Apple Music curator.
- `case external` - Indicates that the playlist was created by an external curator.
- `case personalMix` - Indicates that the playlist is a personalized playlist for an Apple Music user.
- `case replay` - Indicates that the playlist is a personalized Replay playlist for an Apple Music user.
- `case userShared` - Indicates that the playlist was created and shared by an Apple Music user.

## Properties

### Instance Properties

#### `var artwork: Artwork?`

The artwork for the playlist.

#### `var curator: Curator?`

The playlist's associated curator.

#### `var curatorName: String?`

The display name for the playlist's curator.

#### `var entries: MusicItemCollection<Playlist.Entry>?`

The entries in the playlist

#### `var featuredArtists: MusicItemCollection<Artist>?`

A collection of featured artists for this playlist.

#### `let id: MusicItemID`

The unique identifier for the playlist.

#### `var isChart: Bool?`

A Boolean value that indicates whether the playlist represents a popularity chart.

#### `var kind: Playlist.Kind?`

The kind of playlist.

#### `var lastModifiedDate: Date?`

The playlist's most recent modification date.

#### `var lastPlayedDate: Date?`

The date when the user last played the playlist on this device.

#### `var libraryAddedDate: Date?`

The date when the user added the playlist to the library.

#### `var moreByCurator: MusicItemCollection<Playlist>?`

A collection of additional playlists by the same curator.

#### `var name: String`

The name of the playlist.

#### `var playParameters: PlayParameters?`

The parameters to use to play the tracks in the playlist.

#### `var radioShow: RadioShow?`

The playlist's associated radio show.

#### `var shortDescription: String?`

An abbreviated description to show inline or when the playlist appears alongside other content.

#### `var standardDescription: String?`

A description to show when the playlist is prominently displayed.

#### `var tracks: MusicItemCollection<Track>?`

The tracks in the playlist.

#### `var url: URL?`

The URL for the playlist.

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

- [`struct Album`](Album.md) - A music item that represents an album.
- [`struct Artist`](Artist.md) - A music item that represents an artist.
- [`struct Curator`](Curator.md) - A music item that represents a curator.
- [`struct Genre`](Genre.md) - A music item that represents a genre.
- [`struct MusicVideo`](MusicVideo.md) - A music item that represents a music video.
- [`struct RadioShow`](RadioShow.md) - A music item that represents a radio show.
- [`struct RecordLabel`](RecordLabel.md) - A music item that represents a record label.
- [`struct Song`](Song.md) - A music item that represents a song.
- [`struct Station`](Station.md) - A music item that represents a station.
- [`enum Track`](Track.md) - A music item that represents a track.