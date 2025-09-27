# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogresourceresponse

- [MusicKit](/documentation/musickit)
- MusicCatalogResourceResponse

Structure

# MusicCatalogResourceResponse

An object that contains results for a catalog resource request.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicCatalogResourceResponse<MusicItemType> where MusicItemType : MusicItem
```

## [Topics](/documentation/musickit/musiccatalogresourceresponse#topics)

### [Instance Properties](/documentation/musickit/musiccatalogresourceresponse#Instance-Properties)

[`let items: MusicItemCollection<MusicItemType>`](/documentation/musickit/musiccatalogresourceresponse/items)

A collection of items matching the filter used in the originating [`MusicCatalogResourceRequest`](/documentation/musickit/musiccatalogresourcerequest).

## [Relationships](/documentation/musickit/musiccatalogresourceresponse#relationships)

### [Conforms To](/documentation/musickit/musiccatalogresourceresponse#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/musiccatalogresourceresponse#see-also)

### [Resource Loading Using Filters](/documentation/musickit/musiccatalogresourceresponse#Resource-Loading-Using-Filters)

[`struct MusicCatalogResourceRequest`](/documentation/musickit/musiccatalogresourcerequest)

A request that your app uses to fetch items from the Apple Music catalog using a filter.

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

[`protocol FilterableMusicItem`](/documentation/musickit/filterablemusicitem)

A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.
