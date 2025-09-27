# Catalog Search APIs

> Source: Multiple Apple MusicKit documentation pages

The Catalog Search APIs provide comprehensive search functionality for the Apple Music catalog, including basic search capabilities and search suggestions. These APIs allow developers to search for various types of music content and retrieve structured results with detailed information.

## MusicCatalogSearchRequest

- **Swift Declaration**: `struct MusicCatalogSearchRequest`
- **Purpose**: A request that your app uses to fetch items from the Apple Music catalog using a search term.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogsearchrequest)
- **Availability**: iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

### Initializers

- `init(term: String, types: [any MusicCatalogSearchable.Type])` - Creates a catalog search request for a specified search term and list of catalog searchable types.

### Properties

- `var includeTopResults: Bool` - A Boolean value that indicates whether to request top search results.
- `var limit: Int?` - A limit for the number of items to return in the catalog search response.
- `var offset: Int?` - An offset for the request.
- `let term: String` - The search term for the request.
- `var types: [any MusicCatalogSearchable.Type]` - The list of requested catalog searchable types.

### Methods

- `func response() async throws -> MusicCatalogSearchResponse` - Fetches items of the requested catalog searchable types that match the search term of the request.

## MusicCatalogSearchResponse

- **Swift Declaration**: `struct MusicCatalogSearchResponse`
- **Purpose**: An object that contains results for a catalog search request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogsearchresponse)
- **Availability**: iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

### Properties

- `let albums: MusicItemCollection<Album>` - A collection of albums.
- `let artists: MusicItemCollection<Artist>` - A collection of artists.
- `let curators: MusicItemCollection<Curator>` - A collection of curators.
- `let musicVideos: MusicItemCollection<MusicVideo>` - A collection of music videos.
- `let playlists: MusicItemCollection<Playlist>` - A collection of playlists.
- `let radioShows: MusicItemCollection<RadioShow>` - A collection of radio shows.
- `let recordLabels: MusicItemCollection<RecordLabel>` - A collection of record labels.
- `let songs: MusicItemCollection<Song>` - A collection of songs.
- `let stations: MusicItemCollection<Station>` - A collection of stations.
- `let topResults: MusicItemCollection<MusicCatalogSearchResponse.TopResult>` - A collection of top results.

### Conforms To

- `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`

## MusicCatalogSearchResponse.TopResult

- **Swift Declaration**: `enum TopResult`
- **Purpose**: An item that represents one of the top results in a catalog search response.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogsearchresponse/topresult)
- **Availability**: iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

### Enumeration Cases

- `case album(Album)` - An item that corresponds to an album.
- `case artist(Artist)` - An item that corresponds to an artist.
- `case curator(Curator)` - An item that corresponds to a curator.
- `case musicVideo(MusicVideo)` - An item that corresponds to a music video.
- `case playlist(Playlist)` - An item that corresponds to a playlist.
- `case radioShow(RadioShow)` - An item that corresponds to a radio show.
- `case recordLabel(RecordLabel)` - An item that corresponds to a record label.
- `case song(Song)` - An item that corresponds to a song.
- `case station(Station)` - An item that corresponds to a station.

### Properties

- `var artwork: Artwork?` - The artwork of this top result for catalog search.
- `var id: MusicItemID` - The unique identifier of this top result for catalog search.
- `var title: String` - The title of this top result for catalog search.

### Conforms To

- `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Identifiable`, `MusicItem`, `Sendable`, `SendableMetatype`

## MusicCatalogSearchSuggestionsRequest

- **Swift Declaration**: `struct MusicCatalogSearchSuggestionsRequest`
- **Purpose**: A request that your app uses to fetch suggestions from the Apple Music catalog using a search term.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsrequest)
- **Availability**: iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

### Initializers

- `init(term: String, includingTopResultsOfTypes: [any MusicCatalogSearchable.Type])` - Creates a catalog search suggestions request for a specified search term along with a list of types to include when fetching top results.

### Properties

- `var limit: Int?` - A limit for the number of items to return in the catalog search suggestions response.
- `let term: String` - The search term for the request.
- `var typesForTopResults: [any MusicCatalogSearchable.Type]` - The list of requested types for top results.

### Methods

- `func response() async throws -> MusicCatalogSearchSuggestionsResponse` - Fetches suggestions of the requested catalog searchable types that match the search term of the request.

## MusicCatalogSearchSuggestionsResponse

- **Swift Declaration**: `struct MusicCatalogSearchSuggestionsResponse`
- **Purpose**: An object that contains results for a catalog search suggestions request.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsresponse)
- **Availability**: iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

### Properties

- `let suggestions: [MusicCatalogSearchSuggestionsResponse.Suggestion]` - A collection of suggested terms.
- `let topResults: MusicItemCollection<MusicCatalogSearchSuggestionsResponse.TopResult>` - A collection of top results.

### Type Aliases

- `typealias TopResult` - A type alias for an item that represents one of the top results in a catalog search suggestions response.

### Conforms To

- `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Sendable`, `SendableMetatype`

## MusicCatalogSearchSuggestionsResponse.Suggestion

- **Swift Declaration**: `struct Suggestion`
- **Purpose**: An item that represents a suggestion in the search suggestions response.
- **Source**: [Apple Developer Documentation](https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsresponse/suggestion)
- **Availability**: iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+

### Properties

- `let displayTerm: String` - A term to display to the user to select from.
- `var id: String` - The unique identifier for the suggestion.
- `let searchTerm: String` - The term to use as a search input when using this suggestion.

### Conforms To

- `Copyable`, `CustomDebugStringConvertible`, `CustomStringConvertible`, `Decodable`, `Encodable`, `Equatable`, `Hashable`, `Identifiable`, `Sendable`, `SendableMetatype`

## Related Types

### MusicCatalogSearchable

A protocol for music items that your app can fetch by using a catalog search request. This protocol is implemented by various MusicKit types to enable them to be searched through the catalog search APIs.

## Cross-References

- [`MusicCatalogResourceRequest`](CatalogResourceAPI.md#musiccatalogresourcerequest) - For resource-based catalog queries
- [`MusicCatalogChartsRequest`](CatalogChartsAPI.md#musiccatalogchartsrequest) - For fetching popular items and charts
- [`MusicItemCollection`](../utilities/CoreDataTypes.md#musicitemcollection) - Used for containing search results
- [`MusicItem`](../protocols/UtilityProtocols.md#musicitem) - Base protocol for all music items returned in searches