# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibraryrequest/filter(matching:equalto:)-8efya

- [MusicKit](/documentation/musickit)
- [MusicLibraryRequest](/documentation/musickit/musiclibraryrequest)
- filter(matching:equalTo:)

Instance Method

# filter(matching:equalTo:)

Filters items by a given optional property that matches a specific value.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func filter<Value>(
    matching keyPath: KeyPath<MusicItemType.LibraryFilter, Value?>,
    equalTo value: Value?
) where Value : MusicLibraryRequestFilterValueEquatable
```
