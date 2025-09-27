# RecordLabel

> Source: https://developer.apple.com/documentation/musickit/recordlabel

```swift
struct RecordLabel
```

A music item that represents a record label.

## Properties

### Instance Properties

```swift
var artwork: Artwork? { get }
```
The record label's artwork.

```swift
let id: MusicItemID
```
The unique identifier for the record label.

```swift
var latestReleases: MusicItemCollection<Album>? { get }
```
A collection of the most recent releases for the record label.

```swift
var name: String { get }
```
The name of the record label.

```swift
var shortDescription: String? { get }
```
An abbreviated description to show inline or when the record label appears alongside other content.

```swift
var standardDescription: String? { get }
```
A description to show when the record label is prominently displayed.

```swift
var topReleases: MusicItemCollection<Album>? { get }
```
A collection of top releases for the record label.

```swift
var url: URL? { get }
```
The URL for the record label.

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

[`struct RadioShow`](RadioShow.md) - A music item that represents a radio show.

[`struct Song`](Song.md) - A music item that represents a song.

[`struct Station`](Station.md) - A music item that represents a station.

[`enum Track`](Track.md) - A music item that represents a track.