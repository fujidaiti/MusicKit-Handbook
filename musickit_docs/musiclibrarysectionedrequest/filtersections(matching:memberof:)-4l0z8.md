# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest/filtersections(matching:memberof:)-4l0z8

- [MusicKit](/documentation/musickit)
- [MusicLibrarySectionedRequest](/documentation/musickit/musiclibrarysectionedrequest)
- filterSections(matching:memberOf:)

Instance Method

# filterSections(matching:memberOf:)

Filters sections by a property for an array of possible values.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func filterSections<Value>(
    matching keyPath: KeyPath<SectionType.LibraryFilter, Value>,
    memberOf values: [Value]
) where SectionType : MusicLibraryRequestable, Value : MusicLibraryRequestFilterValueMembershipComparable
```
