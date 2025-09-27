# Library API

> Source: Multiple Apple MusicKit documentation pages

The Library API provides functionality for accessing and searching the user's personal music library. It includes request types for fetching, searching, and organizing library content, along with their corresponding response types.

## MusicLibraryRequest

- **Swift Declaration**: `struct MusicLibraryRequest<MusicItemType> where MusicItemType : MusicLibraryRequestable`
- **Purpose**: A request that your app uses to fetch items from the user's music library.
- **Source**: https://developer.apple.com/documentation/musickit/musiclibraryrequest

### Properties

- `var includeOnlyDownloadedContent: Bool` - A Boolean value that indicates whether the library response should only include items downloaded on the user's device.
- `var limit: Int` - A limit for the number of items to return in the library response.
- `var offset: Int` - An offset for the request.

### Methods

#### Initializers
- `init()` - Creates a request to fetch items from the library.

#### Filtering Methods
- `func filter(matching: KeyPath<MusicItemType.LibraryFilter, String?>, contains: String)` - Filters items by a given optional property that contains a specific string.
- `func filter(matching: KeyPath<MusicItemType.LibraryFilter, String>, contains: String)` - Filters items by a given property that contains a specific string.
- `func filter<RelatedMusicItemType>(matching: KeyPath<MusicItemType.LibraryFilter, MusicItemCollection<RelatedMusicItemType>?>, contains: RelatedMusicItemType)` - Filters items by a given relationship that matches a specific value.
- `func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, equalTo: Value)` - Filters items by a given property that matches a specific value.
- `func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, equalTo: Value?)` - Filters items by a given optional property that matches a specific value.
- `func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, memberOf: [Value?])` - Filters items by an optional property for an array of possible values.
- `func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, memberOf: [Value])` - Filters items by a property for an array of possible values.
- `func filter(text: String)` - Filters items by a specific string.

#### Sorting Methods
- `func sort<Value>(by: KeyPath<MusicItemType.LibrarySortProperties, Value>, ascending: Bool)` - Sorts items by a specified property.

#### Response Method
- `func response() async throws -> MusicLibraryResponse<MusicItemType>` - Fetches items from the user's music library.

## MusicLibraryResponse

- **Swift Declaration**: `struct MusicLibraryResponse<MusicItemType> where MusicItemType : MusicItem`
- **Purpose**: An object that contains results for a library request.
- **Source**: https://developer.apple.com/documentation/musickit/musiclibraryresponse

### Properties

- `let items: MusicItemCollection<MusicItemType>` - A collection of items that match the filters on the originating library request.

### Conformances

- `Copyable`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `Sendable`
- `SendableMetatype`

## MusicLibrarySearchRequest

- **Swift Declaration**: `struct MusicLibrarySearchRequest`
- **Purpose**: A request that your app uses to fetch items from user's library using a search term.
- **Source**: https://developer.apple.com/documentation/musickit/musiclibrarysearchrequest

### Properties

- `var includeTopResults: Bool` - A Boolean value that indicates whether to request top search results.
- `var limit: Int` - A limit for the number of items to return in the library search response.
- `let term: String` - The search term for the request.
- `var types: [any MusicLibrarySearchable.Type]` - The list of requested library searchable types.

### Methods

#### Initializers
- `init(term: String, types: [any MusicLibrarySearchable.Type])` - Creates a library search request for a specified search term and list of library searchable types.

#### Response Method
- `func response() async throws -> MusicLibrarySearchResponse` - Fetches items of the requested library searchable types that match the search term of the request.

### Conformances

- `Equatable`
- `Hashable`
- `Sendable`
- `SendableMetatype`

## MusicLibrarySearchResponse

- **Swift Declaration**: `struct MusicLibrarySearchResponse`
- **Purpose**: An object that contains results for a library search request.
- **Source**: https://developer.apple.com/documentation/musickit/musiclibrarysearchresponse

### Properties

- `let albums: MusicItemCollection<Album>` - A collection of albums.
- `let artists: MusicItemCollection<Artist>` - A collection of artists.
- `let musicVideos: MusicItemCollection<MusicVideo>` - A collection of music videos.
- `let playlists: MusicItemCollection<Playlist>` - A collection of playlists.
- `let songs: MusicItemCollection<Song>` - A collection of songs.
- `let topResults: MusicItemCollection<MusicLibrarySearchResponse.TopResult>` - A collection of top results.

### Nested Types

#### TopResult
- **Swift Declaration**: `enum TopResult`
- **Purpose**: An item that represents one of the top results in a library search response.

##### Cases
- `case album(Album)` - An item that corresponds to an album.
- `case artist(Artist)` - An item that corresponds to an artist.
- `case musicVideo(MusicVideo)` - An item that corresponds to a music video.
- `case playlist(Playlist)` - An item that corresponds to a playlist.
- `case song(Song)` - An item that corresponds to a song.

##### Properties
- `var artwork: Artwork?` - The artwork of this top result for library search.
- `var id: MusicItemID` - The unique identifier of this item.
- `var title: String` - The title of this top result for library search.

### Conformances

- `Copyable`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `Sendable`
- `SendableMetatype`

## MusicLibrarySectionedRequest

- **Swift Declaration**: `struct MusicLibrarySectionedRequest<SectionType, MusicItemType> where SectionType : MusicLibrarySectionRequestable, MusicItemType : MusicLibraryRequestable`
- **Purpose**: A request that your app uses to fetch items grouped by sections from the user's music library.
- **Source**: https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest

### Properties

- `var includeOnlyDownloadedContent: Bool` - A Boolean value that indicates whether the library response should only include items downloaded on the user's device.
- `var limit: Int` - A limit for the number of items to return in the library response.
- `var offset: Int` - An offset for the request.

### Methods

#### Initializers
- `init()` - Creates a request to fetch items grouped by sections from the library.

#### Item Filtering Methods
- `func filterItems<RelatedMusicItemType>(matching: KeyPath<MusicItemType.LibraryFilter, MusicItemCollection<RelatedMusicItemType>?>, contains: RelatedMusicItemType)` - Filters items by a given relationship that matches a specific value.
- `func filterItems(matching: KeyPath<MusicItemType.LibraryFilter, String>, contains: String)` - Filters items by a given property that contains a specific string.
- `func filterItems(matching: KeyPath<MusicItemType.LibraryFilter, String?>, contains: String)` - Filters items by a given optional property that contains a specific string.
- `func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, equalTo: Value)` - Filters items by a given property that matches a specific value.
- `func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, equalTo: Value?)` - Filters items by a given optional property that matches a specific value.
- `func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, memberOf: [Value])` - Filters items by a property for an array of possible values.
- `func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, memberOf: [Value?])` - Filters items by an optional property for an array of possible values.
- `func filterItems(text: String)` - Filters items by a specific string.

#### Section Filtering Methods
- `func filterSections(matching: KeyPath<SectionType.LibraryFilter, String?>, contains: String)` - Filters sections by a given optional property that contains a specific string.
- `func filterSections(matching: KeyPath<SectionType.LibraryFilter, String>, contains: String)` - Filters sections by a given property that contains a specific string.
- `func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value?>, equalTo: Value?)` - Filters sections by a given optional property that matches a specific value.
- `func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value>, equalTo: Value)` - Filters sections by a given property that matches a specific value.
- `func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value>, memberOf: [Value])` - Filters sections by a property for an array of possible values.
- `func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value?>, memberOf: [Value?])` - Filters sections by an optional property for an array of possible values.
- `func filterSections(text: String)` - Filters sections by a specific string.

#### Sorting Methods
- `func sortItems<Value>(by: KeyPath<MusicItemType.LibrarySortProperties, Value>, ascending: Bool)` - Sorts items by a specified property.
- `func sortSections<Value>(by: KeyPath<SectionType.LibrarySortProperties, Value>, ascending: Bool)` - Sorts sections by a specified property.

#### Response Method
- `func response() async throws -> MusicLibrarySectionedResponse<SectionType, MusicItemType>` - Fetches items grouped by sections from the user's music library.

## MusicLibrarySectionedResponse

- **Swift Declaration**: `struct MusicLibrarySectionedResponse<SectionType, MusicItemType> where SectionType : MusicLibrarySectionRequestable, MusicItemType : MusicLibraryRequestable`
- **Purpose**: An object that contains results for a library sectioned request.
- **Source**: https://developer.apple.com/documentation/musickit/musiclibrarysectionedresponse

### Properties

- `let sections: [MusicLibrarySection<SectionType, MusicItemType>]` - An array of sections that match the filters on the originating library request.

### Conformances

- `Copyable`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `Sendable`
- `SendableMetatype`

## MusicLibrarySection

- **Swift Declaration**: `@dynamicMemberLookup struct MusicLibrarySection<SectionType, MusicItemType> where SectionType : MusicLibrarySectionRequestable, MusicItemType : MusicLibraryRequestable`
- **Purpose**: A section for a library sectioned response.
- **Source**: https://developer.apple.com/documentation/musickit/musiclibrarysection

### Overview

Your app can access any property of the requested section type directly on this library section object.

Your app can also access the items contained in a library section with the `items` property.

### Properties

- `let items: MusicItemCollection<MusicItemType>` - A collection of items that correspond to the children of the section.

### Subscripts

- `subscript<T>(dynamicMember _: KeyPath<SectionType, T>) -> T` - A subscript that allows your app to access any property of the requested section type directly on this library section object.

### Conformances

- `Copyable`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `Identifiable`
- `Sendable`
- `SendableMetatype`

## Usage

The Library API provides a comprehensive set of tools for accessing user library content:

1. **Basic Library Access**: Use `MusicLibraryRequest` to fetch library items with filtering, sorting, and pagination support.

2. **Library Search**: Use `MusicLibrarySearchRequest` to search through library content with text-based queries and type filtering.

3. **Sectioned Library Access**: Use `MusicLibrarySectionedRequest` for complex queries that group results by sections, providing hierarchical organization of library content.

All requests support asynchronous execution and return strongly-typed responses containing collections of music items that conform to the appropriate protocols.