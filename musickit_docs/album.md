# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/album

- [MusicKit](/documentation/musickit)
- Album

Structure

# Album

A music item that represents an album.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct Album
```

## [Topics](/documentation/musickit/album#topics)

### [Instance Properties](/documentation/musickit/album#Instance-Properties)

[`var appearsOn: MusicItemCollection<Playlist>?`](/documentation/musickit/album/appearson)

A collection of playlists that include tracks from the album.

[`var artistName: String`](/documentation/musickit/album/artistname)

The artist’s name.

[`var artistURL: URL?`](/documentation/musickit/album/artisturl)

The artist’s URL.

[`var artists: MusicItemCollection<Artist>?`](/documentation/musickit/album/artists)

The album’s associated artists.

[`var artwork: Artwork?`](/documentation/musickit/album/artwork)

The album artwork.

[`var audioVariants: [AudioVariant]?`](/documentation/musickit/album/audiovariants)

The variants that indicate the quality of audio available for the album.

[`var contentRating: ContentRating?`](/documentation/musickit/album/contentrating)

The rating of the content.

[`var copyright: String?`](/documentation/musickit/album/copyright)

The copyright text for the album.

[`var editorialNotes: EditorialNotes?`](/documentation/musickit/album/editorialnotes)

The notes about the album that appear in the Music app.

[`var genreNames: [String]`](/documentation/musickit/album/genrenames)

The names of the album’s associated genres.

[`var genres: MusicItemCollection<Genre>?`](/documentation/musickit/album/genres)

The genres for the album.

[`let id: MusicItemID`](/documentation/musickit/album/id)

The unique identifier for the album.

[`var isAppleDigitalMaster: Bool?`](/documentation/musickit/album/isappledigitalmaster)

A Boolean value that indicates whether the album is an Apple Digital Master.

[`var isCompilation: Bool?`](/documentation/musickit/album/iscompilation)

A Boolean value that indicates whether the album is a compilation.

[`var isComplete: Bool?`](/documentation/musickit/album/iscomplete)

A Boolean value that indicates whether the album is complete.

[`var isSingle: Bool?`](/documentation/musickit/album/issingle)

A Boolean value that indicates whether the album consists of a single song.

[`var lastPlayedDate: Date?`](/documentation/musickit/album/lastplayeddate)

The date when the user last played the album on this device.

[`var libraryAddedDate: Date?`](/documentation/musickit/album/libraryaddeddate)

The date when the user added the album to the library.

[`var otherVersions: MusicItemCollection<Album>?`](/documentation/musickit/album/otherversions)

A collection of other versions of the album.

[`var playParameters: PlayParameters?`](/documentation/musickit/album/playparameters)

The parameters to use to play the tracks of the album.

[`var recordLabelName: String?`](/documentation/musickit/album/recordlabelname)

The name of the album’s record label.

[`var recordLabels: MusicItemCollection<RecordLabel>?`](/documentation/musickit/album/recordlabels)

The record labels for the album.

[`var relatedAlbums: MusicItemCollection<Album>?`](/documentation/musickit/album/relatedalbums)

A collection of related albums.

[`var relatedVideos: MusicItemCollection<MusicVideo>?`](/documentation/musickit/album/relatedvideos)

A collection of the album’s music videos.

[`var releaseDate: Date?`](/documentation/musickit/album/releasedate)

The release date (or expected prerelease date) for the album.

[`var title: String`](/documentation/musickit/album/title)

The title of the album.

[`var trackCount: Int`](/documentation/musickit/album/trackcount)

The number of tracks for the album.

[`var tracks: MusicItemCollection<Track>?`](/documentation/musickit/album/tracks)

The tracks on the album.

[`var upc: String?`](/documentation/musickit/album/upc)

The universal product code (UPC) for the album.

[`var url: URL?`](/documentation/musickit/album/url)

The URL for the album.

### [Default Implementations](/documentation/musickit/album#Default-Implementations)

[API Reference

FilterableMusicItem Implementations](/documentation/musickit/album/filterablemusicitem-implementations)

[API Reference

MusicLibraryRequestable Implementations](/documentation/musickit/album/musiclibraryrequestable-implementations)

## [Relationships](/documentation/musickit/album#relationships)

### [Conforms To](/documentation/musickit/album#conforms-to)

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

## [See Also](/documentation/musickit/album#see-also)

### [Music Items](/documentation/musickit/album#Music-Items)

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

[`struct Station`](/documentation/musickit/station)

A music item that represents a station.

[`enum Track`](/documentation/musickit/track)

A music item that represents a track.
