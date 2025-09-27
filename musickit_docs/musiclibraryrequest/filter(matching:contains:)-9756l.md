# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibraryrequest/filter(matching:contains:)-9756l

- [MusicKit](/documentation/musickit)
- [MusicLibraryRequest](/documentation/musickit/musiclibraryrequest)
- filter(matching:contains:)

Instance Method

# filter(matching:contains:)

Filters items by a given relationship that matches a specific value.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func filter<RelatedMusicItemType>(
    matching keyPath: KeyPath<MusicItemType.LibraryFilter, MusicItemCollection<RelatedMusicItemType>?>,
    contains relatedItem: RelatedMusicItemType
) where RelatedMusicItemType : MusicItem
```
