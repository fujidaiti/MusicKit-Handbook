# Station

> Source: https://developer.apple.com/documentation/musickit/station

```swift
struct Station
```

A music item that represents a station.

## Properties

### Instance Properties

#### `var artwork: Artwork?`
The station artwork.

#### `var contentRating: ContentRating?`
The rating of the content that potentially plays while playing the station.

#### `var duration: TimeInterval?`
The duration of the stream.

#### `var editorialNotes: EditorialNotes?`
The notes about the station that appear in the Music app.

#### `var episodeNumber: Int?`
The episode number of the station.

#### `let id: MusicItemID`
The unique identifier for the station.

#### `var isLive: Bool`
A Boolean value that indicates whether the station is live.

#### `var name: String`
The name of the station.

#### `var playParameters: PlayParameters?`
The parameters to use to play the station.

#### `var stationProviderName: String?`
The name of the entity that provides the station.

#### `var url: URL?`
The URL for the station.

## Relationships

### Conforms To

- [`FilterableMusicItem`](../protocols/FilterProtocols.md#filterablemusicitem)
- [`MusicCatalogSearchable`](../protocols/RequestProtocols.md#musiccatalogsearchable)
- [`MusicItem`](../protocols/UtilityProtocols.md#musicitem)
- [`MusicPersonalRecommendationItem`](../protocols/RequestProtocols.md#musicpersonalrecommendationitem)
- [`MusicPropertyContainer`](../protocols/UtilityProtocols.md#musicpropertycontainer)
- [`MusicRecentlyPlayedRequestable`](../protocols/RequestProtocols.md#musicrecentlyplayedrequestable)
- [`PlayableMusicItem`](../protocols/PlaybackProtocols.md#playablemusicitem)

## See Also

### Music Items

[`struct Album`](Album.md) - A music item that represents an album.

[`struct Artist`](Artist.md) - A music item that represents an artist.

[`struct Curator`](Curator.md) - A music item that represents a curator.

[`struct Genre`](Genre.md) - A music item that represents a genre.

[`struct MusicVideo`](MusicVideo.md) - A music item that represents a music video.

[`struct Playlist`](Playlist.md) - A music item that represents a playlist.

[`struct RadioShow`](RadioShow.md) - A music item that represents a radio show.

[`struct RecordLabel`](RecordLabel.md) - A music item that represents a record label.

[`struct Song`](Song.md) - A music item that represents a song.

[`enum Track`](Track.md) - A music item that represents a track.