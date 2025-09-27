# Catalog Charts APIs

> Source: Multiple Apple MusicKit documentation pages

The Catalog Charts APIs provide access to popular and trending music content from the Apple Music catalog. These APIs enable developers to fetch chart data including most played items, global top charts, and city-specific top charts across different music types and genres.

## MusicCatalogChartsRequest

- **Swift Declaration**: `struct MusicCatalogChartsRequest`
- **Purpose**: A request that your app uses to fetch the most popular items in the Apple Music catalog.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogchartsrequest)
- **Availability**: iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

### Initializers

- `init(genre: Genre?, kinds: [MusicCatalogChartKind], types: [any MusicCatalogChartRequestable.Type])` - Creates a catalog charts request for a specified genre and list of types to include in the catalog charts response.

### Properties

- `var genre: Genre?` - The genre for the request.
- `var kinds: [MusicCatalogChartKind]` - The kinds of requested catalog charts.
- `var limit: Int?` - A limit for the number of items to return in the catalog search response.
- `var offset: Int?` - An offset for the request.
- `var types: [any MusicCatalogChartRequestable.Type]` - The list of requested types for the catalog charts response.

### Methods

- `func response() async throws -> MusicCatalogChartsResponse` - Fetches the most popular items of the requested types that match the genre and kinds for the request.

### Conforms To

- `Equatable`, `Hashable`, `Sendable`, `SendableMetatype`

## MusicCatalogChartsResponse

- **Swift Declaration**: `struct MusicCatalogChartsResponse`
- **Purpose**: An object that contains results for a catalog charts request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogchartsresponse)
- **Availability**: iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

### Properties

- `let albumCharts: [MusicCatalogChart<Album>]` - A collection of charts that contain albums.
- `let musicVideoCharts: [MusicCatalogChart<MusicVideo>]` - A collection of charts that contain music videos.
- `let playlistCharts: [MusicCatalogChart<Playlist>]` - A collection of charts that contain playlists.
- `let songCharts: [MusicCatalogChart<Song>]` - A collection of charts that contain songs.

### Conforms To

- `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`, `SendableMetatype`

## MusicCatalogChart

- **Swift Declaration**: `struct MusicCatalogChart<MusicItemType> where MusicItemType : MusicCatalogChartRequestable`
- **Purpose**: An object that contains popular items in the Apple Music catalog.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogchart)
- **Availability**: iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

### Properties

- `let id: String` - The unique identifier for the catalog chart.
- `let items: MusicItemCollection<MusicItemType>` - The items for the catalog chart.
- `let kind: MusicCatalogChartKind` - The kind of catalog chart.
- `let title: String` - The title for the catalog chart.

### Conforms To

- `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Identifiable`, `Sendable`, `SendableMetatype`

## MusicCatalogChartKind

- **Swift Declaration**: `enum MusicCatalogChartKind`
- **Purpose**: The available kinds of catalog charts.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogchartkind)
- **Availability**: iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

### Enumeration Cases

- `case cityTop` - City-specific top charts showing popular content in specific cities.
- `case dailyGlobalTop` - Daily global top charts showing worldwide popular content updated daily.
- `case mostPlayed` - Charts showing the most played content across the platform.

### Conforms To

- `CaseIterable`, `Copyable`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`, `SendableMetatype`

## Related Types

### MusicCatalogChartRequestable

A protocol that defines music item types that can be included in catalog charts requests. This protocol is implemented by various MusicKit types to enable them to be fetched through the charts APIs.

## Usage Patterns

### Basic Charts Request

```swift
// Fetch most played songs globally
let request = MusicCatalogChartsRequest(
    genre: nil,
    kinds: [.mostPlayed],
    types: [Song.self]
)
let response = try await request.response()
```

### Genre-Specific Charts

```swift
// Fetch daily global top albums for rock genre
let request = MusicCatalogChartsRequest(
    genre: rockGenre,
    kinds: [.dailyGlobalTop],
    types: [Album.self]
)
let response = try await request.response()
```

### Multi-Type Charts

```swift
// Fetch city top charts for multiple content types
let request = MusicCatalogChartsRequest(
    genre: nil,
    kinds: [.cityTop],
    types: [Song.self, Album.self, Playlist.self]
)
let response = try await request.response()
```

### Accessing Chart Results

```swift
let response = try await request.response()

// Access different chart types
for chart in response.songCharts {
    print("Chart: \(chart.title) (Kind: \(chart.kind))")
    for song in chart.items {
        print("- \(song.title)")
    }
}

for chart in response.albumCharts {
    print("Album Chart: \(chart.title)")
    for album in chart.items {
        print("- \(album.title) by \(album.artistName)")
    }
}
```

## Cross-References

- [`MusicCatalogSearchRequest`](CatalogSearchAPI.md#musiccatalogsearchrequest) - For search-based catalog queries
- [`MusicCatalogResourceRequest`](CatalogResourceAPI.md#musiccatalogresourcerequest) - For filtered catalog queries
- [`MusicItemCollection`](../utilities/CoreDataTypes.md#musicitemcollection) - Used for containing chart items
- [`Genre`](../core-types/Genre.md) - For genre-specific chart filtering
- [`Album`](../core-types/Album.md), [`Song`](../core-types/Song.md), [`Playlist`](../core-types/Playlist.md), [`MusicVideo`](../core-types/MusicVideo.md) - Chart item types