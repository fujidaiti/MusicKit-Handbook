# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/artist

- [MusicKit](/documentation/musickit)
- Artist

Structure

# Artist

A music item that represents an artist.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct Artist
```

## [Topics](/documentation/musickit/artist#topics)

### [Instance Properties](/documentation/musickit/artist#Instance-Properties)

[`var albums: MusicItemCollection<Album>?`](/documentation/musickit/artist/albums)

The artist’s associated albums.

[`var appearsOnAlbums: MusicItemCollection<Album>?`](/documentation/musickit/artist/appearsonalbums)

A collection of albums from other artists that this artist appears on.

[`var artwork: Artwork?`](/documentation/musickit/artist/artwork)

The artist artwork.

[`var compilationAlbums: MusicItemCollection<Album>?`](/documentation/musickit/artist/compilationalbums)

A collection of compilation albums that include tracks by the artist.

[`var editorialNotes: EditorialNotes?`](/documentation/musickit/artist/editorialnotes)

The notes about the artist that appear in the Music catalog.

[`var featuredAlbums: MusicItemCollection<Album>?`](/documentation/musickit/artist/featuredalbums)

A collection of featured albums of the artist.

[`var featuredPlaylists: MusicItemCollection<Playlist>?`](/documentation/musickit/artist/featuredplaylists)

A collection of the artist’s associated playlists.

[`var fullAlbums: MusicItemCollection<Album>?`](/documentation/musickit/artist/fullalbums)

A collection of the artist’s full-release albums.

[`var genreNames: [String]?`](/documentation/musickit/artist/genrenames)

The names of this artist’s associated genres.

[`var genres: MusicItemCollection<Genre>?`](/documentation/musickit/artist/genres)

The artist’s associated genres.

[`let id: MusicItemID`](/documentation/musickit/artist/id)

The unique identifier for the artist.

[`var latestRelease: Album?`](/documentation/musickit/artist/latestrelease)

The artist’s most recent album.

[`var libraryAddedDate: Date?`](/documentation/musickit/artist/libraryaddeddate)

The date when the user added the artist to the library.

[`var liveAlbums: MusicItemCollection<Album>?`](/documentation/musickit/artist/livealbums)

A collection of the artist’s live albums.

[`var musicVideos: MusicItemCollection<MusicVideo>?`](/documentation/musickit/artist/musicvideos)

The artist’s associated music videos.

[`var name: String`](/documentation/musickit/artist/name)

The name of the artist.

[`var playlists: MusicItemCollection<Playlist>?`](/documentation/musickit/artist/playlists)

The artist’s associated playlists.

[`var similarArtists: MusicItemCollection<Artist>?`](/documentation/musickit/artist/similarartists)

A collection of artists similar to this artist.

[`var singles: MusicItemCollection<Album>?`](/documentation/musickit/artist/singles)

A collection of the artist’s associated albums in the *singles* category.

[`var station: Station?`](/documentation/musickit/artist/station)

The artist’s associated station.

[`var topMusicVideos: MusicItemCollection<MusicVideo>?`](/documentation/musickit/artist/topmusicvideos)

A collection of the artist’s top music videos.

[`var topSongs: MusicItemCollection<Song>?`](/documentation/musickit/artist/topsongs)

A collection of the artist’s top songs.

[`var url: URL?`](/documentation/musickit/artist/url)

The URL for the artist.

### [Default Implementations](/documentation/musickit/artist#Default-Implementations)

[API Reference

FilterableMusicItem Implementations](/documentation/musickit/artist/filterablemusicitem-implementations)

[API Reference

MusicLibraryRequestable Implementations](/documentation/musickit/artist/musiclibraryrequestable-implementations)

## [Relationships](/documentation/musickit/artist#relationships)

### [Conforms To](/documentation/musickit/artist#conforms-to)

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
- [`MusicLibraryRequestable`](/documentation/musickit/musiclibraryrequestable)
- [`MusicLibrarySearchable`](/documentation/musickit/musiclibrarysearchable)
- [`MusicLibrarySectionRequestable`](/documentation/musickit/musiclibrarysectionrequestable)
- [`MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/artist#see-also)

### [Music Items](/documentation/musickit/artist#Music-Items)

[`struct Album`](/documentation/musickit/album)

A music item that represents an album.

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
