# Property Management

> Source: Multiple Apple MusicKit documentation pages

This section contains the types used for managing properties and relationships of music items, including loading additional data asynchronously and handling property identifiers with various levels of type erasure.

## MusicPropertyContainer
- **Swift Declaration**: `protocol MusicPropertyContainer`
- **Purpose**: A protocol for music items that allow loading additional properties that you can fetch asynchronously.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicpropertycontainer)
- **Methods**:
  - `func with([PartialMusicAsyncProperty<Self>]) async throws -> Self`: Loads a new instance of the music item that includes the specified properties (default implementation provided)
  - `func with([PartialMusicAsyncProperty<Self>], preferredSource: MusicPropertySource) async throws -> Self`: Loads a new instance with properties from a preferred source
  - `func with(PartialMusicAsyncProperty<Self>..., preferredSource: MusicPropertySource) async throws -> Self`: Loads a new instance with variadic properties from a preferred source
- **Usage**: Implemented by music item types (Album, Artist, Song, etc.) to enable loading additional properties and relationships asynchronously. Used to fetch detailed information that isn't included in the basic item representation.
- **Conforming Types**: `Album`, `Artist`, `Curator`, `Genre`, `MusicVideo`, `Playlist`, `RadioShow`, `RecordLabel`, `Song`, `Station`, `Track`, and various entry/item types

## MusicRelationshipProperty
- **Swift Declaration**: `class MusicRelationshipProperty<Root, RelatedMusicItemType> where RelatedMusicItemType : MusicItem, RelatedMusicItemType : Decodable`
- **Purpose**: An identifier for a music item relationship property from a specific root type to a specific value type for the element of the resulting collection.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicrelationshipproperty)
- **Properties**: Inherits from `PartialMusicAsyncProperty`
- **Methods**: Inherited from parent classes
- **Usage**: Used to identify and fetch related music items, such as an artist's albums, a song's artists, or an album's tracks. Provides type-safe access to relationship data that can be loaded asynchronously.
- **Inherits From**: `PartialMusicAsyncProperty`
- **Conforms To**: `CustomStringConvertible`, `Equatable`, `Hashable`, `Sendable`

## MusicExtendedAttributeProperty
- **Swift Declaration**: `class MusicExtendedAttributeProperty<Root, Value> where Value : Decodable`
- **Purpose**: An identifier for a music item extended attribute property from a specific root type to a specific resulting value type.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicextendedattributeproperty)
- **Properties**: Inherits from `PartialMusicAsyncProperty`
- **Methods**: Inherited from parent classes
- **Usage**: Used to identify and fetch extended attributes that provide additional metadata beyond basic properties, such as artist URLs, audio variants, or other supplemental information.
- **Inherits From**: `PartialMusicAsyncProperty`
- **Conforms To**: `CustomStringConvertible`, `Equatable`, `Hashable`, `Sendable`

## MusicAttributeProperty
- **Swift Declaration**: `class MusicAttributeProperty<Root, Value> where Value : Decodable`
- **Purpose**: An identifier for a music item attribute property from a specific root type to a specific resulting value type.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicattributeproperty)
- **Properties**: Inherits from `PartialMusicProperty`
- **Methods**: Inherited from parent classes
- **Usage**: Used to identify basic attribute properties of music items that can be accessed synchronously, such as titles, names, or other fundamental properties.
- **Inherits From**: `PartialMusicProperty`
- **Conforms To**: `CustomStringConvertible`, `Equatable`, `Hashable`, `Sendable`

## PartialMusicAsyncProperty
- **Swift Declaration**: `class PartialMusicAsyncProperty<Root>`
- **Purpose**: A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/partialmusicasyncproperty)
- **Properties**: Inherits from `PartialMusicProperty`
- **Methods**: Inherited from parent classes
- **Usage**: Base class for properties that can be loaded asynchronously. Provides partial type erasure while maintaining the root type constraint, enabling asynchronous property loading with type safety.
- **Inherits From**: `PartialMusicProperty`
- **Inherited By**: `MusicExtendedAttributeProperty`, `MusicRelationshipProperty`
- **Conforms To**: `Equatable`, `Hashable`, `Sendable`

## PartialMusicProperty
- **Swift Declaration**: `class PartialMusicProperty<Root>`
- **Purpose**: A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/partialmusicproperty)
- **Properties**: Contains extensive static properties for various music item relationships and attributes (albums, artists, genres, tracks, etc.)
- **Methods**: Inherited from parent classes
- **Usage**: Provides static property identifiers for all supported music item relationships and attributes. Contains predefined properties like `.albums`, `.artists`, `.genres`, `.tracks`, `.audioVariants`, etc. for different music item types.
- **Static Properties**: Extensive collection including:
  - Relationship properties: `.albums`, `.artists`, `.genres`, `.tracks`, `.playlists`, `.musicVideos`, etc.
  - Extended attributes: `.audioVariants`, `.artistURL`
  - Association properties: `.featuredArtists`, `.similarArtists`, `.moreByArtist`, etc.
- **Inherits From**: `AnyMusicProperty`
- **Inherited By**: `MusicAttributeProperty`, `PartialMusicAsyncProperty`
- **Conforms To**: `Equatable`, `Hashable`, `Sendable`

## AnyMusicProperty
- **Swift Declaration**: `class AnyMusicProperty`
- **Purpose**: A type-erased identifier for a music item property, from any root type to any resulting value type.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/anymusicproperty)
- **Properties**: Base type with no specific properties
- **Methods**: No specific methods documented
- **Usage**: Base class for all music property identifiers. Provides complete type erasure, allowing properties to be stored and passed around without type constraints.
- **Inherited By**: `PartialMusicProperty`
- **Conforms To**: `Equatable`, `Hashable`, `Sendable`