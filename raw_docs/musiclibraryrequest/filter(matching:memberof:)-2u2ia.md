# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibraryrequest/filter(matching:memberof:)-2u2ia

- [MusicKit](/documentation/musickit)
- [MusicLibraryRequest](/documentation/musickit/musiclibraryrequest)
- filter(matching:memberOf:)

Instance Method

# filter(matching:memberOf:)

Filters items by an optional property for an array of possible values.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func filter<Value>(
    matching keyPath: KeyPath<MusicItemType.LibraryFilter, Value?>,
    memberOf values: [Value?]
) where Value : MusicLibraryRequestFilterValueMembershipComparable
```
