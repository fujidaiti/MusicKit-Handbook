# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/partialmusicproperty

- [MusicKit](/documentation/musickit)
- PartialMusicProperty

Class

# PartialMusicProperty

A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
class PartialMusicProperty<Root>
```

## [Topics](/documentation/musickit/partialmusicproperty#topics)

### [Type Properties](/documentation/musickit/partialmusicproperty#Type-Properties)

[`static let albums: MusicRelationshipProperty<Artist, Album>`](/documentation/musickit/partialmusicproperty/albums-2huns)

An identifier for the relationship property that returns the associated albums for the artist.

[`static let albums: MusicRelationshipProperty<Song, Album>`](/documentation/musickit/partialmusicproperty/albums-5kqf6)

An identifier for the relationship property that returns the associated albums for the song.

[`static let albums: MusicRelationshipProperty<MusicVideo, Album>`](/documentation/musickit/partialmusicproperty/albums-6v0rp)

An identifier of the relationship property that returns the associated albums for the music video.

[`static let appearsOn: MusicRelationshipProperty<Album, Playlist>`](/documentation/musickit/partialmusicproperty/appearson)

An identifier for the association property that returns a collection of playlists that include tracks from the album.

[`static let appearsOnAlbums: MusicRelationshipProperty<Artist, Album>`](/documentation/musickit/partialmusicproperty/appearsonalbums)

An identifier for the association property that returns a collection of albums from other artists that this artist appears on.

[`static var artistURL: MusicExtendedAttributeProperty<MusicVideo, URL>`](/documentation/musickit/partialmusicproperty/artisturl-7j56f)

An identifier for the extended attribute property that returns the artist’s URL.

[`static var artistURL: MusicExtendedAttributeProperty<Song, URL>`](/documentation/musickit/partialmusicproperty/artisturl-81r7i)

An identifier for the extended attribute property that returns the artist’s URL.

[`static var artistURL: MusicExtendedAttributeProperty<Album, URL>`](/documentation/musickit/partialmusicproperty/artisturl-msvj)

An identifier for the extended attribute property that returns the artist’s URL.

[`static let artists: MusicRelationshipProperty<Album, Artist>`](/documentation/musickit/partialmusicproperty/artists-1bm4c)

An identifier for the relationship property that returns the associated artists for the album.

[`static let artists: MusicRelationshipProperty<Song, Artist>`](/documentation/musickit/partialmusicproperty/artists-3x8cx)

An identifier for the relationship property that returns the associated artists for the song.

[`static let artists: MusicRelationshipProperty<MusicVideo, Artist>`](/documentation/musickit/partialmusicproperty/artists-6myll)

An identifier of the relationship property that returns the associated artists for the music video.

[`static let audioVariants: MusicExtendedAttributeProperty<Song, [AudioVariant]>`](/documentation/musickit/partialmusicproperty/audiovariants-60v28)

An identifier for the extended attribute property that returns the audio variants for the song.

[`static let audioVariants: MusicExtendedAttributeProperty<Album, [AudioVariant]>`](/documentation/musickit/partialmusicproperty/audiovariants-8zkt2)

An identifier for the extended attribute property that returns the audio variants for the album.

[`static let compilationAlbums: MusicRelationshipProperty<Artist, Album>`](/documentation/musickit/partialmusicproperty/compilationalbums)

An identifier for the association property that returns a collection of compilation albums that include tracks by the artist.

[`static let composers: MusicRelationshipProperty<Song, Artist>`](/documentation/musickit/partialmusicproperty/composers)

An identifier for the relationship property that returns the song’s composers.

[`static let curator: MusicRelationshipProperty<Playlist, Curator>`](/documentation/musickit/partialmusicproperty/curator)

An identifier for the extended attribute property that returns the playlist’s associated curator.

[`static let entries: MusicRelationshipProperty<Playlist, Playlist.Entry>`](/documentation/musickit/partialmusicproperty/entries)

An identifier for the relationship property that returns the entries in the playlist.

[`static let featuredAlbums: MusicRelationshipProperty<Artist, Album>`](/documentation/musickit/partialmusicproperty/featuredalbums)

An identifier for the association property that returns a collection of featured albums for the artist.

[`static let featuredArtists: MusicRelationshipProperty<Playlist, Artist>`](/documentation/musickit/partialmusicproperty/featuredartists)

An identifier for the association property that returns a collection of featured artists for this playlist.

[`static let featuredPlaylists: MusicRelationshipProperty<Artist, Playlist>`](/documentation/musickit/partialmusicproperty/featuredplaylists)

An identifier for the association property that returns a collection of the artist’s playlists.

[`static let fullAlbums: MusicRelationshipProperty<Artist, Album>`](/documentation/musickit/partialmusicproperty/fullalbums)

An identifier for the association property that returns a collection of the artist’s full-release albums.

[`static let genres: MusicRelationshipProperty<MusicVideo, Genre>`](/documentation/musickit/partialmusicproperty/genres-2y2ss)

An identifier of the relationship property that returns the associated genres for the music video.

[`static let genres: MusicRelationshipProperty<Artist, Genre>`](/documentation/musickit/partialmusicproperty/genres-3jsli)

An identifier for the relationship property that returns the associated genres for the artist.

[`static let genres: MusicRelationshipProperty<Song, Genre>`](/documentation/musickit/partialmusicproperty/genres-5w9nm)

An identifier for the relationship property that returns the associated genres for the song.

[`static let genres: MusicRelationshipProperty<Album, Genre>`](/documentation/musickit/partialmusicproperty/genres-7el74)

An identifier for the relationship property that returns the genres for the album.

[`static let latestRelease: MusicRelationshipProperty<Artist, Album>`](/documentation/musickit/partialmusicproperty/latestrelease)

An identifier for the association property that returns the artist’s most recent album.

[`static var latestReleases: MusicRelationshipProperty<RecordLabel, Album>`](/documentation/musickit/partialmusicproperty/latestreleases)

An identifier for the association property that returns a collection of the most recent releases for the record label.

[`static let liveAlbums: MusicRelationshipProperty<Artist, Album>`](/documentation/musickit/partialmusicproperty/livealbums)

An identifier for the association property that returns a collection of the artist’s live albums.

[`static let moreByArtist: MusicRelationshipProperty<MusicVideo, MusicVideo>`](/documentation/musickit/partialmusicproperty/morebyartist)

An identifier of the association property that returns a collection of additional music videos by the artist.

[`static let moreByCurator: MusicRelationshipProperty<Playlist, Playlist>`](/documentation/musickit/partialmusicproperty/morebycurator)

An identifier for the association property that returns a collection of additional playlists by the same curator.

[`static let moreInGenre: MusicRelationshipProperty<MusicVideo, MusicVideo>`](/documentation/musickit/partialmusicproperty/moreingenre)

A identifier of the association property that returns a collection of music videos in the same genre as this music video.

[`static let musicVideos: MusicRelationshipProperty<Artist, MusicVideo>`](/documentation/musickit/partialmusicproperty/musicvideos-6hip3)

An identifier for the relationship property that returns the associated music videos for the artist.

[`static let musicVideos: MusicRelationshipProperty<Song, MusicVideo>`](/documentation/musickit/partialmusicproperty/musicvideos-89mym)

An identifier for the relationship property that returns the song’s associated music videos.

[`static let otherVersions: MusicRelationshipProperty<Album, Album>`](/documentation/musickit/partialmusicproperty/otherversions)

An identifier for the association property that returns a collection of other versions of the album.

[`static let playlists: MusicRelationshipProperty<Artist, Playlist>`](/documentation/musickit/partialmusicproperty/playlists-1j0l9)

An identifier for the relationship property that returns the associated playlists for the artist.

[`static let playlists: MusicRelationshipProperty<Curator, Playlist>`](/documentation/musickit/partialmusicproperty/playlists-9quj1)

An identifier for the relationship property that returns the associated playlists for the curator.

[`static let playlists: MusicRelationshipProperty<RadioShow, Playlist>`](/documentation/musickit/partialmusicproperty/playlists-wgt7)

An identifier for the relationship property that returns the associated playlists for the radio show.

[`static let radioShow: MusicRelationshipProperty<Playlist, RadioShow>`](/documentation/musickit/partialmusicproperty/radioshow)

An identifier for the extended attribute property that returns the playlist’s associated radio show.

[`static let recordLabels: MusicRelationshipProperty<Album, RecordLabel>`](/documentation/musickit/partialmusicproperty/recordlabels)

An identifier for the relationship property that returns the record labels for the album.

[`static let relatedAlbums: MusicRelationshipProperty<Album, Album>`](/documentation/musickit/partialmusicproperty/relatedalbums)

An identifier for the association property that returns a collection of related albums.

[`static let relatedVideos: MusicRelationshipProperty<Album, MusicVideo>`](/documentation/musickit/partialmusicproperty/relatedvideos)

An identifier for the association property that returns a collection of related music videos for the album.

[`static let similarArtists: MusicRelationshipProperty<Artist, Artist>`](/documentation/musickit/partialmusicproperty/similarartists)

An identifier for the association property that returns a collection of artists similar to this artist.

[`static let singles: MusicRelationshipProperty<Artist, Album>`](/documentation/musickit/partialmusicproperty/singles)

An identifier of the association property that returns a collection of the artist’s albums in the *singles* category.

[`static let songs: MusicRelationshipProperty<MusicVideo, Song>`](/documentation/musickit/partialmusicproperty/songs)

An identifier of the relationship property that returns the associated songs for the music video.

[`static let station: MusicRelationshipProperty<Song, Station>`](/documentation/musickit/partialmusicproperty/station-8u1rf)

An identifier for the relationship property that returns the associated station for the song.

[`static let station: MusicRelationshipProperty<Artist, Station>`](/documentation/musickit/partialmusicproperty/station-8zftf)

An identifier for the relationship property that returns the associated station for the artist.

[`static let topMusicVideos: MusicRelationshipProperty<Artist, MusicVideo>`](/documentation/musickit/partialmusicproperty/topmusicvideos)

An identifier for the association property that returns a collection of the artist’s top music videos.

[`static var topReleases: MusicRelationshipProperty<RecordLabel, Album>`](/documentation/musickit/partialmusicproperty/topreleases)

An identifier for the association property that returns a collection of top releases for the record label.

[`static let topSongs: MusicRelationshipProperty<Artist, Song>`](/documentation/musickit/partialmusicproperty/topsongs)

An identifier for the association property that returns a collection of the artist’s top songs.

[`static let tracks: MusicRelationshipProperty<Playlist, Track>`](/documentation/musickit/partialmusicproperty/tracks-8mq2j)

An identifier for the relationship property that returns the tracks in the playlist.

[`static let tracks: MusicRelationshipProperty<Album, Track>`](/documentation/musickit/partialmusicproperty/tracks-9mk2l)

An identifier for the relationship property that returns the tracks on the album.

## [Relationships](/documentation/musickit/partialmusicproperty#relationships)

### [Inherits From](/documentation/musickit/partialmusicproperty#inherits-from)

- [`AnyMusicProperty`](/documentation/musickit/anymusicproperty)

### [Inherited By](/documentation/musickit/partialmusicproperty#inherited-by)

- [`MusicAttributeProperty`](/documentation/musickit/musicattributeproperty)
- [`PartialMusicAsyncProperty`](/documentation/musickit/partialmusicasyncproperty)

### [Conforms To](/documentation/musickit/partialmusicproperty#conforms-to)

- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/partialmusicproperty#see-also)

### [Utility](/documentation/musickit/partialmusicproperty#Utility)

[`protocol MusicItem`](/documentation/musickit/musicitem)

A protocol with basic requirements for music items.

[`struct MusicItemID`](/documentation/musickit/musicitemid)

An object that represents a unique identifier for a music item.

[`struct MusicItemCollection`](/documentation/musickit/musicitemcollection)

A collection of music items.

[`protocol MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)

A protocol for music items that allow loading additional properties that you can fetch asynchronously.

[`class MusicRelationshipProperty`](/documentation/musickit/musicrelationshipproperty)

An identifier for a music item relationship property from a specific root type to a specific value type for the element of the resulting collection.

[`class MusicExtendedAttributeProperty`](/documentation/musickit/musicextendedattributeproperty)

An identifier for a music item extended attribute property from a specific root type to a specific resulting value type.

[`class MusicAttributeProperty`](/documentation/musickit/musicattributeproperty)

An identifier for a music item attribute property from a specific root type to a specific resulting value type.

[`class PartialMusicAsyncProperty`](/documentation/musickit/partialmusicasyncproperty)

A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.

[`class AnyMusicProperty`](/documentation/musickit/anymusicproperty)

A type-erased identifier for a music item property, from any root type to any resulting value type.
