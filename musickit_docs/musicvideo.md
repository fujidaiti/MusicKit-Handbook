# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicvideo

- [MusicKit](/documentation/musickit)
- MusicVideo

Structure

# MusicVideo

A music item that represents a music video.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicVideo
```

## [Topics](/documentation/musickit/musicvideo#topics)

### [Instance Properties](/documentation/musickit/musicvideo#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/musicvideo/albumtitle)

The title of the album the music video appears on.

[`var albums: MusicItemCollection<Album>?`](/documentation/musickit/musicvideo/albums)

The music video’s associated albums.

[`var artistName: String`](/documentation/musickit/musicvideo/artistname)

The artist’s name.

[`var artistURL: URL?`](/documentation/musickit/musicvideo/artisturl)

The artist’s URL.

[`var artists: MusicItemCollection<Artist>?`](/documentation/musickit/musicvideo/artists)

The music video’s associated artists.

[`var artwork: Artwork?`](/documentation/musickit/musicvideo/artwork)

The artwork for the music video.

[`var contentRating: ContentRating?`](/documentation/musickit/musicvideo/contentrating)

The rating of the content.

[`var duration: TimeInterval?`](/documentation/musickit/musicvideo/duration)

The duration of the music video.

[`var editorialNotes: EditorialNotes?`](/documentation/musickit/musicvideo/editorialnotes)

The editorial notes for the music video.

[`var genreNames: [String]`](/documentation/musickit/musicvideo/genrenames)

The names of the music video’s associated genres.

[`var genres: MusicItemCollection<Genre>?`](/documentation/musickit/musicvideo/genres)

The music video’s associated genres.

[`var has4K: Bool?`](/documentation/musickit/musicvideo/has4k)

A Boolean value that indicates whether the music video has 4K content.

[`var hasHDR: Bool?`](/documentation/musickit/musicvideo/hashdr)

A Boolean value that indicates whether the music video has HDR10-encoded content.

[`let id: MusicItemID`](/documentation/musickit/musicvideo/id)

The unique identifier for the music video.

[`var isPreview: Bool`](/documentation/musickit/musicvideo/ispreview)

A Boolean value that indicates whether this content corresponds to a subscription video preview.

[`var isrc: String?`](/documentation/musickit/musicvideo/isrc)

The International Standard Recording Code (ISRC) for the music video.

[`var lastPlayedDate: Date?`](/documentation/musickit/musicvideo/lastplayeddate)

The date when the user last played the music video on this device.

[`var libraryAddedDate: Date?`](/documentation/musickit/musicvideo/libraryaddeddate)

The date when the user added the music video to the library.

[`var moreByArtist: MusicItemCollection<MusicVideo>?`](/documentation/musickit/musicvideo/morebyartist)

A collection of additional music videos by the artist.

[`var moreInGenre: MusicItemCollection<MusicVideo>?`](/documentation/musickit/musicvideo/moreingenre)

A collection of music videos in the same genre as this music video.

[`var playCount: Int?`](/documentation/musickit/musicvideo/playcount)

The number of times the user played the music video.

[`var playParameters: PlayParameters?`](/documentation/musickit/musicvideo/playparameters)

The parameters to use to play the music video.

[`var previewAssets: [PreviewAsset]?`](/documentation/musickit/musicvideo/previewassets)

The preview assets for the music video.

[`var releaseDate: Date?`](/documentation/musickit/musicvideo/releasedate)

The release date (or expected prerelease date) for the music video.

[`var songs: MusicItemCollection<Song>?`](/documentation/musickit/musicvideo/songs)

The music video’s associated songs.

[`var title: String`](/documentation/musickit/musicvideo/title)

The title of the music video.

[`var trackNumber: Int?`](/documentation/musickit/musicvideo/tracknumber)

The music video’s number in the album’s track list.

[`var url: URL?`](/documentation/musickit/musicvideo/url)

The URL for the music video.

[`var workName: String?`](/documentation/musickit/musicvideo/workname)

For classical music only, the name of the associated work.

### [Default Implementations](/documentation/musickit/musicvideo#Default-Implementations)

[API Reference

FilterableMusicItem Implementations](/documentation/musickit/musicvideo/filterablemusicitem-implementations)

[API Reference

MusicLibraryRequestable Implementations](/documentation/musickit/musicvideo/musiclibraryrequestable-implementations)

## [Relationships](/documentation/musickit/musicvideo#relationships)

### [Conforms To](/documentation/musickit/musicvideo#conforms-to)

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
- [`MusicPlaylistAddable`](/documentation/musickit/musicplaylistaddable)
- [`MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)
- [`MusicRecentlyPlayedRequestable`](/documentation/musickit/musicrecentlyplayedrequestable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/musicvideo#see-also)

### [Music Items](/documentation/musickit/musicvideo#Music-Items)

[`struct Album`](/documentation/musickit/album)

A music item that represents an album.

[`struct Artist`](/documentation/musickit/artist)

A music item that represents an artist.

[`struct Curator`](/documentation/musickit/curator)

A music item that represents a curator.

[`struct Genre`](/documentation/musickit/genre)

A music item that represents a genre.

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
