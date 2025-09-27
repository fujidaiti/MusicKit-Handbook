# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/curator

- [MusicKit](/documentation/musickit)
- Curator

Structure

# Curator

A music item that represents a curator.

iOS 15.4+iPadOS 15.4+Mac Catalyst 15.4+macOS 12.3+tvOS 15.4+visionOS 1.0+watchOS 9.0+

```
struct Curator
```

## [Topics](/documentation/musickit/curator#topics)

### [Instance Properties](/documentation/musickit/curator#Instance-Properties)

[`var artwork: Artwork?`](/documentation/musickit/curator/artwork)

The curator artwork.

[`var editorialNotes: EditorialNotes?`](/documentation/musickit/curator/editorialnotes)

The notes about the curator that appear in the Music catalog.

[`let id: MusicItemID`](/documentation/musickit/curator/id)

The unique identifier for the curator.

[`var kind: Curator.Kind`](/documentation/musickit/curator/kind-swift.property)

The kind of curator.

[`var name: String`](/documentation/musickit/curator/name)

The name of the curator.

[`var playlists: MusicItemCollection<Playlist>?`](/documentation/musickit/curator/playlists)

The curator’s associated playlists.

[`var url: URL?`](/documentation/musickit/curator/url)

The URL for the curator.

### [Enumerations](/documentation/musickit/curator#Enumerations)

[`enum Kind`](/documentation/musickit/curator/kind-swift.enum)

The available kinds of curators.

### [Default Implementations](/documentation/musickit/curator#Default-Implementations)

[API Reference

FilterableMusicItem Implementations](/documentation/musickit/curator/filterablemusicitem-implementations)

## [Relationships](/documentation/musickit/curator#relationships)

### [Conforms To](/documentation/musickit/curator#conforms-to)

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

## [See Also](/documentation/musickit/curator#see-also)

### [Music Items](/documentation/musickit/curator#Music-Items)

[`struct Album`](/documentation/musickit/album)

A music item that represents an album.

[`struct Artist`](/documentation/musickit/artist)

A music item that represents an artist.

[`struct Genre`](/documentation/musickit/genre)

A music item that represents a genre.

[`struct MusicVideo`](/documentation/musickit/musicvideo)

A music item that represents a music video.

[`struct Playlist`](/documentation/musickit/playlist)

A music item that represents a playlist.

[`struct RadioShow`](/documentation/musickit/radioshow)

A music item that represents a radio show.

[`struct RecordLabel`](/documentation/musickit/recordlabel)

A music item that represents a record label.

[`struct Song`](/documentation/musickit/song)

A music item that represents a song.

[`struct Station`](/documentation/musickit/station)

A music item that represents a station.

[`enum Track`](/documentation/musickit/track)

A music item that represents a track.
