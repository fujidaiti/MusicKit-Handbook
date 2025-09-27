# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest/filteritems(matching:memberof:)-49h2x

- [MusicKit](/documentation/musickit)
- [MusicLibrarySectionedRequest](/documentation/musickit/musiclibrarysectionedrequest)
- filterItems(matching:memberOf:)

Instance Method

# filterItems(matching:memberOf:)

Filters items by a property for an array of possible values.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func filterItems<Value>(
    matching keyPath: KeyPath<MusicItemType.LibraryFilter, Value>,
    memberOf values: [Value]
) where Value : MusicLibraryRequestFilterValueMembershipComparable
```
