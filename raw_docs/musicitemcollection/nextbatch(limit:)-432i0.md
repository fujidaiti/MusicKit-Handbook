# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicitemcollection/nextbatch(limit:)-432i0

- [MusicKit](/documentation/musickit)
- [MusicItemCollection](/documentation/musickit/musicitemcollection)
- nextBatch(limit:)

Instance Method

# nextBatch(limit:)

Fetches the next batch of items asynchronously.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
func nextBatch(limit: Int? = nil) async throws -> MusicItemCollection<MusicItemType>? where MusicItemType : Decodable
```

Available when `MusicItemType` conforms to `MusicItem`.

## [Discussion](/documentation/musickit/musicitemcollection/nextbatch(limit:)-432i0#discussion)

This method returns the next batch of items as another collection of music items
of the same type.
