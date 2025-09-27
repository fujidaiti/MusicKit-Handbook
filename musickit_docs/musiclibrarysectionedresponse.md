# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysectionedresponse

- [MusicKit](/documentation/musickit)
- MusicLibrarySectionedResponse

Structure

# MusicLibrarySectionedResponse

An object that contains results for a library sectioned request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicLibrarySectionedResponse<SectionType, MusicItemType> where SectionType : MusicLibrarySectionRequestable, MusicItemType : MusicLibraryRequestable
```

## [Topics](/documentation/musickit/musiclibrarysectionedresponse#topics)

### [Instance Properties](/documentation/musickit/musiclibrarysectionedresponse#Instance-Properties)

[`let sections: [MusicLibrarySection<SectionType, MusicItemType>]`](/documentation/musickit/musiclibrarysectionedresponse/sections)

An array of sections that match the filters on the originating library request.

## [Relationships](/documentation/musickit/musiclibrarysectionedresponse#relationships)

### [Conforms To](/documentation/musickit/musiclibrarysectionedresponse#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
