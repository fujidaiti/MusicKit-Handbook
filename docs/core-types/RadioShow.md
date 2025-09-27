# RadioShow

> Source: https://developer.apple.com/documentation/musickit/radioshow

```swift
struct RadioShow
```

A music item that represents a radio show.

## Properties

### Instance Properties

```swift
var artwork: Artwork? { get }
```
The radio show artwork.

```swift
var editorialNotes: EditorialNotes? { get }
```
The notes about the radio show that appear in the Music catalog.

```swift
var hostName: String? { get }
```
The name of the host for the radio show.

```swift
let id: MusicItemID
```
The unique identifier for the radio show.

```swift
var name: String { get }
```
The name of the radio show.

```swift
var playlists: MusicItemCollection<Playlist>? { get }
```
The radio show's associated playlists.

```swift
var url: URL? { get }
```
The URL for the radio show.

## Relationships

### Conforms To

- [`FilterableMusicItem`](../protocols/FilterProtocols.md#filterablemusicitem)
- [`MusicCatalogSearchable`](../protocols/RequestProtocols.md#musiccatalogsearchable)
- [`MusicItem`](../protocols/UtilityProtocols.md#musicitem)
- [`MusicPropertyContainer`](../protocols/UtilityProtocols.md#musicpropertycontainer)

## See Also

### Music Items

[`struct Album`](Album.md) - A music item that represents an album.

[`struct Artist`](Artist.md) - A music item that represents an artist.

[`struct Curator`](Curator.md) - A music item that represents a curator.

[`struct Genre`](Genre.md) - A music item that represents a genre.

[`struct MusicVideo`](MusicVideo.md) - A music item that represents a music video.

[`struct Playlist`](Playlist.md) - A music item that represents a playlist.

[`struct RecordLabel`](RecordLabel.md) - A music item that represents a record label.

[`struct Song`](Song.md) - A music item that represents a song.

[`struct Station`](Station.md) - A music item that represents a station.

[`enum Track`](Track.md) - A music item that represents a track.