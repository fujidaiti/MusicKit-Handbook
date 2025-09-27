# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicrecentlyplayedresponse

- [MusicKit](/documentation/musickit)
- MusicRecentlyPlayedResponse

Structure

# MusicRecentlyPlayedResponse

An object that contains items the user has recently played.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct MusicRecentlyPlayedResponse<MusicItemType> where MusicItemType : MusicRecentlyPlayedRequestable
```

## [Topics](/documentation/musickit/musicrecentlyplayedresponse#topics)

### [Instance Properties](/documentation/musickit/musicrecentlyplayedresponse#Instance-Properties)

[`let items: MusicItemCollection<MusicItemType>`](/documentation/musickit/musicrecentlyplayedresponse/items)

A collection of items the user has recently played.

## [Relationships](/documentation/musickit/musicrecentlyplayedresponse#relationships)

### [Conforms To](/documentation/musickit/musicrecentlyplayedresponse#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
