# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/radioshow

- [MusicKit](/documentation/musickit)
- RadioShow

Structure

# RadioShow

A music item that represents a radio show.

iOS 15.4+iPadOS 15.4+Mac Catalyst 15.4+macOS 12.3+tvOS 15.4+visionOS 1.0+watchOS 9.0+

```
struct RadioShow
```

## [Topics](/documentation/musickit/radioshow#topics)

### [Instance Properties](/documentation/musickit/radioshow#Instance-Properties)

[`var artwork: Artwork?`](/documentation/musickit/radioshow/artwork)

The radio show artwork.

[`var editorialNotes: EditorialNotes?`](/documentation/musickit/radioshow/editorialnotes)

The notes about the radio show that appear in the Music catalog.

[`var hostName: String?`](/documentation/musickit/radioshow/hostname)

The name of the host for the radio show.

[`let id: MusicItemID`](/documentation/musickit/radioshow/id)

The unique identifier for the radio show.

[`var name: String`](/documentation/musickit/radioshow/name)

The name of the radio show.

[`var playlists: MusicItemCollection<Playlist>?`](/documentation/musickit/radioshow/playlists)

The radio show’s associated playlists.

[`var url: URL?`](/documentation/musickit/radioshow/url)

The URL for the radio show.

### [Default Implementations](/documentation/musickit/radioshow#Default-Implementations)

[API Reference

FilterableMusicItem Implementations](/documentation/musickit/radioshow/filterablemusicitem-implementations)

## [Relationships](/documentation/musickit/radioshow#relationships)

### [Conforms To](/documentation/musickit/radioshow#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`FilterableMusicItem`](/documentation/musickit/filterablemusicitem)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`MusicCatalogSearchable`](/documentation/musickit/musiccatalogsearchable)
- [`MusicItem`](/documentation/musickit/musicitem)
- [`MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/radioshow#see-also)

### [Music Items](/documentation/musickit/radioshow#Music-Items)

[`struct Album`](/documentation/musickit/album)

A music item that represents an album.

[`struct Artist`](/documentation/musickit/artist)

A music item that represents an artist.

[`struct Curator`](/documentation/musickit/curator)

A music item that represents a curator.

[`struct Genre`](/documentation/musickit/genre)

A music item that represents a genre.

[`struct MusicVideo`](/documentation/musickit/musicvideo)

A music item that represents a music video.

[`struct Playlist`](/documentation/musickit/playlist)

A music item that represents a playlist.

[`struct RecordLabel`](/documentation/musickit/recordlabel)

A music item that represents a record label.

[`struct Song`](/documentation/musickit/song)

A music item that represents a song.

[`struct Station`](/documentation/musickit/station)

A music item that represents a station.

[`enum Track`](/documentation/musickit/track)

A music item that represents a track.
