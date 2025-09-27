# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicpropertycontainer

- [MusicKit](/documentation/musickit)
- MusicPropertyContainer

Protocol

# MusicPropertyContainer

A protocol for music items that allow loading additional properties that you can fetch asynchronously.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
protocol MusicPropertyContainer
```

## [Topics](/documentation/musickit/musicpropertycontainer#topics)

### [Instance Methods](/documentation/musickit/musicpropertycontainer#Instance-Methods)

[`func with([PartialMusicAsyncProperty<Self>]) async throws -> Self`](/documentation/musickit/musicpropertycontainer/with(_:))

Loads a new instance of the music item that includes the specified properties.

**Required** Default implementation provided.

[`func with([PartialMusicAsyncProperty<Self>], preferredSource: MusicPropertySource) async throws -> Self`](/documentation/musickit/musicpropertycontainer/with(_:preferredsource:)-8ec7p)

Loads a new instance of the music item that includes the specified properties.

**Required**

[`func with(PartialMusicAsyncProperty<Self>..., preferredSource: MusicPropertySource) async throws -> Self`](/documentation/musickit/musicpropertycontainer/with(_:preferredsource:)-9wqhc)

Loads a new instance of the music item that includes the specified properties.

**Required**

## [Relationships](/documentation/musickit/musicpropertycontainer#relationships)

### [Conforming Types](/documentation/musickit/musicpropertycontainer#conforming-types)

- [`Album`](/documentation/musickit/album)
- [`Artist`](/documentation/musickit/artist)
- [`Curator`](/documentation/musickit/curator)
- [`Genre`](/documentation/musickit/genre)
- [`MusicPlayer.Queue.Entry.Item`](/documentation/musickit/musicplayer/queue/entry/item-swift.enum)
- [`MusicVideo`](/documentation/musickit/musicvideo)
- [`Playlist`](/documentation/musickit/playlist)
- [`Playlist.Entry`](/documentation/musickit/playlist/entry)
- [`Playlist.Entry.Item`](/documentation/musickit/playlist/entry/item-swift.enum)
- [`RadioShow`](/documentation/musickit/radioshow)
- [`RecordLabel`](/documentation/musickit/recordlabel)
- [`Song`](/documentation/musickit/song)
- [`Station`](/documentation/musickit/station)
- [`Track`](/documentation/musickit/track)

## [See Also](/documentation/musickit/musicpropertycontainer#see-also)

### [Utility](/documentation/musickit/musicpropertycontainer#Utility)

[`protocol MusicItem`](/documentation/musickit/musicitem)

A protocol with basic requirements for music items.

[`struct MusicItemID`](/documentation/musickit/musicitemid)

An object that represents a unique identifier for a music item.

[`struct MusicItemCollection`](/documentation/musickit/musicitemcollection)

A collection of music items.

[`class MusicRelationshipProperty`](/documentation/musickit/musicrelationshipproperty)

An identifier for a music item relationship property from a specific root type to a specific value type for the element of the resulting collection.

[`class MusicExtendedAttributeProperty`](/documentation/musickit/musicextendedattributeproperty)

An identifier for a music item extended attribute property from a specific root type to a specific resulting value type.

[`class MusicAttributeProperty`](/documentation/musickit/musicattributeproperty)

An identifier for a music item attribute property from a specific root type to a specific resulting value type.

[`class PartialMusicAsyncProperty`](/documentation/musickit/partialmusicasyncproperty)

A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.

[`class PartialMusicProperty`](/documentation/musickit/partialmusicproperty)

A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.

[`class AnyMusicProperty`](/documentation/musickit/anymusicproperty)

A type-erased identifier for a music item property, from any root type to any resulting value type.
