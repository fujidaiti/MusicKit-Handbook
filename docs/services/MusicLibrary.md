# Music Library Service

> Source: Multiple Apple MusicKit documentation pages

This service provides functionality for accessing and modifying the user's music library, including adding items, creating playlists, and editing playlists.

## MusicLibrary
- **Swift Declaration**: `class MusicLibrary`
- **Purpose**: An object your app uses to access the user's music library
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musiclibrary)
- **Type Properties**:
  - `static let shared: MusicLibrary` - A shared object that allows your app to modify the user's music library
- **Instance Methods**:
  - `func add<MusicItemType>(_ item: MusicItemType) async throws` - Adds an item to the user's music library (where MusicItemType : MusicLibraryAddable)
  - `func add<MusicItemType>(_ item: MusicItemType, to playlist: Playlist) async throws -> Playlist` - Adds an item to the end of an existing playlist
  - `func createPlaylist(name: String, description: String?, authorDisplayName: String?) async throws -> Playlist` - Creates a playlist in the user's music library
  - `func createPlaylist<S, MusicPlaylistAddableType>(name: String, description: String?, authorDisplayName: String?, items: S) async throws -> Playlist` - Creates a playlist in the user's music library with initial items
  - `func edit(_ playlist: Playlist, name: String?, description: String?, authorDisplayName: String?) async throws -> Playlist` - Edits a playlist that your app has created
  - `func edit<S, MusicPlaylistAddableType>(_ playlist: Playlist, name: String?, description: String?, authorDisplayName: String?, items: S) async throws -> Playlist` - Edits a playlist that your app has created including items to rebuild the list of entries
- **Nested Types**:
  - `enum Error` - An error that the music library can throw upon accessing, manipulating, or requesting data from the user's music library
- **Availability**: iOS 16.0+, iPadOS 16.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+
- **Usage**: Use the shared instance to perform library modifications. All methods are asynchronous and may throw errors related to permissions or operation failures.

## MusicLibrary.Error
- **Swift Declaration**: `enum Error`
- **Purpose**: An error that the music library can throw upon accessing, manipulating, or requesting data from the user's music library
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musiclibrary/error)
- **Enumeration Cases**:
  - `case addToPlaylistFailed` - An error that indicates a failure in the process of adding an item to a playlist
  - `case createPlaylistFailed` - An error that indicates a failure in the process of creating a playlist
  - `case editPlaylistFailed` - An error that indicates a failure in the process of editing a playlist
  - `case itemAlreadyAdded` - An error indicating that the item attempting to be added to the user's music library is already in the library
  - `case permissionDenied` - An error that occurs when the user doesn't consent for the current app to access their Apple Music library
  - `case playlistNotInLibrary` - An error indicating that the playlist attempting to be added to is not in the user's library
  - `case unableToAddItem` - An error indicating that the item attempting to be added to the user's music library cannot be added
  - `case unknown` - An error indicating the ocurrence of an unknown or unexpected error
- **Conformances**: [`Copyable`](/documentation/Swift/Copyable), [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible), [`Equatable`](/documentation/Swift/Equatable), [`Error`](/documentation/Swift/Error), [`Hashable`](/documentation/Swift/Hashable), [`LocalizedError`](/documentation/Foundation/LocalizedError), [`RawRepresentable`](/documentation/Swift/RawRepresentable), [`Sendable`](/documentation/Swift/Sendable), [`SendableMetatype`](/documentation/Swift/SendableMetatype)
- **Availability**: iOS 16.1+, iPadOS 16.1+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 16.1+, visionOS 1.0+, watchOS 9.1+

## Usage Patterns

### Adding Items to Library
```swift
let library = MusicLibrary.shared

do {
    // Add a song to the user's library
    try await library.add(song)

    // Add an album to the user's library
    try await library.add(album)

    // Add an artist to the user's library
    try await library.add(artist)
} catch MusicLibrary.Error.itemAlreadyAdded {
    // Handle case where item is already in library
} catch MusicLibrary.Error.permissionDenied {
    // Handle permission denied
} catch MusicLibrary.Error.unableToAddItem {
    // Handle case where item cannot be added
} catch {
    // Handle other errors
}
```

### Creating Playlists
```swift
let library = MusicLibrary.shared

do {
    // Create an empty playlist
    let playlist = try await library.createPlaylist(
        name: "My Playlist",
        description: "A collection of favorite songs",
        authorDisplayName: "My App"
    )

    // Create a playlist with initial items
    let playlistWithItems = try await library.createPlaylist(
        name: "My Playlist",
        description: "A collection of favorite songs",
        authorDisplayName: "My App",
        items: [song1, song2, song3]
    )
} catch MusicLibrary.Error.createPlaylistFailed {
    // Handle playlist creation failure
} catch MusicLibrary.Error.permissionDenied {
    // Handle permission denied
} catch {
    // Handle other errors
}
```

### Adding Items to Playlists
```swift
let library = MusicLibrary.shared

do {
    let updatedPlaylist = try await library.add(song, to: existingPlaylist)
    // Use the updated playlist reference
} catch MusicLibrary.Error.addToPlaylistFailed {
    // Handle add to playlist failure
} catch MusicLibrary.Error.playlistNotInLibrary {
    // Handle case where playlist is not in user's library
} catch MusicLibrary.Error.permissionDenied {
    // Handle permission denied
} catch {
    // Handle other errors
}
```

### Editing Playlists
```swift
let library = MusicLibrary.shared

do {
    // Edit playlist metadata only
    let updatedPlaylist = try await library.edit(
        playlist,
        name: "New Playlist Name",
        description: "Updated description",
        authorDisplayName: "My App"
    )

    // Edit playlist and replace all items
    let playlistWithNewItems = try await library.edit(
        playlist,
        name: "New Playlist Name",
        description: "Updated description",
        authorDisplayName: "My App",
        items: [newSong1, newSong2, newSong3]
    )
} catch MusicLibrary.Error.editPlaylistFailed {
    // Handle edit failure
} catch MusicLibrary.Error.playlistNotInLibrary {
    // Handle case where playlist is not in user's library
} catch MusicLibrary.Error.permissionDenied {
    // Handle permission denied
} catch {
    // Handle other errors
}
```

## Important Notes

### Permissions
- The user must have granted permission for your app to access their Apple Music library
- Operations will fail with `MusicLibrary.Error.permissionDenied` if permissions are not granted
- Use [MusicAuthorization](Authorization.md#musicauthorization) to check and request permissions

### Library Capabilities
- Check [MusicSubscription.current.hasCloudLibraryEnabled](Authorization.md#musicsubscription) to determine if the user can modify their library
- Library modification requires an active Apple Music subscription with iCloud Music Library enabled

### Playlist Editing Restrictions
- You can only edit playlists that your app has created
- Attempting to edit system playlists or playlists created by other apps will result in errors

### Asynchronous Operations
- All library operations are asynchronous and should be called from async contexts
- Operations may take time to complete, especially when dealing with large playlists or network conditions

### Error Handling
- Always implement comprehensive error handling for library operations
- Network failures, permission changes, and library state changes can cause operations to fail
- Consider implementing retry logic for transient failures

## Related Types
- [MusicLibraryAddable](../protocols/PlaybackProtocols.md#musiclibraryaddable) - Protocol for items that can be added to the library
- [MusicLibraryRequest](../api-layer/LibraryAPI.md#musiclibraryrequest) - For requesting library content
- [MusicAuthorization](Authorization.md#musicauthorization) - For managing user permissions
- [MusicSubscription](Authorization.md#musicsubscription) - For checking library capabilities