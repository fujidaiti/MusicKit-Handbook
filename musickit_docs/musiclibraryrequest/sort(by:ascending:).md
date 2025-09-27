# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibraryrequest/sort(by:ascending:)

- [MusicKit](/documentation/musickit)
- [MusicLibraryRequest](/documentation/musickit/musiclibraryrequest)
- sort(by:ascending:)

Instance Method

# sort(by:ascending:)

Sorts items by a specified property.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func sort<Value>(
    by keyPath: KeyPath<MusicItemType.LibrarySortProperties, Value>,
    ascending: Bool
)
```
