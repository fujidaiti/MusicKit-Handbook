# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/genre

- [MusicKit](/documentation/musickit)
- Genre

Structure

# Genre

A music item that represents a genre.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct Genre
```

## [Topics](/documentation/musickit/genre#topics)

### [Instance Properties](/documentation/musickit/genre#Instance-Properties)

[`let id: MusicItemID`](/documentation/musickit/genre/id)

The unique identifier for the genre.

[`var libraryAddedDate: Date?`](/documentation/musickit/genre/libraryaddeddate)

The date when the user added the genre to the library.

[`var name: String`](/documentation/musickit/genre/name)

The localized name of the genre.

[`var parent: Genre?`](/documentation/musickit/genre/parent)

The parent genre, if any.

### [Default Implementations](/documentation/musickit/genre#Default-Implementations)

[API Reference

FilterableMusicItem Implementations](/documentation/musickit/genre/filterablemusicitem-implementations)

[API Reference

MusicLibraryRequestable Implementations](/documentation/musickit/genre/musiclibraryrequestable-implementations)

## [Relationships](/documentation/musickit/genre#relationships)

### [Conforms To](/documentation/musickit/genre#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`FilterableMusicItem`](/documentation/musickit/filterablemusicitem)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`MusicCatalogTopLevelResourceRequesting`](/documentation/musickit/musiccatalogtoplevelresourcerequesting)
- [`MusicItem`](/documentation/musickit/musicitem)
- [`MusicLibraryRequestable`](/documentation/musickit/musiclibraryrequestable)
- [`MusicLibrarySectionRequestable`](/documentation/musickit/musiclibrarysectionrequestable)
- [`MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/genre#see-also)

### [Music Items](/documentation/musickit/genre#Music-Items)

[`struct Album`](/documentation/musickit/album)

A music item that represents an album.

[`struct Artist`](/documentation/musickit/artist)

A music item that represents an artist.

[`struct Curator`](/documentation/musickit/curator)

A music item that represents a curator.

[`struct MusicVideo`](/documentation/musickit/musicvideo)

A music item that represents a music video.

[`struct Playlist`](/documentation/musickit/playlist)

A music item that represents a playlist.

[`struct RadioShow`](/documentation/musickit/radioshow)

A music item that represents a radio show.

[`struct RecordLabel`](/documentation/musickit/recordlabel)

A music item that represents a record label.

[`struct Song`](/documentation/musickit/song)

A music item that represents a song.

[`struct Station`](/documentation/musickit/station)

A music item that represents a station.

[`enum Track`](/documentation/musickit/track)

A music item that represents a track.
