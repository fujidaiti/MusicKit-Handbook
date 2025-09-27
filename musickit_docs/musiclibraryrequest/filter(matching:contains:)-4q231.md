# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibraryrequest/filter(matching:contains:)-4q231

- [MusicKit](/documentation/musickit)
- [MusicLibraryRequest](/documentation/musickit/musiclibraryrequest)
- filter(matching:contains:)

Instance Method

# filter(matching:contains:)

Filters items by a given optional property that contains a specific string.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func filter(
    matching keyPath: KeyPath<MusicItemType.LibraryFilter, String?>,
    contains text: String
)
```
