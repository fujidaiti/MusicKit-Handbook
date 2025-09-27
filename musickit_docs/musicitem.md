# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicitem

- [MusicKit](/documentation/musickit)
- MusicItem

Protocol

# MusicItem

A protocol with basic requirements for music items.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
protocol MusicItem : Sendable
```

## [Topics](/documentation/musickit/musicitem#topics)

### [Instance Properties](/documentation/musickit/musicitem#Instance-Properties)

[`var id: MusicItemID`](/documentation/musickit/musicitem/id)

The unique identifier for the music item.

**Required**

### [Instance Methods](/documentation/musickit/musicitem#Instance-Methods)

[`func with([PartialMusicAsyncProperty<Self>]) async throws -> Self`](/documentation/musickit/musicitem/with(_:))

Loads a new instance of the music item that includes the specified properties.

[`func with(PartialMusicAsyncProperty<Self>..., preferredSource: MusicPropertySource) async throws -> Self`](/documentation/musickit/musicitem/with(_:preferredsource:)-2hn42)

Loads a new instance of the music item that includes the specified properties.

[`func with([PartialMusicAsyncProperty<Self>], preferredSource: MusicPropertySource) async throws -> Self`](/documentation/musickit/musicitem/with(_:preferredsource:)-416sk)

Loads a new instance of the music item that includes the specified properties.

## [Relationships](/documentation/musickit/musicitem#relationships)

### [Inherits From](/documentation/musickit/musicitem#inherits-from)

- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

### [Inherited By](/documentation/musickit/musicitem#inherited-by)

- [`FilterableMusicItem`](/documentation/musickit/filterablemusicitem)
- [`MusicCatalogChartRequestable`](/documentation/musickit/musiccatalogchartrequestable)
- [`MusicCatalogSearchable`](/documentation/musickit/musiccatalogsearchable)
- [`MusicCatalogTopLevelResourceRequesting`](/documentation/musickit/musiccatalogtoplevelresourcerequesting)
- [`MusicLibraryAddable`](/documentation/musickit/musiclibraryaddable)
- [`MusicLibraryRequestable`](/documentation/musickit/musiclibraryrequestable)
- [`MusicLibrarySearchable`](/documentation/musickit/musiclibrarysearchable)
- [`MusicPersonalRecommendationItem`](/documentation/musickit/musicpersonalrecommendationitem)
- [`MusicPlaylistAddable`](/documentation/musickit/musicplaylistaddable)
- [`MusicRecentlyPlayedRequestable`](/documentation/musickit/musicrecentlyplayedrequestable)
- [`PlayableMusicItem`](/documentation/musickit/playablemusicitem)

### [Conforming Types](/documentation/musickit/musicitem#conforming-types)

- [`Album`](/documentation/musickit/album)
- [`Artist`](/documentation/musickit/artist)
- [`Curator`](/documentation/musickit/curator)
- [`Genre`](/documentation/musickit/genre)
- [`MusicCatalogSearchResponse.TopResult`](/documentation/musickit/musiccatalogsearchresponse/topresult)
- [`MusicLibrarySearchResponse.TopResult`](/documentation/musickit/musiclibrarysearchresponse/topresult)
- [`MusicPersonalRecommendation`](/documentation/musickit/musicpersonalrecommendation)
- [`MusicPersonalRecommendation.Item`](/documentation/musickit/musicpersonalrecommendation/item)
- [`MusicPlayer.Queue.Entry.Item`](/documentation/musickit/musicplayer/queue/entry/item-swift.enum)
- [`MusicVideo`](/documentation/musickit/musicvideo)
- [`Playlist`](/documentation/musickit/playlist)
- [`Playlist.Entry`](/documentation/musickit/playlist/entry)
- [`Playlist.Entry.Item`](/documentation/musickit/playlist/entry/item-swift.enum)
- [`RadioShow`](/documentation/musickit/radioshow)
- [`RecentlyPlayedMusicItem`](/documentation/musickit/recentlyplayedmusicitem)
- [`RecordLabel`](/documentation/musickit/recordlabel)
- [`Song`](/documentation/musickit/song)
- [`Station`](/documentation/musickit/station)
- [`Track`](/documentation/musickit/track)

## [See Also](/documentation/musickit/musicitem#see-also)

### [Utility](/documentation/musickit/musicitem#Utility)

[`struct MusicItemID`](/documentation/musickit/musicitemid)

An object that represents a unique identifier for a music item.

[`struct MusicItemCollection`](/documentation/musickit/musicitemcollection)

A collection of music items.

[`protocol MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)

A protocol for music items that allow loading additional properties that you can fetch asynchronously.

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
