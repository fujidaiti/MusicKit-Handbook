# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/station

- [MusicKit](/documentation/musickit)
- Station

Structure

# Station

A music item that represents a station.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct Station
```

## [Topics](/documentation/musickit/station#topics)

### [Instance Properties](/documentation/musickit/station#Instance-Properties)

[`var artwork: Artwork?`](/documentation/musickit/station/artwork)

The station artwork.

[`var contentRating: ContentRating?`](/documentation/musickit/station/contentrating)

The rating of the content that potentially plays while playing the station.

[`var duration: TimeInterval?`](/documentation/musickit/station/duration)

The duration of the stream.

[`var editorialNotes: EditorialNotes?`](/documentation/musickit/station/editorialnotes)

The notes about the station that appear in the Music app.

[`var episodeNumber: Int?`](/documentation/musickit/station/episodenumber)

The episode number of the station.

[`let id: MusicItemID`](/documentation/musickit/station/id)

The unique identifier for the station.

[`var isLive: Bool`](/documentation/musickit/station/islive)

A Boolean value that indicates whether the station is live.

[`var name: String`](/documentation/musickit/station/name)

The name of the station.

[`var playParameters: PlayParameters?`](/documentation/musickit/station/playparameters)

The parameters to use to play the station.

[`var stationProviderName: String?`](/documentation/musickit/station/stationprovidername)

The name of the entity that provides the station.

[`var url: URL?`](/documentation/musickit/station/url)

The URL for the station.

### [Default Implementations](/documentation/musickit/station#Default-Implementations)

[API Reference

FilterableMusicItem Implementations](/documentation/musickit/station/filterablemusicitem-implementations)

## [Relationships](/documentation/musickit/station#relationships)

### [Conforms To](/documentation/musickit/station#conforms-to)

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
- [`MusicPersonalRecommendationItem`](/documentation/musickit/musicpersonalrecommendationitem)
- [`MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)
- [`MusicRecentlyPlayedRequestable`](/documentation/musickit/musicrecentlyplayedrequestable)
- [`PlayableMusicItem`](/documentation/musickit/playablemusicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/station#see-also)

### [Music Items](/documentation/musickit/station#Music-Items)

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

[`struct RecordLabel`](/documentation/musickit/recordlabel)

A music item that represents a record label.

[`struct Song`](/documentation/musickit/song)

A music item that represents a song.

[`enum Track`](/documentation/musickit/track)

A music item that represents a track.
