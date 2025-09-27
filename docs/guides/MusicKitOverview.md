# MusicKit Framework Overview

> Source: https://developer.apple.com/documentation/musickit

Integrate your app with Apple Music.

**Availability:** iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+

## Overview

Use MusicKit to integrate your app with [Apple Music API](https://developer.apple.com/documentation/AppleMusicAPI), a web service you use to access information about music items in the Apple Music catalog. Using MusicKit, you can more easily build apps that tie into Apple Music.

The framework provides a model layer for accessing music items in Swift, as well as playback support so you can add music to your app. Additionally, it provides some related user interface elements, such as a view to display images that correspond to artwork for a music item, or a way to present music subscription offers to users who may not have an active Apple Music subscription.

**Important:** Users must grant permission for your app to access their music data. Add the [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) key to your app's `Info.plist` file, and include a description of how you intend to use the user's media. If this key isn't present, the system terminates your app when it tries to access the user's music.

Request permission for your app to use MusicKit with [`MusicAuthorization`](../services/Authorization.md#musicauthorization). Check specific capabilities for the current [`MusicSubscription`](../services/Authorization.md#musicsubscription) to ensure your music-related functionality is available to the user. Find music items using a search term with [`MusicCatalogSearchRequest`](../api-layer/CatalogSearchAPI.md#musiccatalogsearchrequest), or find music items using a filter with [`MusicCatalogResourceRequest`](../api-layer/CatalogResourceAPI.md#musiccatalogresourcerequest). Play music in your app with one of the two music players that MusicKit offers. Allow the user to begin a free trial for Apple Music from within your app by presenting a music subscription offer.

You can load content from an arbitrary Apple Music API endpoint with [`MusicDataRequest`](../api-layer/DataRequestAPI.md#musicdatarequest) to take further advantage of additional functionality available in Apple Music API.

## API Reference by Topics

### Essentials

**[Using Automatic Developer Token Generation for Apple Music API](https://developer.apple.com/documentation/musickit/using-automatic-token-generation-for-apple-music-api)**
Enable your app's integration with the MusicKit App Service in the developer portal.

**[Using MusicKit to Integrate with Apple Music](https://developer.apple.com/documentation/musickit/using_musickit_to_integrate_with_apple_music)**
Find an album in Apple Music that corresponds to a CD in a user's collection, and present the information for the album.

**[`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription)**
A message that tells people why the app is requesting access to their media library.

### Music Items

A set of value types represents each kind of music item.

- **[`struct Album`](../core-types/Album.md)** - A music item that represents an album.
- **[`struct Artist`](../core-types/Artist.md)** - A music item that represents an artist.
- **[`struct Curator`](../core-types/Curator.md)** - A music item that represents a curator.
- **[`struct Genre`](../core-types/Genre.md)** - A music item that represents a genre.
- **[`struct MusicVideo`](../core-types/MusicVideo.md)** - A music item that represents a music video.
- **[`struct Playlist`](../core-types/Playlist.md)** - A music item that represents a playlist.
- **[`struct RadioShow`](../core-types/RadioShow.md)** - A music item that represents a radio show.
- **[`struct RecordLabel`](../core-types/RecordLabel.md)** - A music item that represents a record label.
- **[`struct Song`](../core-types/Song.md)** - A music item that represents a song.
- **[`struct Station`](../core-types/Station.md)** - A music item that represents a station.
- **[`enum Track`](../core-types/Track.md)** - A music item that represents a track.

### Music Item Attributes

A set of structured attributes for music items.

- **[`enum ContentRating`](../utilities/Enumerations.md#contentrating)** - The rating of the content that potentially plays while playing a resource.
- **[`struct EditorialNotes`](../utilities/CoreDataTypes.md#editorialnotes)** - An object that represents editorial notes.
- **[`struct PreviewAsset`](../utilities/CoreDataTypes.md#previewasset)** - An object that represents a preview for resources.

### Catalog Search

The catalog search request allows your app to find music items in the Apple Music catalog.

- **[`struct MusicCatalogSearchRequest`](../api-layer/CatalogSearchAPI.md#musiccatalogsearchrequest)** - A request that your app uses to fetch items from the Apple Music catalog using a search term.
- **[`struct MusicCatalogSearchResponse`](../api-layer/CatalogSearchAPI.md#musiccatalogsearchresponse)** - An object that contains results for a catalog search request.
- **[`protocol MusicCatalogSearchable`](../protocols/RequestProtocols.md#musiccatalogsearchable)** - A protocol for music items that your app can fetch by using a catalog search request.

### Resource Loading Using Filters

The catalog resource request allows your app to load items using a specific filter. Each music item type has its own set of properties you can use as a filter for a catalog resource request when loading music items for your app.

- **[`struct MusicCatalogResourceRequest`](../api-layer/CatalogResourceAPI.md#musiccatalogresourcerequest)** - A request that your app uses to fetch items from the Apple Music catalog using a filter.
- **[`struct MusicCatalogResourceResponse`](../api-layer/CatalogResourceAPI.md#musiccatalogresourceresponse)** - An object that contains results for a catalog resource request.

#### Filter Protocols
- **[`protocol AlbumFilter`](../protocols/FilterProtocols.md#albumfilter)** - Album properties your app uses as a filter for a catalog resource request.
- **[`protocol ArtistFilter`](../protocols/FilterProtocols.md#artistfilter)** - Artist properties your app uses as a filter for a catalog resource request.
- **[`protocol CuratorFilter`](../protocols/FilterProtocols.md#curatorfilter)** - Curator properties your app uses as a filter for a catalog resource request.
- **[`protocol GenreFilter`](../protocols/FilterProtocols.md#genrefilter)** - Genre properties your app uses as a filter for a catalog resource request.
- **[`protocol MusicVideoFilter`](../protocols/FilterProtocols.md#musicvideofilter)** - Music video properties your app uses as a filter for a catalog resource request.
- **[`protocol PlaylistFilter`](../protocols/FilterProtocols.md#playlistfilter)** - Playlist properties your app uses as a filter for a catalog resource request.
- **[`protocol RadioShowFilter`](../protocols/FilterProtocols.md#radioshowfilter)** - Radio Show properties your app uses as a filter for a catalog resource request.
- **[`protocol RecordLabelFilter`](../protocols/FilterProtocols.md#recordlabelfilter)** - The set of record label properties your app uses as a filter for a catalog resource request.
- **[`protocol SongFilter`](../protocols/FilterProtocols.md#songfilter)** - Song properties your app uses as a filter for a catalog resource request.
- **[`protocol StationFilter`](../protocols/FilterProtocols.md#stationfilter)** - The set of station properties your app uses as a filter for a catalog resource request.
- **[`protocol FilterableMusicItem`](../protocols/FilterProtocols.md#filterablemusicitem)** - A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.

### General Purpose Data Request

- **[`struct MusicDataRequest`](../api-layer/DataRequestAPI.md#musicdatarequest)** - A request for loading data from an arbitrary Apple Music API endpoint.
- **[`struct MusicDataResponse`](../api-layer/DataRequestAPI.md#musicdataresponse)** - An object containing results for a data request.

### Playback

- **[`class ApplicationMusicPlayer`](../services/MusicPlayers.md#applicationmusicplayer)** - An object your app uses to play music in a way that doesn't affect the Music app's state.
- **[`class SystemMusicPlayer`](../services/MusicPlayers.md#systemmusicplayer)** - An object your app uses to play music by controlling the Music app's state.
- **[`class MusicPlayer`](../services/MusicPlayers.md#musicplayer)** - An object your app uses to play music.
- **[`protocol PlayableMusicItem`](../protocols/PlaybackProtocols.md#playablemusicitem)** - A set of properties that a music player uses to initiate playback for a music item.
- **[`struct PlayParameters`](../utilities/CoreDataTypes.md#playparameters)** - An opaque object that represents parameters to initiate playback of a playable music item using a music player.

### Artwork

- **[`struct Artwork`](../utilities/CoreDataTypes.md#artwork)** - An object that represents artwork for a music item.
- **[`struct ArtworkImage`](../utilities/CoreDataTypes.md#artworkimage)** - A view that displays the image for a music item's artwork.

### Authorization

Before you can use any of the functionality of the framework, you need to request the user's informed consent for your app to access their music data.

- **[`struct MusicAuthorization`](../services/Authorization.md#musicauthorization)** - A type that allows you to request the user's informed consent for your app to access their music data.

### Apple Music Subscription

- **[`struct MusicSubscription`](../services/Authorization.md#musicsubscription)** - A representation of the current state of the user's subscription to Apple Music.
- **[`struct MusicSubscriptionOffer`](../services/Authorization.md#musicsubscriptionoffer)** - A type for grouping other types for showing subscription offers for Apple Music.

### Token Management

The framework manages tokens for accessing Apple Music API automatically by default, but you can generate your own developer token by creating a class that inherits from the token provider type alias.

- **[`typealias MusicTokenProvider`](../services/TokenManagement.md#musictokenprovider)** - An object that music requests use to access Apple Music API.
- **[`protocol MusicDeveloperTokenProvider`](../services/TokenManagement.md#musicdevelopertokenprovider)** - A set of methods that music requests use to access Apple Music API.
- **[`class MusicUserTokenProvider`](../services/TokenManagement.md#musicusertokenprovider)** - A class that music requests use to fetch user tokens your app requires to access Apple Music API.
- **[`struct MusicTokenRequestOptions`](../services/TokenManagement.md#musictokenrequestoptions)** - Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.
- **[`enum MusicTokenRequestError`](../services/TokenManagement.md#musictokenrequesterror)** - An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.
- **[`class DefaultMusicTokenProvider`](../services/TokenManagement.md#defaultmusictokenprovider)** - The default token provider that music requests use to access Apple Music API.

### Music Library

- **[`class MusicLibrary`](../services/MusicLibrary.md#musiclibrary)** - An object your app uses to access the user's music library.

#### Library Filters
- **[`protocol LibraryAlbumFilter`](../protocols/FilterProtocols.md#libraryalbumfilter)** - Album properties your app uses as a filter for a library request.
- **[`protocol LibraryArtistFilter`](../protocols/FilterProtocols.md#libraryartistfilter)** - Artist properties your app uses as a filter for a library request.
- **[`protocol LibraryGenreFilter`](../protocols/FilterProtocols.md#librarygenrefilter)** - Genre properties your app uses as a filter for a library request.
- **[`protocol LibraryMusicVideoFilter`](../protocols/FilterProtocols.md#librarymusicvideofilter)** - Music video properties your app uses as a filter for a library request.
- **[`protocol LibraryPlaylistEntryFilter`](../protocols/FilterProtocols.md#libraryplaylistentryfilter)** - Playlist entry properties your app uses as a filter for a library request.
- **[`protocol LibraryPlaylistFilter`](../protocols/FilterProtocols.md#libraryplaylistfilter)** - Playlist properties your app uses as a filter for a library request.
- **[`protocol LibrarySongFilter`](../protocols/FilterProtocols.md#librarysongfilter)** - Song properties your app uses as a filter for a library request.
- **[`protocol LibraryTrackFilter`](../protocols/FilterProtocols.md#librarytrackfilter)** - Track properties your app uses as a filter for a library request.

#### Library Sort Properties
- **[`protocol LibraryAlbumSortProperties`](../protocols/SortProtocols.md#libraryalbumsortproperties)** - Album properties your app uses to sort results for a library request.
- **[`protocol LibraryArtistSortProperties`](../protocols/SortProtocols.md#libraryartistsortproperties)** - Artist properties your app uses to sort results for a library request.
- **[`protocol LibraryGenreSortProperties`](../protocols/SortProtocols.md#librarygenresortproperties)** - Genre properties your app uses to sort results for a library request.
- **[`protocol LibraryMusicVideoSortProperties`](../protocols/SortProtocols.md#librarymusicvideosortproperties)** - Music video properties your app uses to sort results for a library request.
- **[`protocol LibraryPlaylistEntrySortProperties`](../protocols/SortProtocols.md#libraryplaylistentrysortproperties)** - Playlist entry properties your app uses to sort results for a library request.
- **[`protocol LibraryPlaylistSortProperties`](../protocols/SortProtocols.md#libraryplaylistsortproperties)** - Playlist properties your app uses to sort results for a library request.
- **[`protocol LibrarySongSortProperties`](../protocols/SortProtocols.md#librarysongsortproperties)** - Song properties your app uses to sort results for a library request.
- **[`protocol LibraryTrackSortProperties`](../protocols/SortProtocols.md#librarytracksortproperties)** - Track properties your app uses to sort results for a library request.

### Catalog Charts and Recommendations

- **[`struct MusicCatalogChart`](../api-layer/CatalogChartsAPI.md#musiccatalogchart)** - An object that contains popular items in the Apple Music catalog.
- **[`struct MusicCatalogChartsRequest`](../api-layer/CatalogChartsAPI.md#musiccatalogchartsrequest)** - A request that your app uses to fetch the most popular items in the Apple Music catalog.
- **[`struct MusicCatalogChartsResponse`](../api-layer/CatalogChartsAPI.md#musiccatalogchartsresponse)** - An object that contains results for a catalog charts request.
- **[`struct MusicPersonalRecommendation`](../api-layer/PersonalRecommendationsAPI.md#musicpersonalrecommendation)** - An object that contains recommended items based on the user's library and listening history.
- **[`struct MusicPersonalRecommendationsRequest`](../api-layer/PersonalRecommendationsAPI.md#musicpersonalrecommendationsrequest)** - A request that your app uses to fetch music recommendations based on the user's library and listening history.
- **[`struct MusicPersonalRecommendationsResponse`](../api-layer/PersonalRecommendationsAPI.md#musicpersonalrecommendationsresponse)** - An object that contains results for a personal recommendations request.

### Search Suggestions

- **[`struct MusicCatalogSearchSuggestionsRequest`](../api-layer/CatalogSearchAPI.md#musiccatalogsearchsuggestionsrequest)** - A request that your app uses to fetch suggestions from the Apple Music catalog using a search term.
- **[`struct MusicCatalogSearchSuggestionsResponse`](../api-layer/CatalogSearchAPI.md#musiccatalogsearchsuggestionsresponse)** - An object that contains results for a catalog search suggestions request.

### Recently Played

- **[`struct MusicRecentlyPlayedRequest`](../api-layer/RecentlyPlayedAPI.md#musicrecentlyplayedrequest)** - A request that your app uses to fetch items the user has recently played.
- **[`struct MusicRecentlyPlayedResponse`](../api-layer/RecentlyPlayedAPI.md#musicrecentlyplayedresponse)** - An object that contains items the user has recently played.
- **[`typealias MusicRecentlyPlayedContainerRequest`](../api-layer/RecentlyPlayedAPI.md#musicrecentlyplayedcontainerrequest)** - A request that your app uses to fetch albums, playlists or stations that the user has recently played.
- **[`typealias MusicRecentlyPlayedContainerResponse`](../api-layer/RecentlyPlayedAPI.md#musicrecentlyplayedcontainerresponse)** - An object that contains albums, playlists or stations that the user has recently played.
- **[`enum RecentlyPlayedMusicItem`](../utilities/Enumerations.md#recentlyplayedmusicitem)** - An item that represents an album, a playlist, or a station that the user has recently played.

### Library Requests

- **[`struct MusicLibraryRequest`](../api-layer/LibraryAPI.md#musiclibraryrequest)** - A request that your app uses to fetch items from the user's music library.
- **[`struct MusicLibraryResponse`](../api-layer/LibraryAPI.md#musiclibraryresponse)** - An object that contains results for a library request.
- **[`struct MusicLibrarySearchRequest`](../api-layer/LibraryAPI.md#musiclibrarysearchrequest)** - A request that your app uses to fetch items from user's library using a search term.
- **[`struct MusicLibrarySearchResponse`](../api-layer/LibraryAPI.md#musiclibrarysearchresponse)** - An object that contains results for a library search request.
- **[`struct MusicLibrarySection`](../api-layer/LibraryAPI.md#musiclibrarysection)** - A section for a library sectioned response.
- **[`struct MusicLibrarySectionedRequest`](../api-layer/LibraryAPI.md#musiclibrarysectionedrequest)** - A request that your app uses to fetch items grouped by sections from the user's music library.
- **[`struct MusicLibrarySectionedResponse`](../api-layer/LibraryAPI.md#musiclibrarysectionedresponse)** - An object that contains results for a library sectioned request.
- **[`struct TitledSection`](../utilities/SupportTypes.md#titledsection)** - A section you can use to request items from the library grouped by title.

### Utility Types and Protocols

- **[`protocol MusicItem`](../protocols/UtilityProtocols.md#musicitem)** - A protocol with basic requirements for music items.
- **[`struct MusicItemID`](../utilities/CoreDataTypes.md#musicitemid)** - An object that represents a unique identifier for a music item.
- **[`struct MusicItemCollection`](../utilities/CoreDataTypes.md#musicitemcollection)** - A collection of music items.
- **[`protocol MusicPropertyContainer`](../protocols/UtilityProtocols.md#musicpropertycontainer)** - A protocol for music items that allow loading additional properties that you can fetch asynchronously.

#### Property System
- **[`class MusicRelationshipProperty`](../utilities/PropertyManagement.md#musicrelationshipproperty)** - An identifier for a music item relationship property from a specific root type to a specific value type for the element of the resulting collection.
- **[`class MusicExtendedAttributeProperty`](../utilities/PropertyManagement.md#musicextendedattributeproperty)** - An identifier for a music item extended attribute property from a specific root type to a specific resulting value type.
- **[`class MusicAttributeProperty`](../utilities/PropertyManagement.md#musicattributeproperty)** - An identifier for a music item attribute property from a specific root type to a specific resulting value type.
- **[`class PartialMusicAsyncProperty`](../utilities/PropertyManagement.md#partialmusicasyncproperty)** - A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.
- **[`class PartialMusicProperty`](../utilities/PropertyManagement.md#partialmusicproperty)** - A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.
- **[`class AnyMusicProperty`](../utilities/PropertyManagement.md#anymusicproperty)** - A type-erased identifier for a music item property, from any root type to any resulting value type.

### Protocol Capabilities

- **[`protocol MusicCatalogChartRequestable`](../protocols/RequestProtocols.md#musiccatalogchartrequestable)** - A protocol for music items that your app can fetch by using a catalog charts request.
- **[`protocol MusicCatalogTopLevelResourceRequesting`](../protocols/RequestProtocols.md#musiccatalogtoplevelresourcerequesting)** - A protocol for music items that your app can fetch by using a catalog resource request without any filter.
- **[`protocol MusicLibraryAddable`](../protocols/PlaybackProtocols.md#musiclibraryaddable)** - A protocol for music items that your app can add to the music library.
- **[`protocol MusicLibraryRequestable`](../protocols/RequestProtocols.md#musiclibraryrequestable)** - A protocol for music items that your app can fetch by using a library request.
- **[`protocol MusicLibrarySearchable`](../protocols/RequestProtocols.md#musiclibrarysearchable)** - A protocol for music items that your app can fetch by using a library search request.
- **[`protocol MusicLibrarySectionRequestable`](../protocols/RequestProtocols.md#musiclibrarysectionrequestable)** - A protocol for types your app uses as sections when fetching items using a library sectioned request.
- **[`protocol MusicPersonalRecommendationItem`](../protocols/RequestProtocols.md#musicpersonalrecommendationitem)** - A protocol for music items that your app can fetch by using a personal recommendations request.
- **[`protocol MusicPlaylistAddable`](../protocols/PlaybackProtocols.md#musicplaylistaddable)** - A protocol for music items that your app can add to a playlist.
- **[`protocol MusicRecentlyPlayedRequestable`](../protocols/RequestProtocols.md#musicrecentlyplayedrequestable)** - A protocol for music items that your app can fetch by using a recently played request.

#### Library Request Filter Value Types
- **[`protocol MusicLibraryRequestFilterValueEquatable`](../protocols/UtilityProtocols.md#musiclibraryrequestfiltervalueequatable)** - A protocol for types of values your app can use with equality filters when fetching items using a music library request.
- **[`protocol MusicLibraryRequestFilterValueMembershipComparable`](../protocols/UtilityProtocols.md#musiclibraryrequestfiltervaluemembershipcomparable)** - A protocol for types of values your app can use with membership filters when fetching items using a music library request.

### Enumerations

- **[`enum AudioVariant`](../utilities/Enumerations.md#audiovariant)** - Variants that indicate the quality of audio available for an item.
- **[`enum MusicCatalogChartKind`](../api-layer/CatalogChartsAPI.md#musiccatalogchartkind)** - The available kinds of catalog charts.
- **[`enum MusicPropertySource`](../utilities/Enumerations.md#musicpropertysource)** - An enumeration that specifies which source to use when requesting properties and relationships.

## Related Documentation

### Apple Frameworks
- **[Media Player](https://developer.apple.com/documentation/MediaPlayer)** - Find and play songs, audio podcasts, audio books, and more from within your app.
- **[Apple Music API](https://developer.apple.com/documentation/AppleMusicAPI)** - Integrate streaming music with catalog and personal content.