# Catalog Resource APIs

> Source: Multiple Apple MusicKit documentation pages

The Catalog Resource APIs provide filtered access to Apple Music catalog items using specific criteria. These APIs enable developers to fetch music items based on various filter properties, offering more targeted and precise queries compared to search-based approaches.

## MusicCatalogResourceRequest

- **Swift Declaration**: `struct MusicCatalogResourceRequest<MusicItemType> where MusicItemType : MusicItem, MusicItemType : Decodable`
- **Purpose**: A request that your app uses to fetch items from the Apple Music catalog using a filter.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogresourcerequest)
- **Availability**: iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

### Initializers

- `init()` - Creates a request to fetch top-level items in the Apple Music catalog.
- `init<Value>(matching: KeyPath<MusicItemType.FilterType, Value>, equalTo: Value)` - Creates a request to fetch items using a filter that matches a specific value.
- `init<Value>(matching: KeyPath<MusicItemType.FilterType, Value>, memberOf: [Value])` - Creates a request to fetch items using a filter that matches any value from an array of possible values.

### Properties

- `var limit: Int?` - A limit for the number of items to return in the catalog resource response.
- `var properties: [PartialMusicAsyncProperty<MusicItemType>]` - A list of properties which the resource request will fetch for each music item in the response.

### Methods

- `func response() async throws -> MusicCatalogResourceResponse<MusicItemType>` - Fetches items from the Apple Music catalog that match a specific filter.

### Conforms To

- `Sendable`, `SendableMetatype`

## MusicCatalogResourceResponse

- **Swift Declaration**: `struct MusicCatalogResourceResponse<MusicItemType> where MusicItemType : MusicItem`
- **Purpose**: An object that contains results for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogresourceresponse)
- **Availability**: iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

### Properties

- `let items: MusicItemCollection<MusicItemType>` - A collection of items matching the filter used in the originating `MusicCatalogResourceRequest`.

### Conforms To

- `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`, `SendableMetatype`

## Related Filter Protocols

The Catalog Resource API works with various filter protocols that define the properties available for filtering different types of music items:

### AlbumFilter

Album properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/albumfilter)

### ArtistFilter

Artist properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/artistfilter)

### CuratorFilter

Curator properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/curatorfilter)

### GenreFilter

Genre properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/genrefilter)

### MusicVideoFilter

Music video properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musicvideofilter)

### PlaylistFilter

Playlist properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/playlistfilter)

### RadioShowFilter

Radio Show properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/radioshowfilter)

### RecordLabelFilter

The set of record label properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/recordlabelfilter)

### SongFilter

Song properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/songfilter)

### StationFilter

The set of station properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/stationfilter)

### FilterableMusicItem

A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/filterablemusicitem)

## Usage Patterns

### Basic Resource Fetching

```swift
// Fetch all albums
let request = MusicCatalogResourceRequest<Album>()
let response = try await request.response()
```

### Filtered Resource Fetching

```swift
// Fetch albums by specific artist ID
let request = MusicCatalogResourceRequest<Album>(
    matching: \.id,
    equalTo: "specific-artist-id"
)
let response = try await request.response()
```

### Multiple Value Filtering

```swift
// Fetch albums matching multiple genre IDs
let genreIds = ["rock", "pop", "jazz"]
let request = MusicCatalogResourceRequest<Album>(
    matching: \.genres,
    memberOf: genreIds
)
let response = try await request.response()
```

## Cross-References

- [`MusicCatalogSearchRequest`](CatalogSearchAPI.md#musiccatalogsearchrequest) - For search-based catalog queries
- [`MusicCatalogChartsRequest`](CatalogChartsAPI.md#musiccatalogchartsrequest) - For fetching popular items and charts
- [`MusicItemCollection`](../utilities/CoreDataTypes.md#musicitemcollection) - Used for containing resource results
- [`MusicItem`](../protocols/UtilityProtocols.md#musicitem) - Base protocol for all music items returned in resource requests
- [`PartialMusicAsyncProperty`](../utilities/PropertyManagement.md#partialmusicasyncproperty) - For specifying which properties to fetch