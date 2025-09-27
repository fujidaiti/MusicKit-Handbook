# MusicVideo

> Source: https://developer.apple.com/documentation/musickit/musicvideo

```swift
struct MusicVideo
```

A music item that represents a music video.

## Properties

### Instance Properties

#### `var albumTitle: String?`
The title of the album the music video appears on.

#### `var albums: MusicItemCollection<Album>?`
The music video's associated albums.

#### `var artistName: String`
The artist's name.

#### `var artistURL: URL?`
The artist's URL.

#### `var artists: MusicItemCollection<Artist>?`
The music video's associated artists.

#### `var artwork: Artwork?`
The artwork for the music video.

#### `var contentRating: ContentRating?`
The rating of the content.

#### `var duration: TimeInterval?`
The duration of the music video.

#### `var editorialNotes: EditorialNotes?`
The editorial notes for the music video.

#### `var genreNames: [String]`
The names of the music video's associated genres.

#### `var genres: MusicItemCollection<Genre>?`
The music video's associated genres.

#### `var has4K: Bool?`
A Boolean value that indicates whether the music video has 4K content.

#### `var hasHDR: Bool?`
A Boolean value that indicates whether the music video has HDR10-encoded content.

#### `let id: MusicItemID`
The unique identifier for the music video.

#### `var isPreview: Bool`
A Boolean value that indicates whether this content corresponds to a subscription video preview.

#### `var isrc: String?`
The International Standard Recording Code (ISRC) for the music video.

#### `var lastPlayedDate: Date?`
The date when the user last played the music video on this device.

#### `var libraryAddedDate: Date?`
The date when the user added the music video to the library.

#### `var moreByArtist: MusicItemCollection<MusicVideo>?`
A collection of additional music videos by the artist.

#### `var moreInGenre: MusicItemCollection<MusicVideo>?`
A collection of music videos in the same genre as this music video.

#### `var playCount: Int?`
The number of times the user played the music video.

#### `var playParameters: PlayParameters?`
The parameters to use to play the music video.

#### `var previewAssets: [PreviewAsset]?`
The preview assets for the music video.

#### `var releaseDate: Date?`
The release date (or expected prerelease date) for the music video.

#### `var songs: MusicItemCollection<Song>?`
The music video's associated songs.

#### `var title: String`
The title of the music video.

#### `var trackNumber: Int?`
The music video's number in the album's track list.

#### `var url: URL?`
The URL for the music video.

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

## See Also

### Music Items

[`struct Album`](Album.md) - A music item that represents an album.

[`struct Artist`](Artist.md) - A music item that represents an artist.

[`struct Curator`](Curator.md) - A music item that represents a curator.

[`struct Genre`](Genre.md) - A music item that represents a genre.

[`struct Playlist`](Playlist.md) - A music item that represents a playlist.

[`struct RadioShow`](RadioShow.md) - A music item that represents a radio show.

[`struct RecordLabel`](RecordLabel.md) - A music item that represents a record label.

[`struct Song`](Song.md) - A music item that represents a song.

[`struct Station`](Station.md) - A music item that represents a station.

[`enum Track`](Track.md) - A music item that represents a track.