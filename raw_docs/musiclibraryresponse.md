# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibraryresponse

- [MusicKit](/documentation/musickit)
- MusicLibraryResponse

Structure

# MusicLibraryResponse

An object that contains results for a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicLibraryResponse<MusicItemType> where MusicItemType : MusicItem
```

## [Topics](/documentation/musickit/musiclibraryresponse#topics)

### [Instance Properties](/documentation/musickit/musiclibraryresponse#Instance-Properties)

[`let items: MusicItemCollection<MusicItemType>`](/documentation/musickit/musiclibraryresponse/items)

A collection of items that match the filters on the originating library request.

## [Relationships](/documentation/musickit/musiclibraryresponse#relationships)

### [Conforms To](/documentation/musickit/musiclibraryresponse#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
