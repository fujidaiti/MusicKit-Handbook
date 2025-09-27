# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibraryrequestable

- [MusicKit](/documentation/musickit)
- MusicLibraryRequestable

Protocol

# MusicLibraryRequestable

A protocol for music items that your app can fetch by using a library request.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
protocol MusicLibraryRequestable : MusicItem
```

## [Topics](/documentation/musickit/musiclibraryrequestable#topics)

### [Associated Types](/documentation/musickit/musiclibraryrequestable#Associated-Types)

[`associatedtype LibraryFilter`](/documentation/musickit/musiclibraryrequestable/libraryfilter)

The associated type that contains the set of music item properties your app uses as a filter for a library request.

**Required**

[`associatedtype LibrarySortProperties`](/documentation/musickit/musiclibraryrequestable/librarysortproperties)

The associated type that contains the set of properties your app uses to sort results for a library request.

**Required**

## [Relationships](/documentation/musickit/musiclibraryrequestable#relationships)

### [Inherits From](/documentation/musickit/musiclibraryrequestable#inherits-from)

- [`MusicItem`](/documentation/musickit/musicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

### [Conforming Types](/documentation/musickit/musiclibraryrequestable#conforming-types)

- [`Album`](/documentation/musickit/album)
- [`Artist`](/documentation/musickit/artist)
- [`Genre`](/documentation/musickit/genre)
- [`MusicVideo`](/documentation/musickit/musicvideo)
- [`Playlist`](/documentation/musickit/playlist)
- [`Playlist.Entry`](/documentation/musickit/playlist/entry)
- [`Song`](/documentation/musickit/song)
- [`Track`](/documentation/musickit/track)
