# Personal Recommendations API

> Source: Multiple Apple MusicKit documentation pages

The Personal Recommendations API provides access to personalized music recommendations based on the user's library and listening history. It allows developers to fetch curated recommendations that adapt to user preferences.

## MusicPersonalRecommendationsRequest

- **Swift Declaration**: `struct MusicPersonalRecommendationsRequest`
- **Purpose**: A request that your app uses to fetch music recommendations based on the user's library and listening history.
- **Source**: https://developer.apple.com/documentation/musickit/musicpersonalrecommendationsrequest

### Properties

- `var limit: Int?` - A limit for the number of recommendations to return in the personal recommendations response.
- `var offset: Int?` - An offset for the request.

### Methods

#### Initializers
- `init()` - Creates a request to fetch default personal recommendations for the user.
- `init<S>(refreshing: S)` - Creates a request to fetch default personal recommendations for the user.

#### Response Method
- `func response() async throws -> MusicPersonalRecommendationsResponse` - Fetches the music recommendations based on the user's library and listening history.

### Conformances

- `Equatable`
- `Hashable`
- `Sendable`
- `SendableMetatype`

## MusicPersonalRecommendationsResponse

- **Swift Declaration**: `struct MusicPersonalRecommendationsResponse`
- **Purpose**: An object that contains results for a personal recommendations request.
- **Source**: https://developer.apple.com/documentation/musickit/musicpersonalrecommendationsresponse

### Properties

- `let recommendations: MusicItemCollection<MusicPersonalRecommendation>` - A collection of personal recommendations.

### Conformances

- `Copyable`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Decodable`
- `Encodable`
- `Equatable`
- `Hashable`
- `Sendable`
- `SendableMetatype`

## MusicPersonalRecommendation

- **Swift Declaration**: `struct MusicPersonalRecommendation`
- **Purpose**: An object that contains recommended items based on the user's library and listening history.
- **Source**: https://developer.apple.com/documentation/musickit/musicpersonalrecommendation

### Properties

- `var albums: MusicItemCollection<Album>` - The albums for the personal recommendation.
- `let id: MusicItemID` - The unique identifier for the personal recommendation.
- `var items: MusicItemCollection<MusicPersonalRecommendation.Item>` - The items for the personal recommendation.
- `let nextRefreshDate: Date?` - The next date for refreshing the personal recommendation.
- `var playlists: MusicItemCollection<Playlist>` - The playlists for the personal recommendation.
- `let reason: String?` - The reason for the personal recommendation.
- `var stations: MusicItemCollection<Station>` - The stations for the personal recommendation.
- `let title: String?` - The title for the personal recommendation.
- `var types: [any MusicPersonalRecommendationItem.Type]` - The types of items in the personal recommendation.

### Conformances

- `Copyable`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Decodable`
- `Encodable`
- `Equatable`
- `Hashable`
- `Identifiable`
- `MusicItem`
- `Sendable`
- `SendableMetatype`

### Nested Types

#### Item
- **Swift Declaration**: `enum Item`
- **Purpose**: An item that represents an album, a playlist, or a station for a personal recommendation.

##### Cases
- `case album(Album)` - An item that corresponds to an album.
- `case playlist(Playlist)` - An item that corresponds to a playlist.
- `case station(Station)` - An item that corresponds to a station.

##### Properties
- `var artwork: Artwork?` - The artwork of this item.
- `var id: MusicItemID` - The unique identifier of this item.
- `var subtitle: String?` - The subtitle of this item.
- `var title: String` - The title of this item.

##### Conformances
- `Copyable`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Decodable`
- `Encodable`
- `Equatable`
- `Hashable`
- `Identifiable`
- `MusicItem`
- `Sendable`
- `SendableMetatype`

## Usage

The Personal Recommendations API provides intelligent music discovery features:

1. **Personalized Content**: Recommendations are tailored based on the user's music library and listening history, providing relevant suggestions.

2. **Diverse Content Types**: Recommendations can include albums, playlists, and stations, offering various ways to discover music.

3. **Refresh Management**: The API provides `nextRefreshDate` to help manage when to request updated recommendations.

4. **Contextual Information**: Each recommendation includes a `reason` field explaining why the content was recommended, and a `title` for categorization.

5. **Flexible Access**: The `items` property provides a unified collection, while type-specific properties (`albums`, `playlists`, `stations`) allow filtered access to specific content types.

This API is ideal for:
- Building discovery features in music apps
- Creating personalized home screens
- Implementing "For You" sections
- Enhancing user engagement through relevant content suggestions

The recommendation system adapts over time as users interact with their library and streaming content, ensuring recommendations remain current and relevant.