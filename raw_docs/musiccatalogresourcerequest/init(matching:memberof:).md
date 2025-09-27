# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogresourcerequest/init(matching:memberof:)

- [MusicKit](/documentation/musickit)
- [MusicCatalogResourceRequest](/documentation/musickit/musiccatalogresourcerequest)
- init(matching:memberOf:)

Initializer

# init(matching:memberOf:)

Creates a request to fetch items using a filter that matches any value from an array of possible values.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
init<Value>(
    matching keyPath: KeyPath<MusicItemType.FilterType, Value>,
    memberOf values: [Value]
) where MusicItemType : FilterableMusicItem
```
