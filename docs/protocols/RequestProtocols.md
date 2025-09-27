# Request Protocols

> Source: Multiple Apple MusicKit documentation pages

These protocols define capabilities for music items that can be fetched through various types of requests in MusicKit, including catalog searches, library requests, and recommendation requests.

## Overview

The request protocols enable developers to work with music items that can be retrieved through different types of MusicKit requests. These protocols categorize music items based on how they can be fetched from the Apple Music catalog, user's library, or recommendation systems.

## Protocols

### MusicCatalogSearchable
- **Swift Declaration**: `protocol MusicCatalogSearchable : MusicItem`
- **Purpose**: A protocol for music items that your app can fetch by using a catalog search request.
- **Source**: [https://developer.apple.com/documentation/musickit/musiccatalogsearchable](https://developer.apple.com/documentation/musickit/musiccatalogsearchable)
- **Requirements**: None specified beyond MusicItem inheritance
- **Used By**:
  - [`Album`](../core-types/Album.md)
  - [`Artist`](../core-types/Artist.md)
  - [`Curator`](../core-types/Curator.md)
  - [`MusicVideo`](../core-types/MusicVideo.md)
  - [`Playlist`](../core-types/Playlist.md)
  - [`RadioShow`](../core-types/RadioShow.md)
  - [`RecordLabel`](../core-types/RecordLabel.md)
  - [`Song`](../core-types/Song.md)
  - [`Station`](../core-types/Station.md)

### MusicCatalogChartRequestable
- **Swift Declaration**: `protocol MusicCatalogChartRequestable : MusicItem`
- **Purpose**: A protocol for music items that your app can fetch by using a catalog charts request.
- **Source**: [https://developer.apple.com/documentation/musickit/musiccatalogchartrequestable](https://developer.apple.com/documentation/musickit/musiccatalogchartrequestable)
- **Requirements**: None specified beyond MusicItem inheritance
- **Used By**:
  - [`Album`](../core-types/Album.md)
  - [`MusicVideo`](../core-types/MusicVideo.md)
  - [`Playlist`](../core-types/Playlist.md)
  - [`Song`](../core-types/Song.md)

### MusicCatalogTopLevelResourceRequesting
- **Swift Declaration**: `protocol MusicCatalogTopLevelResourceRequesting : MusicItem`
- **Purpose**: A protocol for music items that your app can fetch by using a catalog resource request without any filter.
- **Source**: [https://developer.apple.com/documentation/musickit/musiccatalogtoplevelresourcerequesting](https://developer.apple.com/documentation/musickit/musiccatalogtoplevelresourcerequesting)
- **Requirements**: None specified beyond MusicItem inheritance
- **Used By**:
  - [`Genre`](../core-types/Genre.md)

### MusicLibraryRequestable
- **Swift Declaration**: `protocol MusicLibraryRequestable : MusicItem`
- **Purpose**: A protocol for music items that your app can fetch by using a library request.
- **Source**: [https://developer.apple.com/documentation/musickit/musiclibraryrequestable](https://developer.apple.com/documentation/musickit/musiclibraryrequestable)
- **Requirements**:
  - `associatedtype LibraryFilter` (Required) - The associated type that contains the set of music item properties your app uses as a filter for a library request.
  - `associatedtype LibrarySortProperties` (Required) - The associated type that contains the set of properties your app uses to sort results for a library request.
- **Used By**:
  - [`Album`](../core-types/Album.md)
  - [`Artist`](../core-types/Artist.md)
  - [`Genre`](../core-types/Genre.md)
  - [`MusicVideo`](../core-types/MusicVideo.md)
  - [`Playlist`](../core-types/Playlist.md)
  - [`Playlist.Entry`](../core-types/Playlist.md#playlist-entry)
  - [`Song`](../core-types/Song.md)
  - [`Track`](../core-types/Track.md)

### MusicLibrarySearchable
- **Swift Declaration**: `protocol MusicLibrarySearchable : MusicItem`
- **Purpose**: A protocol for music items that your app can fetch by using a library search request.
- **Source**: [https://developer.apple.com/documentation/musickit/musiclibrarysearchable](https://developer.apple.com/documentation/musickit/musiclibrarysearchable)
- **Requirements**: None specified beyond MusicItem inheritance
- **Used By**:
  - [`Album`](../core-types/Album.md)
  - [`Artist`](../core-types/Artist.md)
  - [`MusicVideo`](../core-types/MusicVideo.md)
  - [`Playlist`](../core-types/Playlist.md)
  - [`Song`](../core-types/Song.md)

### MusicLibrarySectionRequestable
- **Swift Declaration**: `protocol MusicLibrarySectionRequestable`
- **Purpose**: A protocol for types your app uses as sections when fetching items using a library sectioned request.
- **Source**: [https://developer.apple.com/documentation/musickit/musiclibrarysectionrequestable](https://developer.apple.com/documentation/musickit/musiclibrarysectionrequestable)
- **Requirements**: None specified (does not inherit from MusicItem)
- **Used By**:
  - [`Album`](../core-types/Album.md)
  - [`Artist`](../core-types/Artist.md)
  - [`Genre`](../core-types/Genre.md)
  - [`Playlist`](../core-types/Playlist.md)
  - [`TitledSection`](../utilities/SupportTypes.md#titledsection)

### MusicRecentlyPlayedRequestable
- **Swift Declaration**: `protocol MusicRecentlyPlayedRequestable : MusicItem`
- **Purpose**: A protocol for music items that your app can fetch by using a recently played request.
- **Source**: [https://developer.apple.com/documentation/musickit/musicrecentlyplayedrequestable](https://developer.apple.com/documentation/musickit/musicrecentlyplayedrequestable)
- **Requirements**: None specified beyond MusicItem inheritance
- **Used By**:
  - [`MusicVideo`](../core-types/MusicVideo.md)
  - [`RecentlyPlayedMusicItem`](../utilities/Enumerations.md#recentlyplayedmusicitem)
  - [`Song`](../core-types/Song.md)
  - [`Station`](../core-types/Station.md)
  - [`Track`](../core-types/Track.md)

### MusicPersonalRecommendationItem
- **Swift Declaration**: `protocol MusicPersonalRecommendationItem : MusicItem`
- **Purpose**: A protocol for music items that your app can fetch by using a personal recommendations request.
- **Source**: [https://developer.apple.com/documentation/musickit/musicpersonalrecommendationitem](https://developer.apple.com/documentation/musickit/musicpersonalrecommendationitem)
- **Requirements**: None specified beyond MusicItem inheritance
- **Used By**:
  - [`Album`](../core-types/Album.md)
  - [`Playlist`](../core-types/Playlist.md)
  - [`Station`](../core-types/Station.md)