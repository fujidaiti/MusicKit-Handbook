# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiccatalogsearchresponse

- [MusicKit](/documentation/musickit)
- MusicCatalogSearchResponse

Structure

# MusicCatalogSearchResponse

An object that contains results for a catalog search request.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicCatalogSearchResponse
```

## [Topics](/documentation/musickit/musiccatalogsearchresponse#topics)

### [Instance Properties](/documentation/musickit/musiccatalogsearchresponse#Instance-Properties)

[`let albums: MusicItemCollection<Album>`](/documentation/musickit/musiccatalogsearchresponse/albums)

A collection of albums.

[`let artists: MusicItemCollection<Artist>`](/documentation/musickit/musiccatalogsearchresponse/artists)

A collection of artists.

[`let curators: MusicItemCollection<Curator>`](/documentation/musickit/musiccatalogsearchresponse/curators)

A collection of curators.

[`let musicVideos: MusicItemCollection<MusicVideo>`](/documentation/musickit/musiccatalogsearchresponse/musicvideos)

A collection of music videos.

[`let playlists: MusicItemCollection<Playlist>`](/documentation/musickit/musiccatalogsearchresponse/playlists)

A collection of playlists.

[`let radioShows: MusicItemCollection<RadioShow>`](/documentation/musickit/musiccatalogsearchresponse/radioshows)

A collection of radio shows.

[`let recordLabels: MusicItemCollection<RecordLabel>`](/documentation/musickit/musiccatalogsearchresponse/recordlabels)

A collection of record labels.

[`let songs: MusicItemCollection<Song>`](/documentation/musickit/musiccatalogsearchresponse/songs)

A collection of songs.

[`let stations: MusicItemCollection<Station>`](/documentation/musickit/musiccatalogsearchresponse/stations)

A collection of stations.

[`let topResults: MusicItemCollection<MusicCatalogSearchResponse.TopResult>`](/documentation/musickit/musiccatalogsearchresponse/topresults)

A collection of top results.

### [Enumerations](/documentation/musickit/musiccatalogsearchresponse#Enumerations)

[`enum TopResult`](/documentation/musickit/musiccatalogsearchresponse/topresult)

An item that represents one of the top results in a catalog search response.

## [Relationships](/documentation/musickit/musiccatalogsearchresponse#relationships)

### [Conforms To](/documentation/musickit/musiccatalogsearchresponse#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)

## [See Also](/documentation/musickit/musiccatalogsearchresponse#see-also)

### [Catalog Search](/documentation/musickit/musiccatalogsearchresponse#Catalog-Search)

[`struct MusicCatalogSearchRequest`](/documentation/musickit/musiccatalogsearchrequest)

A request that your app uses to fetch items from the Apple Music catalog using a search term.

[`protocol MusicCatalogSearchable`](/documentation/musickit/musiccatalogsearchable)

A protocol for music items that your app can fetch by using a catalog search request.
