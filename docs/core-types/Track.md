# Track

> Source: https://developer.apple.com/documentation/musickit/track

```swift
enum Track
```

A music item that represents a track.

## Enumeration Cases

```swift
case musicVideo(MusicVideo)
```
A track that corresponds to a music video.

```swift
case song(Song)
```
A track that corresponds to a song.

## Properties

### Instance Properties

```swift
var albumTitle: String? { get }
```
The title of the album the track appears on.

```swift
var albums: MusicItemCollection<Album>? { get }
```
The track's associated albums.

```swift
var artistName: String { get }
```
The artist's name.

```swift
var artistURL: URL? { get }
```
The artist's URL.

```swift
var artists: MusicItemCollection<Artist>? { get }
```
The track's associated artists.

```swift
var artwork: Artwork? { get }
```
The artwork for the track.

```swift
var contentRating: ContentRating? { get }
```
The rating of the content.

```swift
var discNumber: Int? { get }
```
The disc number of the track.

```swift
var duration: TimeInterval? { get }
```
The duration of the track.

```swift
var editorialNotes: EditorialNotes? { get }
```
The editorial notes for the track.

```swift
var genreNames: [String] { get }
```
The names of the track's associated genres.

```swift
var genres: MusicItemCollection<Genre>? { get }
```
The track's associated genres.

```swift
var id: MusicItemID { get }
```
The unique identifier for the track.

```swift
var isrc: String? { get }
```
The International Standard Recording Code (ISRC) for the track.

```swift
var lastPlayedDate: Date? { get }
```
The date when the user last played the track on this device.

```swift
var libraryAddedDate: Date? { get }
```
The date when the user added the track to the library.

```swift
var playCount: Int? { get }
```
The number of times the user played the track.

```swift
var playParameters: PlayParameters? { get }
```
The parameters to use to play the track.

```swift
var previewAssets: [PreviewAsset]? { get }
```
The preview assets for the track.

```swift
var releaseDate: Date? { get }
```
The release date (or expected for pre-release) of the track.

```swift
var title: String { get }
```
The title of the track.

```swift
var trackNumber: Int? { get }
```
The track's number in the album's track list.

```swift
var url: URL? { get }
```
The URL for the track.

```swift
var workName: String? { get }
```
For classical music only, the name of the associated work.

## Relationships

### Conforms To

- [`MusicItem`](../protocols/UtilityProtocols.md#musicitem)
- [`MusicLibraryAddable`](../protocols/PlaybackProtocols.md#musiclibraryaddable)
- [`MusicLibraryRequestable`](../protocols/RequestProtocols.md#musiclibraryrequestable)
- [`MusicPlaylistAddable`](../protocols/PlaybackProtocols.md#musicplaylistaddable)
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

[`struct Station`](Station.md) - A music item that represents a station.