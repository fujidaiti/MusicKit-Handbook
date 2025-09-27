# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest/filtersections(matching:equalto:)-7v8tr

- [MusicKit](/documentation/musickit)
- [MusicLibrarySectionedRequest](/documentation/musickit/musiclibrarysectionedrequest)
- filterSections(matching:equalTo:)

Instance Method

# filterSections(matching:equalTo:)

Filters sections by a given property that matches a specific value.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
mutating func filterSections<Value>(
    matching keyPath: KeyPath<SectionType.LibraryFilter, Value>,
    equalTo value: Value
) where SectionType : MusicLibraryRequestable, Value : MusicLibraryRequestFilterValueEquatable
```
