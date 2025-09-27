# Filter Protocols

> Source: Multiple Apple MusicKit documentation pages

Filter protocols define properties that can be used to filter music items when making catalog and library requests.

## Overview

MusicKit provides two main categories of filter protocols:
- **Catalog Filters**: For filtering items from the Apple Music catalog
- **Library Filters**: For filtering items from the user's personal music library

All filter protocols work in conjunction with [`MusicCatalogResourceRequest`](../api-layer/CatalogResourceAPI.md#musiccatalogresourcerequest) and [`MusicLibraryResourceRequest`](../api-layer/LibraryAPI.md#musiclibraryrequest) to enable targeted queries for specific music content.

## Base Filter Protocol

### FilterableMusicItem

A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.

```swift
protocol FilterableMusicItem : MusicItem
```

#### Associated Types

- `associatedtype FilterType` - The associated type that contains the set of music item properties your app uses as a filter for a catalog resource request. **Required**

#### Inherits From
- [`MusicItem`](UtilityProtocols.md#musicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

#### Conforming Types
- [`Album`](../core-types/Album.md)
- [`Artist`](../core-types/Artist.md)
- [`Curator`](../core-types/Curator.md)
- [`Genre`](../core-types/Genre.md)
- [`MusicVideo`](../core-types/MusicVideo.md)
- [`Playlist`](../core-types/Playlist.md)
- [`RadioShow`](../core-types/RadioShow.md)
- [`RecordLabel`](../core-types/RecordLabel.md)
- [`Song`](../core-types/Song.md)
- [`Station`](../core-types/Station.md)

## Catalog Filter Protocols

### AlbumFilter

Album properties your app uses as a filter for a catalog resource request.

```swift
protocol AlbumFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the album. **Required**
- `var upc: String?` - The universal product code (UPC) for the album. **Required**

### ArtistFilter

Artist properties your app uses as a filter for a catalog resource request.

```swift
protocol ArtistFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the artist. **Required**

### CuratorFilter

Curator properties your app uses as a filter for a catalog resource request.

```swift
protocol CuratorFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the curator. **Required**

### GenreFilter

Genre properties your app uses as a filter for a catalog resource request.

```swift
protocol GenreFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the genre. **Required**

### MusicVideoFilter

Music video properties your app uses as a filter for a catalog resource request.

```swift
protocol MusicVideoFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the music video. **Required**
- `var isrc: String?` - The International Standard Recording Code (ISRC) for the music video. **Required**

### PlaylistFilter

Playlist properties your app uses as a filter for a catalog resource request.

```swift
protocol PlaylistFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the playlist. **Required**

### RadioShowFilter

Radio Show properties your app uses as a filter for a catalog resource request.

```swift
protocol RadioShowFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the radio show. **Required**

### RecordLabelFilter

The set of record label properties your app uses as a filter for a catalog resource request.

```swift
protocol RecordLabelFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the record label. **Required**

### SongFilter

Song properties your app uses as a filter for a catalog resource request.

```swift
protocol SongFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the song. **Required**
- `var isrc: String?` - The International Standard Recording Code (ISRC) for the song. **Required**

### StationFilter

The set of station properties your app uses as a filter for a catalog resource request.

```swift
protocol StationFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the station. **Required**

## Library Filter Protocols

### LibraryAlbumFilter

Album properties your app uses as a filter for a library request.

```swift
protocol LibraryAlbumFilter
```

#### Instance Properties

- `var artistName: String` - The artist's name. **Required**
- `var artists: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Artist>?` - The album's associated artists. **Required**
- `var genres: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Genre>?` - The genres for the album. **Required**
- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the album. **Required**
- `var isCompilation: Bool?` - A Boolean value that indicates whether the album is a compilation. **Required**
- `var title: String` - The title of the album. **Required**

### LibraryArtistFilter

Artist properties your app uses as a filter for a library request.

```swift
protocol LibraryArtistFilter
```

#### Instance Properties

- `var genres: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Genre>?` - The artist's associated genres. **Required**
- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the artist. **Required**
- `var name: String` - The name of the artist. **Required**
- `var playlists: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Playlist>?` - The artist's associated playlists. **Required**

### LibraryGenreFilter

Genre properties your app uses as a filter for a library request.

```swift
protocol LibraryGenreFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the genre. **Required**
- `var name: String` - The localized name of the genre. **Required**

### LibraryMusicVideoFilter

Music video properties your app uses as a filter for a library request.

```swift
protocol LibraryMusicVideoFilter
```

#### Instance Properties

- `var albumTitle: String?` - The title of the album the music video appears on. **Required**
- `var albums: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Album>?` - The music video's associated albums. **Required**
- `var artistName: String?` - The artist's name. **Required**
- `var artists: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Artist>?` - The music video's associated artists. **Required**
- `var genres: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Genre>?` - The music video's associated genres. **Required**
- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the music video. **Required**
- `var title: String` - The title of the music video. **Required**

### LibraryPlaylistEntryFilter

Playlist entry properties your app uses as a filter for a library request.

```swift
protocol LibraryPlaylistEntryFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the playlist entry. **Required**

### LibraryPlaylistFilter

Playlist properties your app uses as a filter for a library request.

```swift
protocol LibraryPlaylistFilter
```

#### Instance Properties

- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the playlist. **Required**
- `var name: String` - The name of the playlist. **Required**

### LibrarySongFilter

Song properties your app uses as a filter for a library request.

```swift
protocol LibrarySongFilter
```

#### Instance Properties

- `var albumTitle: String?` - The title of the album the song appears on. **Required**
- `var albums: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Album>?` - The song's associated albums. **Required**
- `var artistName: String?` - The artist's name. **Required**
- `var artists: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Artist>?` - The song's associated artists. **Required**
- `var composerName: String?` - The name of the song's composer. **Required**
- `var genres: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Genre>?` - The song's associated genres. **Required**
- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the song. **Required**
- `var title: String` - The title of the song. **Required**

### LibraryTrackFilter

Track properties your app uses as a filter for a library request.

```swift
protocol LibraryTrackFilter
```

#### Instance Properties

- `var albumTitle: String?` - The title of the album the track appears on. **Required**
- `var albums: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Album>?` - The track's associated albums. **Required**
- `var artistName: String?` - The artist's name. **Required**
- `var artists: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Artist>?` - The track's associated artists. **Required**
- `var genres: [MusicItemCollection](../utilities/CoreDataTypes.md#musicitemcollection)<Genre>?` - The track's associated genres. **Required**
- `var id: [MusicItemID](../utilities/CoreDataTypes.md#musicitemid)` - The unique identifier for the track. **Required**
- `var title: String` - The title of the track. **Required**

## See Also

### Resource Loading Using Filters

- [`struct MusicCatalogResourceRequest`](../api-layer/CatalogResourceAPI.md#musiccatalogresourcerequest) - A request that your app uses to fetch items from the Apple Music catalog using a filter.
- [`struct MusicCatalogResourceResponse`](../api-layer/CatalogResourceAPI.md#musiccatalogresourceresponse) - An object that contains results for a catalog resource request.
- [`struct MusicLibraryResourceRequest`](../api-layer/LibraryAPI.md#musiclibraryrequest) - A request that your app uses to fetch items from the user's music library using a filter.
- [`struct MusicLibraryResourceResponse`](../api-layer/LibraryAPI.md#musiclibraryresponse) - An object that contains results for a library resource request.

## Related Documentation

- [Apple MusicKit FilterableMusicItem](https://developer.apple.com/documentation/musickit/filterablemusicitem)
- [Apple MusicKit AlbumFilter](https://developer.apple.com/documentation/musickit/albumfilter)
- [Apple MusicKit ArtistFilter](https://developer.apple.com/documentation/musickit/artistfilter)
- [Apple MusicKit CuratorFilter](https://developer.apple.com/documentation/musickit/curatorfilter)
- [Apple MusicKit GenreFilter](https://developer.apple.com/documentation/musickit/genrefilter)
- [Apple MusicKit MusicVideoFilter](https://developer.apple.com/documentation/musickit/musicvideofilter)
- [Apple MusicKit PlaylistFilter](https://developer.apple.com/documentation/musickit/playlistfilter)
- [Apple MusicKit RadioShowFilter](https://developer.apple.com/documentation/musickit/radioshowfilter)
- [Apple MusicKit RecordLabelFilter](https://developer.apple.com/documentation/musickit/recordlabelfilter)
- [Apple MusicKit SongFilter](https://developer.apple.com/documentation/musickit/songfilter)
- [Apple MusicKit StationFilter](https://developer.apple.com/documentation/musickit/stationfilter)
- [Apple MusicKit LibraryAlbumFilter](https://developer.apple.com/documentation/musickit/libraryalbumfilter)
- [Apple MusicKit LibraryArtistFilter](https://developer.apple.com/documentation/musickit/libraryartistfilter)
- [Apple MusicKit LibraryGenreFilter](https://developer.apple.com/documentation/musickit/librarygenrefilter)
- [Apple MusicKit LibraryMusicVideoFilter](https://developer.apple.com/documentation/musickit/librarymusicvideofilter)
- [Apple MusicKit LibraryPlaylistEntryFilter](https://developer.apple.com/documentation/musickit/libraryplaylistentryfilter)
- [Apple MusicKit LibraryPlaylistFilter](https://developer.apple.com/documentation/musickit/libraryplaylistfilter)
- [Apple MusicKit LibrarySongFilter](https://developer.apple.com/documentation/musickit/librarysongfilter)
- [Apple MusicKit LibraryTrackFilter](https://developer.apple.com/documentation/musickit/librarytrackfilter)