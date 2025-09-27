# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysection/subscript(dynamicmember:)

- [MusicKit](/documentation/musickit)
- [MusicLibrarySection](/documentation/musickit/musiclibrarysection)
- subscript(dynamicMember:)

Instance Subscript

# subscript(dynamicMember:)

A subscript that allows your app to access any property of the requested section type directly on this library section object.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
subscript<T>(dynamicMember keyPath: KeyPath<SectionType, T>) -> T { get }
```
