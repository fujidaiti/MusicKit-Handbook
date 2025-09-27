# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicvideofilter

- [MusicKit](/documentation/musickit)
- MusicVideoFilter

Protocol

# MusicVideoFilter

Music video properties your app uses as a filter for a catalog resource request.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
protocol MusicVideoFilter
```

## [Topics](/documentation/musickit/musicvideofilter#topics)

### [Instance Properties](/documentation/musickit/musicvideofilter#Instance-Properties)

[`var id: MusicItemID`](/documentation/musickit/musicvideofilter/id)

The unique identifier for the music video.

**Required**

[`var isrc: String?`](/documentation/musickit/musicvideofilter/isrc)

The International Standard Recording Code (ISRC) for the music video.

**Required**

## [See Also](/documentation/musickit/musicvideofilter#see-also)

### [Resource Loading Using Filters](/documentation/musickit/musicvideofilter#Resource-Loading-Using-Filters)

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

[`protocol FilterableMusicItem`](/documentation/musickit/filterablemusicitem)

A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.
