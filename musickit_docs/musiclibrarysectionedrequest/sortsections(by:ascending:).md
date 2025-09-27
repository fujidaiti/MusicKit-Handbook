# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest/sortsections(by:ascending:)

- [MusicKit](/documentation/musickit)
- [MusicLibrarySectionedRequest](/documentation/musickit/musiclibrarysectionedrequest)
- sortSections(by:ascending:)

Instance Method

# sortSections(by:ascending:)

Sorts sections by a specified property.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func sortSections<Value>(
    by keyPath: KeyPath<SectionType.LibrarySortProperties, Value>,
    ascending: Bool
) where SectionType : MusicLibraryRequestable
```
