# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/filterablemusicitem

- [MusicKit](/documentation/musickit)
- FilterableMusicItem

Protocol

# FilterableMusicItem

A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
protocol FilterableMusicItem : MusicItem
```

## [Topics](/documentation/musickit/filterablemusicitem#topics)

### [Associated Types](/documentation/musickit/filterablemusicitem#Associated-Types)

[`associatedtype FilterType`](/documentation/musickit/filterablemusicitem/filtertype)

The associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.

**Required**

## [Relationships](/documentation/musickit/filterablemusicitem#relationships)

### [Inherits From](/documentation/musickit/filterablemusicitem#inherits-from)

- [`MusicItem`](/documentation/musickit/musicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

### [Conforming Types](/documentation/musickit/filterablemusicitem#conforming-types)

- [`Album`](/documentation/musickit/album)
- [`Artist`](/documentation/musickit/artist)
- [`Curator`](/documentation/musickit/curator)
- [`Genre`](/documentation/musickit/genre)
- [`MusicVideo`](/documentation/musickit/musicvideo)
- [`Playlist`](/documentation/musickit/playlist)
- [`RadioShow`](/documentation/musickit/radioshow)
- [`RecordLabel`](/documentation/musickit/recordlabel)
- [`Song`](/documentation/musickit/song)
- [`Station`](/documentation/musickit/station)

## [See Also](/documentation/musickit/filterablemusicitem#see-also)

### [Resource Loading Using Filters](/documentation/musickit/filterablemusicitem#Resource-Loading-Using-Filters)

[`struct MusicCatalogResourceRequest`](/documentation/musickit/musiccatalogresourcerequest)

A request that your app uses to fetch items from the Apple Music catalog using a filter.

[`struct MusicCatalogResourceResponse`](/documentation/musickit/musiccatalogresourceresponse)

An object that contains results for a catalog resource request.

[`protocol AlbumFilter`](/documentation/musickit/albumfilter)

Album properties your app uses as a filter for a catalog resource request.

[`protocol ArtistFilter`](/documentation/musickit/artistfilter)

Artist properties your app uses as a filter for a catalog resource request.

[`protocol CuratorFilter`](/documentation/musickit/curatorfilter)

Curator properties your app uses as a filter for a catalog resource request.

[`protocol GenreFilter`](/documentation/musickit/genrefilter)

Genre properties your app uses as a filter for a catalog resource request.

[`protocol MusicVideoFilter`](/documentation/musickit/musicvideofilter)

Music video properties your app uses as a filter for a catalog resource request.

[`protocol PlaylistFilter`](/documentation/musickit/playlistfilter)

Playlist properties your app uses as a filter for a catalog resource request.

[`protocol RadioShowFilter`](/documentation/musickit/radioshowfilter)

Radio Show properties your app uses as a filter for a catalog resource request.

[`protocol RecordLabelFilter`](/documentation/musickit/recordlabelfilter)

The set of record label properties your app uses as a filter for a catalog resource request.

[`protocol SongFilter`](/documentation/musickit/songfilter)

Song properties your app uses as a filter for a catalog resource request.

[`protocol StationFilter`](/documentation/musickit/stationfilter)

The set of station properties your app uses as a filter for a catalog resource request.
