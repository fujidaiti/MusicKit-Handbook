# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest

- [MusicKit](/documentation/musickit)
- MusicLibrarySectionedRequest

Structure

# MusicLibrarySectionedRequest

A request that your app uses to fetch items grouped by sections from the user’s music library.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicLibrarySectionedRequest<SectionType, MusicItemType> where SectionType : MusicLibrarySectionRequestable, MusicItemType : MusicLibraryRequestable
```

## [Topics](/documentation/musickit/musiclibrarysectionedrequest#topics)

### [Initializers](/documentation/musickit/musiclibrarysectionedrequest#Initializers)

[`init()`](/documentation/musickit/musiclibrarysectionedrequest/init())

Creates a request to fetch items grouped by sections from the library.

### [Instance Properties](/documentation/musickit/musiclibrarysectionedrequest#Instance-Properties)

[`var includeOnlyDownloadedContent: Bool`](/documentation/musickit/musiclibrarysectionedrequest/includeonlydownloadedcontent)

A Boolean value that indicates whether the library response should only include items downloaded on the user’s device.

[`var limit: Int`](/documentation/musickit/musiclibrarysectionedrequest/limit)

A limit for the number of items to return in the library response.

[`var offset: Int`](/documentation/musickit/musiclibrarysectionedrequest/offset)

An offset for the request.

### [Instance Methods](/documentation/musickit/musiclibrarysectionedrequest#Instance-Methods)

[`func filterItems<RelatedMusicItemType>(matching: KeyPath<MusicItemType.LibraryFilter, MusicItemCollection<RelatedMusicItemType>?>, contains: RelatedMusicItemType)`](/documentation/musickit/musiclibrarysectionedrequest/filteritems(matching:contains:)-3s88f)

Filters items by a given relationship that matches a specific value.

[`func filterItems(matching: KeyPath<MusicItemType.LibraryFilter, String>, contains: String)`](/documentation/musickit/musiclibrarysectionedrequest/filteritems(matching:contains:)-8rbsc)

Filters items by a given property that contains a specific string.

[`func filterItems(matching: KeyPath<MusicItemType.LibraryFilter, String?>, contains: String)`](/documentation/musickit/musiclibrarysectionedrequest/filteritems(matching:contains:)-9hpfh)

Filters items by a given optional property that contains a specific string.

[`func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, equalTo: Value)`](/documentation/musickit/musiclibrarysectionedrequest/filteritems(matching:equalto:)-3zn4r)

Filters items by a given property that matches a specific value.

[`func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, equalTo: Value?)`](/documentation/musickit/musiclibrarysectionedrequest/filteritems(matching:equalto:)-5ybaa)

Filters items by a given optional property that matches a specific value.

[`func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value>, memberOf: [Value])`](/documentation/musickit/musiclibrarysectionedrequest/filteritems(matching:memberof:)-49h2x)

Filters items by a property for an array of possible values.

[`func filterItems<Value>(matching: KeyPath<MusicItemType.LibraryFilter, Value?>, memberOf: [Value?])`](/documentation/musickit/musiclibrarysectionedrequest/filteritems(matching:memberof:)-zmb0)

Filters items by an optional property for an array of possible values.

[`func filterItems(text: String)`](/documentation/musickit/musiclibrarysectionedrequest/filteritems(text:))

Filters items by a specific string.

[`func filterSections(matching: KeyPath<SectionType.LibraryFilter, String?>, contains: String)`](/documentation/musickit/musiclibrarysectionedrequest/filtersections(matching:contains:)-3jf7b)

Filters sections by a given optional property that contains a specific string.

[`func filterSections(matching: KeyPath<SectionType.LibraryFilter, String>, contains: String)`](/documentation/musickit/musiclibrarysectionedrequest/filtersections(matching:contains:)-5ptoy)

Filters sections by a given property that contains a specific string.

[`func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value?>, equalTo: Value?)`](/documentation/musickit/musiclibrarysectionedrequest/filtersections(matching:equalto:)-5nop7)

Filters sections by a given optional property that matches a specific value.

[`func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value>, equalTo: Value)`](/documentation/musickit/musiclibrarysectionedrequest/filtersections(matching:equalto:)-7v8tr)

Filters sections by a given property that matches a specific value.

[`func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value>, memberOf: [Value])`](/documentation/musickit/musiclibrarysectionedrequest/filtersections(matching:memberof:)-4l0z8)

Filters sections by a property for an array of possible values.

[`func filterSections<Value>(matching: KeyPath<SectionType.LibraryFilter, Value?>, memberOf: [Value?])`](/documentation/musickit/musiclibrarysectionedrequest/filtersections(matching:memberof:)-746mb)

Filters sections by an optional property for an array of possible values.

[`func filterSections(text: String)`](/documentation/musickit/musiclibrarysectionedrequest/filtersections(text:))

Filters sections by a specific string.

[`func response() async throws -> MusicLibrarySectionedResponse<SectionType, MusicItemType>`](/documentation/musickit/musiclibrarysectionedrequest/response())

Fetches items grouped by sections from the user’s music library.

[`func sortItems<Value>(by: KeyPath<MusicItemType.LibrarySortProperties, Value>, ascending: Bool)`](/documentation/musickit/musiclibrarysectionedrequest/sortitems(by:ascending:))

Sorts items by a specified property.

[`func sortSections<Value>(by: KeyPath<SectionType.LibrarySortProperties, Value>, ascending: Bool)`](/documentation/musickit/musiclibrarysectionedrequest/sortsections(by:ascending:))

Sorts sections by a specified property.
