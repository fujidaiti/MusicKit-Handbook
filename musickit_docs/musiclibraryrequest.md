# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibraryrequest

- [MusicKit](/documentation/musickit)
- MusicLibraryRequest

Structure

# MusicLibraryRequest

A request that your app uses to fetch items from the user’s music library.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicLibraryRequest<MusicItemType> where MusicItemType : MusicLibraryRequestable
```

## [Topics](/documentation/musickit/musiclibraryrequest#topics)

### [Initializers](/documentation/musickit/musiclibraryrequest#Initializers)

[`init()`](/documentation/musickit/musiclibraryrequest/init())

Creates a request to fetch items from the library.

### [Instance Properties](/documentation/musickit/musiclibraryrequest#Instance-Properties)

[`var includeOnlyDownloadedContent: Bool`](/documentation/musickit/musiclibraryrequest/includeonlydownloadedcontent)

A Boolean value that indicates whether the library response should only include items downloaded on the user’s device.

[`var limit: Int`](/documentation/musickit/musiclibraryrequest/limit)

A limit for the number of items to return in the library response.

[`var offset: Int`](/documentation/musickit/musiclibraryrequest/offset)

An offset for the request.

### [Instance Methods](/documentation/musickit/musiclibraryrequest#Instance-Methods)

[`func filter(matching: KeyPath<MusicItemType.LibraryFilter, String?>, contains: String)`](/documentation/musickit/musiclibraryrequest/filter(matching:contains:)-4q231)

Filters items by a given optional property that contains a specific string.

[`func filter(matching: KeyPath<MusicItemType.LibraryFilter, String>, contains: String)`](/documentation/musickit/musiclibraryrequest/filter(matching:contains:)-8wwn3)

Filters items by a given property that contains a specific string.

[`func filter<RelatedMusicItemType>(matching: KeyPath<MusicItemType.LibraryFilter, MusicItemCollection<RelatedMusicItemType>?>, contains: RelatedMusicItemType)`](/documentation/musickit/musiclibraryrequest/filter(matching:contains:)-9756l)

Filters items by a given relationship that matches a specific value.

[`func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, equalTo: Value)`](/documentation/musickit/musiclibraryrequest/filter(matching:equalto:)-5jgfj)

Filters items by a given property that matches a specific value.

[`func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, equalTo: Value?)`](/documentation/musickit/musiclibraryrequest/filter(matching:equalto:)-8efya)

Filters items by a given optional property that matches a specific value.

[`func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, memberOf: [Value?])`](/documentation/musickit/musiclibraryrequest/filter(matching:memberof:)-2u2ia)

Filters items by an optional property for an array of possible values.

[`func filter<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, memberOf: [Value])`](/documentation/musickit/musiclibraryrequest/filter(matching:memberof:)-3e2ab)

Filters items by a property for an array of possible values.

[`func filter(text: String)`](/documentation/musickit/musiclibraryrequest/filter(text:))

Filters items by a specific string.

[`func response() async throws -> MusicLibraryResponse<MusicItemType>`](/documentation/musickit/musiclibraryrequest/response())

Fetches items from the user’s music library.

[`func sort<Value>(by: KeyPath<MusicItemType.LibrarySortProperties, Value>, ascending: Bool)`](/documentation/musickit/musiclibraryrequest/sort(by:ascending:))

Sorts items by a specified property.
