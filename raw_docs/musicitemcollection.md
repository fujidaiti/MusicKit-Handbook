# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicitemcollection

- [MusicKit](/documentation/musickit)
- MusicItemCollection

Structure

# MusicItemCollection

A collection of music items.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicItemCollection<MusicItemType> where MusicItemType : MusicItem
```

## [Topics](/documentation/musickit/musicitemcollection#topics)

### [Operators](/documentation/musickit/musicitemcollection#Operators)

[`static func += (inout MusicItemCollection<MusicItemType>, MusicItemCollection<MusicItemType>)`](/documentation/musickit/musicitemcollection/+=(_:_:))

Appends contents of a collection representing a next batch, in the right hand side, to the existing collection on the left hand side.

### [Initializers](/documentation/musickit/musicitemcollection#Initializers)

[`init<S>(S)`](/documentation/musickit/musicitemcollection/init(_:))

### [Instance Properties](/documentation/musickit/musicitemcollection#Instance-Properties)

[`var hasNextBatch: Bool`](/documentation/musickit/musicitemcollection/hasnextbatch)

A Boolean value that indicates whether the collection has information that allows it to fetch a subsequent batch of items.

[`var title: String?`](/documentation/musickit/musicitemcollection/title)

An optional title for the collection.

### [Instance Methods](/documentation/musickit/musicitemcollection#Instance-Methods)

[`func nextBatch(limit: Int?) async throws -> MusicItemCollection<MusicItemType>?`](/documentation/musickit/musicitemcollection/nextbatch(limit:)-432i0)

Fetches the next batch of items asynchronously.

[`func nextBatch(limit: Int?) async throws -> MusicItemCollection<MusicItemType>?`](/documentation/musickit/musicitemcollection/nextbatch(limit:)-ywue)

Fetches the next batch of items asynchronously.

## [Relationships](/documentation/musickit/musicitemcollection#relationships)

### [Conforms To](/documentation/musickit/musicitemcollection#conforms-to)

- [`BidirectionalCollection`](/documentation/Swift/BidirectionalCollection)
- [`Collection`](/documentation/Swift/Collection)
- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`ExpressibleByArrayLiteral`](/documentation/Swift/ExpressibleByArrayLiteral)
- [`Hashable`](/documentation/Swift/Hashable)
- [`RandomAccessCollection`](/documentation/Swift/RandomAccessCollection)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
- [`Sequence`](/documentation/Swift/Sequence)

## [See Also](/documentation/musickit/musicitemcollection#see-also)

### [Utility](/documentation/musickit/musicitemcollection#Utility)

[`protocol MusicItem`](/documentation/musickit/musicitem)

A protocol with basic requirements for music items.

[`struct MusicItemID`](/documentation/musickit/musicitemid)

An object that represents a unique identifier for a music item.

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
