# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/partialmusicasyncproperty

- [MusicKit](/documentation/musickit)
- PartialMusicAsyncProperty

Class

# PartialMusicAsyncProperty

A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
class PartialMusicAsyncProperty<Root>
```

## [Relationships](/documentation/musickit/partialmusicasyncproperty#relationships)

### [Inherits From](/documentation/musickit/partialmusicasyncproperty#inherits-from)

- [`PartialMusicProperty`](/documentation/musickit/partialmusicproperty)

### [Inherited By](/documentation/musickit/partialmusicasyncproperty#inherited-by)

- [`MusicExtendedAttributeProperty`](/documentation/musickit/musicextendedattributeproperty)
- [`MusicRelationshipProperty`](/documentation/musickit/musicrelationshipproperty)

### [Conforms To](/documentation/musickit/partialmusicasyncproperty#conforms-to)

- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/partialmusicasyncproperty#see-also)

### [Utility](/documentation/musickit/partialmusicasyncproperty#Utility)

[`protocol MusicItem`](/documentation/musickit/musicitem)

A protocol with basic requirements for music items.

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

[`class PartialMusicProperty`](/documentation/musickit/partialmusicproperty)

A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.

[`class AnyMusicProperty`](/documentation/musickit/anymusicproperty)

A type-erased identifier for a music item property, from any root type to any resulting value type.
