# Curator

> Source: https://developer.apple.com/documentation/musickit/curator

```swift
struct Curator
```

A music item that represents a curator.

## Properties

### Instance Properties

```swift
var artwork: Artwork? { get }
```
The curator artwork.

```swift
var editorialNotes: EditorialNotes? { get }
```
The notes about the curator that appear in the Music catalog.

```swift
let id: MusicItemID
```
The unique identifier for the curator.

```swift
var kind: Curator.Kind { get }
```
The kind of curator.

```swift
var name: String { get }
```
The name of the curator.

```swift
var playlists: MusicItemCollection<Playlist>? { get }
```
The curator's associated playlists.

```swift
var url: URL? { get }
```
The URL for the curator.

### Enumerations

```swift
enum Kind
```
The available kinds of curators.

#### Enumeration Cases

```swift
case editorial
```
Indicates that the curator is an Apple Music curator.

```swift
case external
```
Indicates that the curator is an external, third-party curator.

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

[`struct Genre`](Genre.md) - A music item that represents a genre.

[`struct MusicVideo`](MusicVideo.md) - A music item that represents a music video.

[`struct Playlist`](Playlist.md) - A music item that represents a playlist.

[`struct RadioShow`](RadioShow.md) - A music item that represents a radio show.

[`struct RecordLabel`](RecordLabel.md) - A music item that represents a record label.

[`struct Song`](Song.md) - A music item that represents a song.

[`struct Station`](Station.md) - A music item that represents a station.

[`enum Track`](Track.md) - A music item that represents a track.