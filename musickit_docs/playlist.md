# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/playlist

- [MusicKit](/documentation/musickit)
- Playlist

Structure

# Playlist

A music item that represents a playlist.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct Playlist
```

## [Topics](/documentation/musickit/playlist#topics)

### [Structures](/documentation/musickit/playlist#Structures)

[`struct Entry`](/documentation/musickit/playlist/entry)

A music item that represents a playlist entry.

### [Instance Properties](/documentation/musickit/playlist#Instance-Properties)

[`var artwork: Artwork?`](/documentation/musickit/playlist/artwork)

The artwork for the playlist.

[`var curator: Curator?`](/documentation/musickit/playlist/curator)

The playlist’s associated curator.

[`var curatorName: String?`](/documentation/musickit/playlist/curatorname)

The display name for the playlist’s curator.

[`var entries: MusicItemCollection<Playlist.Entry>?`](/documentation/musickit/playlist/entries)

The entries in the playlist

[`var featuredArtists: MusicItemCollection<Artist>?`](/documentation/musickit/playlist/featuredartists)

A collection of featured artists for this playlist.

[`let id: MusicItemID`](/documentation/musickit/playlist/id)

The unique identifier for the playlist.

[`var isChart: Bool?`](/documentation/musickit/playlist/ischart)

A Boolean value that indicates whether the playlist represents a popularity chart.

[`var kind: Playlist.Kind?`](/documentation/musickit/playlist/kind-swift.property)

The kind of playlist.

[`var lastModifiedDate: Date?`](/documentation/musickit/playlist/lastmodifieddate)

The playlist’s most recent modification date.

[`var lastPlayedDate: Date?`](/documentation/musickit/playlist/lastplayeddate)

The date when the user last played the playlist on this device.

[`var libraryAddedDate: Date?`](/documentation/musickit/playlist/libraryaddeddate)

The date when the user added the playlist to the library.

[`var moreByCurator: MusicItemCollection<Playlist>?`](/documentation/musickit/playlist/morebycurator)

A collection of additional playlists by the same curator.

[`var name: String`](/documentation/musickit/playlist/name)

The name of the playlist.

[`var playParameters: PlayParameters?`](/documentation/musickit/playlist/playparameters)

The parameters to use to play the tracks in the playlist.

[`var radioShow: RadioShow?`](/documentation/musickit/playlist/radioshow)

The playlist’s associated radio show.

[`var shortDescription: String?`](/documentation/musickit/playlist/shortdescription)

An abbreviated description to show inline or when the playlist appears alongside other content.

[`var standardDescription: String?`](/documentation/musickit/playlist/standarddescription)

A description to show when the playlist is prominently displayed.

[`var tracks: MusicItemCollection<Track>?`](/documentation/musickit/playlist/tracks)

The tracks in the playlist.

[`var url: URL?`](/documentation/musickit/playlist/url)

The URL for the playlist.

### [Enumerations](/documentation/musickit/playlist#Enumerations)

[`enum Kind`](/documentation/musickit/playlist/kind-swift.enum)

The available kinds of playlists.

### [Default Implementations](/documentation/musickit/playlist#Default-Implementations)

[API Reference

FilterableMusicItem Implementations](/documentation/musickit/playlist/filterablemusicitem-implementations)

[API Reference

MusicLibraryRequestable Implementations](/documentation/musickit/playlist/musiclibraryrequestable-implementations)

## [Relationships](/documentation/musickit/playlist#relationships)

### [Conforms To](/documentation/musickit/playlist#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`FilterableMusicItem`](/documentation/musickit/filterablemusicitem)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`MusicCatalogChartRequestable`](/documentation/musickit/musiccatalogchartrequestable)
- [`MusicCatalogSearchable`](/documentation/musickit/musiccatalogsearchable)
- [`MusicItem`](/documentation/musickit/musicitem)
- [`MusicLibraryAddable`](/documentation/musickit/musiclibraryaddable)
- [`MusicLibraryRequestable`](/documentation/musickit/musiclibraryrequestable)
- [`MusicLibrarySearchable`](/documentation/musickit/musiclibrarysearchable)
- [`MusicLibrarySectionRequestable`](/documentation/musickit/musiclibrarysectionrequestable)
- [`MusicPersonalRecommendationItem`](/documentation/musickit/musicpersonalrecommendationitem)
- [`MusicPlaylistAddable`](/documentation/musickit/musicplaylistaddable)
- [`MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)
- [`PlayableMusicItem`](/documentation/musickit/playablemusicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/playlist#see-also)

### [Music Items](/documentation/musickit/playlist#Music-Items)

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
