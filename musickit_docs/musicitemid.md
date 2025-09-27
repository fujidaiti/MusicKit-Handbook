# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicitemid

- [MusicKit](/documentation/musickit)
- MusicItemID

Structure

# MusicItemID

An object that represents a unique identifier for a music item.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
@frozen
struct MusicItemID
```

## [Topics](/documentation/musickit/musicitemid#topics)

### [Initializers](/documentation/musickit/musicitemid#Initializers)

[`init(String)`](/documentation/musickit/musicitemid/init(_:))

Creates a music item identifier with a string.

## [Relationships](/documentation/musickit/musicitemid#relationships)

### [Conforms To](/documentation/musickit/musicitemid#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`ExpressibleByExtendedGraphemeClusterLiteral`](/documentation/Swift/ExpressibleByExtendedGraphemeClusterLiteral)
- [`ExpressibleByStringLiteral`](/documentation/Swift/ExpressibleByStringLiteral)
- [`ExpressibleByUnicodeScalarLiteral`](/documentation/Swift/ExpressibleByUnicodeScalarLiteral)
- [`Hashable`](/documentation/Swift/Hashable)
- [`MusicLibraryRequestFilterValueEquatable`](/documentation/musickit/musiclibraryrequestfiltervalueequatable)
- [`MusicLibraryRequestFilterValueMembershipComparable`](/documentation/musickit/musiclibraryrequestfiltervaluemembershipcomparable)
- [`RawRepresentable`](/documentation/Swift/RawRepresentable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/musicitemid#see-also)

### [Utility](/documentation/musickit/musicitemid#Utility)

[`protocol MusicItem`](/documentation/musickit/musicitem)

A protocol with basic requirements for music items.

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
