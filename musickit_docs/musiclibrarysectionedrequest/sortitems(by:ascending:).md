# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest/sortitems(by:ascending:)

- [MusicKit](/documentation/musickit)
- [MusicLibrarySectionedRequest](/documentation/musickit/musiclibrarysectionedrequest)
- sortItems(by:ascending:)

Instance Method

# sortItems(by:ascending:)

Sorts items by a specified property.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func sortItems<Value>(
    by keyPath: KeyPath<MusicItemType.LibrarySortProperties, Value>,
    ascending: Bool
)
```
