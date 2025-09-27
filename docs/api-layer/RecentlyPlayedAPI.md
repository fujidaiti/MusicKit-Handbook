# Recently Played API

> Source: Multiple Apple MusicKit documentation pages

The Recently Played API provides access to the user's recently played music items, including both individual tracks and container items like albums, playlists, and stations. This API enables developers to build features that show listening history and recently accessed content.

## MusicRecentlyPlayedRequest

- **Swift Declaration**: `struct MusicRecentlyPlayedRequest<MusicItemType> where MusicItemType : MusicRecentlyPlayedRequestable, MusicItemType : Decodable`
- **Purpose**: A request that your app uses to fetch items the user has recently played.
- **Source**: https://developer.apple.com/documentation/musickit/musicrecentlyplayedrequest

### Properties

- `var limit: Int?` - A limit for the number of items to return in the response that contains items the user has recently played.
- `var offset: Int?` - An offset for the request.

### Methods

#### Initializers
- `init()` - Creates a request for items the user has recently played.

#### Response Method
- `func response() async throws -> MusicRecentlyPlayedResponse<MusicItemType>` - Fetches items the user has recently played.

## MusicRecentlyPlayedResponse

- **Swift Declaration**: `struct MusicRecentlyPlayedResponse<MusicItemType> where MusicItemType : MusicRecentlyPlayedRequestable`
- **Purpose**: An object that contains items the user has recently played.
- **Source**: https://developer.apple.com/documentation/musickit/musicrecentlyplayedresponse

### Properties

- `let items: MusicItemCollection<MusicItemType>` - A collection of items the user has recently played.

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

## MusicRecentlyPlayedContainerRequest

- **Swift Declaration**: `typealias MusicRecentlyPlayedContainerRequest = MusicRecentlyPlayedRequest<RecentlyPlayedMusicItem>`
- **Purpose**: A request that your app uses to fetch albums, playlists or stations that the user has recently played.
- **Source**: https://developer.apple.com/documentation/musickit/musicrecentlyplayedcontainerrequest

This is a specialized version of `MusicRecentlyPlayedRequest` that specifically targets container items (albums, playlists, stations) rather than individual tracks.

## MusicRecentlyPlayedContainerResponse

- **Swift Declaration**: `typealias MusicRecentlyPlayedContainerResponse = MusicRecentlyPlayedResponse<RecentlyPlayedMusicItem>`
- **Purpose**: An object that contains albums, playlists or stations that the user has recently played.
- **Source**: https://developer.apple.com/documentation/musickit/musicrecentlyplayedcontainerresponse

This is a specialized version of `MusicRecentlyPlayedResponse` that contains `RecentlyPlayedMusicItem` instances representing container items.

## RecentlyPlayedMusicItem

- **Swift Declaration**: `enum RecentlyPlayedMusicItem`
- **Purpose**: An item that represents an album, a playlist, or a station that the user has recently played.
- **Source**: https://developer.apple.com/documentation/musickit/recentlyplayedmusicitem

### Cases

- `case album(Album)` - An item that corresponds to an album.
- `case playlist(Playlist)` - An item that corresponds to a playlist.
- `case station(Station)` - An item that corresponds to a station.

### Properties

- `var artwork: Artwork?` - The artwork of this item.
- `var id: MusicItemID` - The unique identifier of this item.
- `var playParameters: PlayParameters?` - The parameters to use to play this item.
- `var subtitle: String?` - The subtitle of this item.
- `var title: String` - The title of this item.

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
- `MusicRecentlyPlayedRequestable`
- `PlayableMusicItem`
- `Sendable`
- `SendableMetatype`

## Usage

The Recently Played API provides several ways to access user's listening history:

1. **Generic Recently Played Items**: Use `MusicRecentlyPlayedRequest<T>` with any type that conforms to `MusicRecentlyPlayedRequestable` to fetch recently played items of that specific type.

2. **Container Items**: Use `MusicRecentlyPlayedContainerRequest` (which is a type alias) to specifically fetch recently played albums, playlists, and stations. This is ideal for showing recently accessed collections rather than individual tracks.

3. **Flexible Content Access**: The `RecentlyPlayedMusicItem` enum provides a unified interface for different types of recently played containers while maintaining type safety through its cases.

4. **Pagination Support**: Both request types support `limit` and `offset` parameters for implementing pagination in recently played lists.

5. **Playback Integration**: Items returned include `playParameters` when available, enabling direct playback of recently played content.

This API is particularly useful for:
- Building "Recently Played" sections in music apps
- Implementing quick access to recently accessed content
- Creating listening history features
- Providing continuity across app sessions
- Suggesting content based on recent listening patterns

The API respects user privacy and only returns items that the user has explicitly played through Apple Music or the app.