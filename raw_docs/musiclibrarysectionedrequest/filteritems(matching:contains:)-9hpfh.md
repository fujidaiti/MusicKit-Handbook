# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest/filteritems(matching:contains:)-9hpfh

- [MusicKit](/documentation/musickit)
- [MusicLibrarySectionedRequest](/documentation/musickit/musiclibrarysectionedrequest)
- filterItems(matching:contains:)

Instance Method

# filterItems(matching:contains:)

Filters items by a given optional property that contains a specific string.

iOS 16.0+iPadOS 16.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func filterItems(
    matching keyPath: KeyPath<MusicItemType.LibraryFilter, String?>,
    contains text: String
)
```
