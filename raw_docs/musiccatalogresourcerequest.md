# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogresourcerequest

- [MusicKit](/documentation/musickit)
- MusicCatalogResourceRequest

Structure

# MusicCatalogResourceRequest

A request that your app uses to fetch items from the Apple Music catalog using a filter.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicCatalogResourceRequest<MusicItemType> where MusicItemType : MusicItem, MusicItemType : Decodable
```

## [Topics](/documentation/musickit/musiccatalogresourcerequest#topics)

### [Initializers](/documentation/musickit/musiccatalogresourcerequest#Initializers)

[`init()`](/documentation/musickit/musiccatalogresourcerequest/init())

Creates a request to fetch top-level items in the Apple Music catalog.

[`init<Value>(matching: KeyPath<MusicItemType.FilterType, Value>, equalTo: Value)`](/documentation/musickit/musiccatalogresourcerequest/init(matching:equalto:))

Creates a request to fetch items using a filter that matches a specific value.

[`init<Value>(matching: KeyPath<MusicItemType.FilterType, Value>, memberOf: [Value])`](/documentation/musickit/musiccatalogresourcerequest/init(matching:memberof:))

Creates a request to fetch items using a filter that matches any value from an array of possible values.

### [Instance Properties](/documentation/musickit/musiccatalogresourcerequest#Instance-Properties)

[`var limit: Int?`](/documentation/musickit/musiccatalogresourcerequest/limit)

A limit for the number of items to return in the catalog resource response.

[`var properties: [PartialMusicAsyncProperty<MusicItemType>]`](/documentation/musickit/musiccatalogresourcerequest/properties)

A list of properties which the resource request will fetch for each music item in the response.

### [Instance Methods](/documentation/musickit/musiccatalogresourcerequest#Instance-Methods)

[`func response() async throws -> MusicCatalogResourceResponse<MusicItemType>`](/documentation/musickit/musiccatalogresourcerequest/response())

Fetches items from the Apple Music catalog that match a specific filter.

## [Relationships](/documentation/musickit/musiccatalogresourcerequest#relationships)

### [Conforms To](/documentation/musickit/musiccatalogresourcerequest#conforms-to)

- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/musiccatalogresourcerequest#see-also)

### [Resource Loading Using Filters](/documentation/musickit/musiccatalogresourcerequest#Resource-Loading-Using-Filters)

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

[`protocol FilterableMusicItem`](/documentation/musickit/filterablemusicitem)

A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.
