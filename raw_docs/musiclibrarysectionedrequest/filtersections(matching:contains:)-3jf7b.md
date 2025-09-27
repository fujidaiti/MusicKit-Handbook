# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest/filtersections(matching:contains:)-3jf7b

- [MusicKit](/documentation/musickit)
- [MusicLibrarySectionedRequest](/documentation/musickit/musiclibrarysectionedrequest)
- filterSections(matching:contains:)

Instance Method

# filterSections(matching:contains:)

Filters sections by a given optional property that contains a specific string.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func filterSections(
    matching keyPath: KeyPath<SectionType.LibraryFilter, String?>,
    contains text: String
) where SectionType : MusicLibraryRequestable
```
