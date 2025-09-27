# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/libraryartistsortproperties

- [MusicKit](/documentation/musickit)
- LibraryArtistSortProperties

Protocol

# LibraryArtistSortProperties

Artist properties your app uses to sort results for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol LibraryArtistSortProperties
```

## [Topics](/documentation/musickit/libraryartistsortproperties#topics)

### [Instance Properties](/documentation/musickit/libraryartistsortproperties#Instance-Properties)

[`var albumCount: Int?`](/documentation/musickit/libraryartistsortproperties/albumcount)

The number of albums from this artist.

**Required**

[`var libraryAddedDate: Date?`](/documentation/musickit/libraryartistsortproperties/libraryaddeddate)

The date when the user added the artist to the library.

**Required**

[`var name: String`](/documentation/musickit/libraryartistsortproperties/name)

The name of the artist.

**Required**
