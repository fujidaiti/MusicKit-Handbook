# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/recordlabel

- [MusicKit](/documentation/musickit)
- RecordLabel

Structure

# RecordLabel

A music item that represents a record label.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct RecordLabel
```

## [Topics](/documentation/musickit/recordlabel#topics)

### [Instance Properties](/documentation/musickit/recordlabel#Instance-Properties)

[`var artwork: Artwork?`](/documentation/musickit/recordlabel/artwork)

The record label’s artwork.

[`let id: MusicItemID`](/documentation/musickit/recordlabel/id)

The unique identifier for the record label.

[`var latestReleases: MusicItemCollection<Album>?`](/documentation/musickit/recordlabel/latestreleases)

A collection of the most recent releases for the record label.

[`var name: String`](/documentation/musickit/recordlabel/name)

The name of the record label.

[`var shortDescription: String?`](/documentation/musickit/recordlabel/shortdescription)

An abbreviated description to show inline or when the record label appears alongside other content.

[`var standardDescription: String?`](/documentation/musickit/recordlabel/standarddescription)

A description to show when the record label is prominently displayed.

[`var topReleases: MusicItemCollection<Album>?`](/documentation/musickit/recordlabel/topreleases)

A collection of top releases for the record label.

[`var url: URL?`](/documentation/musickit/recordlabel/url)

The URL for the record label.

### [Default Implementations](/documentation/musickit/recordlabel#Default-Implementations)

[API Reference

FilterableMusicItem Implementations](/documentation/musickit/recordlabel/filterablemusicitem-implementations)

## [Relationships](/documentation/musickit/recordlabel#relationships)

### [Conforms To](/documentation/musickit/recordlabel#conforms-to)

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

## [See Also](/documentation/musickit/recordlabel#see-also)

### [Music Items](/documentation/musickit/recordlabel#Music-Items)

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

[`struct RadioShow`](/documentation/musickit/radioshow)

A music item that represents a radio show.

[`struct Song`](/documentation/musickit/song)

A music item that represents a song.

[`struct Station`](/documentation/musickit/station)

A music item that represents a station.

[`enum Track`](/documentation/musickit/track)

A music item that represents a track.
