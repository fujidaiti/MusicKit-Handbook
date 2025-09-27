# Genre

> Source: https://developer.apple.com/documentation/musickit/genre

```swift
struct Genre
```

A music item that represents a genre.

## Properties

### Instance Properties

```swift
let id: MusicItemID
```
The unique identifier for the genre.

```swift
var libraryAddedDate: Date? { get }
```
The date when the user added the genre to the library.

```swift
var name: String { get }
```
The localized name of the genre.

```swift
var parent: Genre? { get }
```
The parent genre, if any.

## Relationships

### Conforms To

- [`FilterableMusicItem`](../protocols/FilterProtocols.md#filterablemusicitem)
- [`MusicCatalogTopLevelResourceRequesting`](../protocols/RequestProtocols.md#musiccatalogtoplevelresourcerequesting)
- [`MusicItem`](../protocols/UtilityProtocols.md#musicitem)
- [`MusicLibraryRequestable`](../protocols/RequestProtocols.md#musiclibraryrequestable)
- [`MusicLibrarySectionRequestable`](../protocols/RequestProtocols.md#musiclibrarysectionrequestable)
- [`MusicPropertyContainer`](../protocols/UtilityProtocols.md#musicpropertycontainer)

## See Also

### Music Items

[`struct Album`](Album.md) - A music item that represents an album.

[`struct Artist`](Artist.md) - A music item that represents an artist.

[`struct Curator`](Curator.md) - A music item that represents a curator.

[`struct MusicVideo`](MusicVideo.md) - A music item that represents a music video.

[`struct Playlist`](Playlist.md) - A music item that represents a playlist.

[`struct RadioShow`](RadioShow.md) - A music item that represents a radio show.

[`struct RecordLabel`](RecordLabel.md) - A music item that represents a record label.

[`struct Song`](Song.md) - A music item that represents a song.

[`struct Station`](Station.md) - A music item that represents a station.

[`enum Track`](Track.md) - A music item that represents a track.