# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit

Framework

# MusicKit

Integrate your app with Apple Music.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

## [Overview](/documentation/musickit#Overview)

Use MusicKit to integrate your app with [Apple Music
API](/documentation/AppleMusicAPI), a web service you use to access information
about music items in the Apple Music catalog. Using MusicKit, you can more
easily build apps that tie into Apple Music.

The framework provides a model layer for accessing music items in Swift, as well
as playback support so you can add music to your app. Additionally, it provides
some related user interface elements, such as a view to display images that
correspond to artwork for a music item, or a way to present music subscription
offers to users who may not have an active Apple Music subscription.

Important

Users must grant permission for your app to access their music data. Add the
[NSAppleMusicUsageDescription](/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription)
key to your app’s `Info.plist` file, and include a description of how you intend
to use the user’s media. If this key isn’t present, the system terminates your
app when it tries to access the user’s music.

Request permission for your app to use MusicKit with
[`MusicAuthorization`](/documentation/musickit/musicauthorization). Check
specific capabilities for the current
[`MusicSubscription`](/documentation/musickit/musicsubscription) to ensure your
music-related functionality is available to the user. Find music items using a
search term with
[`MusicCatalogSearchRequest`](/documentation/musickit/musiccatalogsearchrequest),
or find music items using a filter with
[`MusicCatalogResourceRequest`](/documentation/musickit/musiccatalogresourcerequest).
Play music in your app with one of the two music players that MusicKit offers.
Allow the user to begin a free trial for Apple Music from within your app by
presenting a music subscription offer.

You can load content from an arbitrary Apple Music API endpoint with
[`MusicDataRequest`](/documentation/musickit/musicdatarequest) to take further
advantage of additional functionality available in Apple Music API.

## [Topics](/documentation/musickit#topics)

### [Essentials](/documentation/musickit#Essentials)

[Using Automatic Developer Token Generation for Apple Music API](/documentation/musickit/using-automatic-token-generation-for-apple-music-api)

Enable your app’s integration with the MusicKit App Service in the developer portal.

[Using MusicKit to Integrate with Apple Music](/documentation/musickit/using_musickit_to_integrate_with_apple_music)

Find an album in Apple Music that corresponds to a CD in a user’s collection, and present the information for the album.

[`NSAppleMusicUsageDescription`](/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription)

A message that tells people why the app is requesting access to their media library.

### [Music Items](/documentation/musickit#Music-Items)

A set of value types represents each kind of music item.

[`struct Album`](/documentation/musickit/album)

A music item that represents an album.

[`struct Artist`](/documentation/musickit/artist)

A music item that represents an artist.

[`struct Curator`](/documentation/musickit/curator)

A music item that represents a curator.

[`struct Genre`](/documentation/musickit/genre)

A music item that represents a genre.

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

### [Music Item Attributes](/documentation/musickit#Music-Item-Attributes)

A set of structured attributes for music items.

[`enum ContentRating`](/documentation/musickit/contentrating)

The rating of the content that potentially plays while playing a resource.

[`struct EditorialNotes`](/documentation/musickit/editorialnotes)

An object that represents editorial notes.

[`struct PreviewAsset`](/documentation/musickit/previewasset)

An object that represents a preview for resources.

### [Catalog Search](/documentation/musickit#Catalog-Search)

The catalog search request allows your app to find music items in the Apple Music catalog.

[`struct MusicCatalogSearchRequest`](/documentation/musickit/musiccatalogsearchrequest)

A request that your app uses to fetch items from the Apple Music catalog using a search term.

[`struct MusicCatalogSearchResponse`](/documentation/musickit/musiccatalogsearchresponse)

An object that contains results for a catalog search request.

[`protocol MusicCatalogSearchable`](/documentation/musickit/musiccatalogsearchable)

A protocol for music items that your app can fetch by using a catalog search request.

### [Resource Loading Using Filters](/documentation/musickit#Resource-Loading-Using-Filters)

The catalog resource request allows your app to load items using a specific filter. Each music item type has its own set of properties you can use as a filter for a catalog resource request when loading music items for your app.

[`struct MusicCatalogResourceRequest`](/documentation/musickit/musiccatalogresourcerequest)

A request that your app uses to fetch items from the Apple Music catalog using a filter.

[`struct MusicCatalogResourceResponse`](/documentation/musickit/musiccatalogresourceresponse)

An object that contains results for a catalog resource request.

[`protocol AlbumFilter`](/documentation/musickit/albumfilter)

Album properties your app uses as a filter for a catalog resource request.

[`protocol ArtistFilter`](/documentation/musickit/artistfilter)

Artist properties your app uses as a filter for a catalog resource request.

[`protocol CuratorFilter`](/documentation/musickit/curatorfilter)

Curator properties your app uses as a filter for a catalog resource request.

[`protocol GenreFilter`](/documentation/musickit/genrefilter)

Genre properties your app uses as a filter for a catalog resource request.

[`protocol MusicVideoFilter`](/documentation/musickit/musicvideofilter)

Music video properties your app uses as a filter for a catalog resource request.

[`protocol PlaylistFilter`](/documentation/musickit/playlistfilter)

Playlist properties your app uses as a filter for a catalog resource request.

[`protocol RadioShowFilter`](/documentation/musickit/radioshowfilter)

Radio Show properties your app uses as a filter for a catalog resource request.

[`protocol RecordLabelFilter`](/documentation/musickit/recordlabelfilter)

The set of record label properties your app uses as a filter for a catalog resource request.

[`protocol SongFilter`](/documentation/musickit/songfilter)

Song properties your app uses as a filter for a catalog resource request.

[`protocol StationFilter`](/documentation/musickit/stationfilter)

The set of station properties your app uses as a filter for a catalog resource request.

[`protocol FilterableMusicItem`](/documentation/musickit/filterablemusicitem)

A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.

### [General Purpose Data Request](/documentation/musickit#General-Purpose-Data-Request)

[`struct MusicDataRequest`](/documentation/musickit/musicdatarequest)

A request for loading data from an arbitrary Apple Music API endpoint.

[`struct MusicDataResponse`](/documentation/musickit/musicdataresponse)

An object containing results for a data request.

### [Playback](/documentation/musickit#Playback)

[`class ApplicationMusicPlayer`](/documentation/musickit/applicationmusicplayer)

An object your app uses to play music in a way that doesn’t affect the Music app’s state.

[`class SystemMusicPlayer`](/documentation/musickit/systemmusicplayer)

An object your app uses to play music by controlling the Music app’s state.

[`class MusicPlayer`](/documentation/musickit/musicplayer)

An object your app uses to play music.

[`protocol PlayableMusicItem`](/documentation/musickit/playablemusicitem)

A set of properties that a music player uses to initiate playback for a music item.

[`struct PlayParameters`](/documentation/musickit/playparameters)

An opaque object that represents parameters to initiate playback of a playable music item using a music player.

### [Artwork](/documentation/musickit#Artwork)

[`struct Artwork`](/documentation/musickit/artwork)

An object that represents artwork for a music item.

[`struct ArtworkImage`](/documentation/musickit/artworkimage)

A view that displays the image for a music item’s artwork.

### [Authorization](/documentation/musickit#Authorization)

Before you can use any of the functionality of the framework, you need to request the user’s informed consent for your app to access their music data.

[`struct MusicAuthorization`](/documentation/musickit/musicauthorization)

A type that allows you to request the user’s informed consent for your app to access their music data.

### [Apple Music Subscription](/documentation/musickit#Apple-Music-Subscription)

[`struct MusicSubscription`](/documentation/musickit/musicsubscription)

A representation of the current state of the user’s subscription to Apple Music.

[`struct MusicSubscriptionOffer`](/documentation/musickit/musicsubscriptionoffer)

A type for grouping other types for showing subscription offers for Apple Music.

### [Token management](/documentation/musickit#Token-management)

The framework manages tokens for accessing Apple Music API automatically by default, but you can generate your own developer token by creating a class that inherits from the token provider type alias.

[`typealias MusicTokenProvider`](/documentation/musickit/musictokenprovider)

An object that music requests use to access Apple Music API.

[`protocol MusicDeveloperTokenProvider`](/documentation/musickit/musicdevelopertokenprovider)

A set of methods that music requests use to access Apple Music API.

[`class MusicUserTokenProvider`](/documentation/musickit/musicusertokenprovider)

A class that music requests use to fetch user tokens your app requires to access Apple Music API.

[`struct MusicTokenRequestOptions`](/documentation/musickit/musictokenrequestoptions)

Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.

[`enum MusicTokenRequestError`](/documentation/musickit/musictokenrequesterror)

An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.

[`class DefaultMusicTokenProvider`](/documentation/musickit/defaultmusictokenprovider)

The default token provider that music requests use to access Apple Music API.

### [Utility](/documentation/musickit#Utility)

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

[`class PartialMusicAsyncProperty`](/documentation/musickit/partialmusicasyncproperty)

A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.

[`class PartialMusicProperty`](/documentation/musickit/partialmusicproperty)

A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.

[`class AnyMusicProperty`](/documentation/musickit/anymusicproperty)

A type-erased identifier for a music item property, from any root type to any resulting value type.

### [Classes](/documentation/musickit#Classes)

[`class MusicLibrary`](/documentation/musickit/musiclibrary)

An object your app uses to access the user’s music library.

### [Protocols](/documentation/musickit#Protocols)

[`protocol LibraryAlbumFilter`](/documentation/musickit/libraryalbumfilter)

Album properties your app uses as a filter for a library request.

[`protocol LibraryAlbumSortProperties`](/documentation/musickit/libraryalbumsortproperties)

Album properties your app uses to sort results for a library request.

[`protocol LibraryArtistFilter`](/documentation/musickit/libraryartistfilter)

Artist properties your app uses as a filter for a library request.

[`protocol LibraryArtistSortProperties`](/documentation/musickit/libraryartistsortproperties)

Artist properties your app uses to sort results for a library request.

[`protocol LibraryGenreFilter`](/documentation/musickit/librarygenrefilter)

Genre properties your app uses as a filter for a library request.

[`protocol LibraryGenreSortProperties`](/documentation/musickit/librarygenresortproperties)

Genre properties your app uses to sort results for a library request.

[`protocol LibraryMusicVideoFilter`](/documentation/musickit/librarymusicvideofilter)

Music video properties your app uses as a filter for a library request.

[`protocol LibraryMusicVideoSortProperties`](/documentation/musickit/librarymusicvideosortproperties)

Music video properties your app uses to sort results for a library request.

[`protocol LibraryPlaylistEntryFilter`](/documentation/musickit/libraryplaylistentryfilter)

Playlist entry properties your app uses as a filter for a library request.

[`protocol LibraryPlaylistEntrySortProperties`](/documentation/musickit/libraryplaylistentrysortproperties)

Playlist entry properties your app uses to sort results for a library request.

[`protocol LibraryPlaylistFilter`](/documentation/musickit/libraryplaylistfilter)

Playlist properties your app uses as a filter for a library request.

[`protocol LibraryPlaylistSortProperties`](/documentation/musickit/libraryplaylistsortproperties)

Playlist properties your app uses to sort results for a library request.

[`protocol LibrarySongFilter`](/documentation/musickit/librarysongfilter)

Song properties your app uses as a filter for a library request.

[`protocol LibrarySongSortProperties`](/documentation/musickit/librarysongsortproperties)

Song properties your app uses to sort results for a library request.

[`protocol LibraryTrackFilter`](/documentation/musickit/librarytrackfilter)

Track properties your app uses as a filter for a library request.

[`protocol LibraryTrackSortProperties`](/documentation/musickit/librarytracksortproperties)

Track properties your app uses to sort results for a library request.

[`protocol MusicCatalogChartRequestable`](/documentation/musickit/musiccatalogchartrequestable)

A protocol for music items that your app can fetch by using a catalog charts request.

[`protocol MusicCatalogTopLevelResourceRequesting`](/documentation/musickit/musiccatalogtoplevelresourcerequesting)

A protocol for music items that your app can fetch by using a catalog resource request without any filter.

[`protocol MusicLibraryAddable`](/documentation/musickit/musiclibraryaddable)

A protocol for music items that your app can add to the music library.

[`protocol MusicLibraryRequestFilterValueEquatable`](/documentation/musickit/musiclibraryrequestfiltervalueequatable)

A protocol for types of values your app can use with equality filters when fetching items using a music library request.

[`protocol MusicLibraryRequestFilterValueMembershipComparable`](/documentation/musickit/musiclibraryrequestfiltervaluemembershipcomparable)

A protocol for types of values your app can use with membership filters when fetching items using a music library request.

[`protocol MusicLibraryRequestable`](/documentation/musickit/musiclibraryrequestable)

A protocol for music items that your app can fetch by using a library request.

[`protocol MusicLibrarySearchable`](/documentation/musickit/musiclibrarysearchable)

A protocol for music items that your app can fetch by using a library search request.

[`protocol MusicLibrarySectionRequestable`](/documentation/musickit/musiclibrarysectionrequestable)

A protocol for types your app uses as sections when fetching items using a library sectioned request.

[`protocol MusicPersonalRecommendationItem`](/documentation/musickit/musicpersonalrecommendationitem)

A protocol for music items that your app can fetch by using a personal recommendations request.

[`protocol MusicPlaylistAddable`](/documentation/musickit/musicplaylistaddable)

A protocol for music items that your app can add to a playlist.

[`protocol MusicRecentlyPlayedRequestable`](/documentation/musickit/musicrecentlyplayedrequestable)

A protocol for music items that your app can fetch by using a recently played request.

### [Structures](/documentation/musickit#Structures)

[`struct MusicCatalogChart`](/documentation/musickit/musiccatalogchart)

An object that contains popular items in the Apple Music catalog.

[`struct MusicCatalogChartsRequest`](/documentation/musickit/musiccatalogchartsrequest)

A request that your app uses to fetch the most popular items in the Apple Music catalog.

[`struct MusicCatalogChartsResponse`](/documentation/musickit/musiccatalogchartsresponse)

An object that contains results for a catalog charts request.

[`struct MusicCatalogSearchSuggestionsRequest`](/documentation/musickit/musiccatalogsearchsuggestionsrequest)

A request that your app uses to fetch suggestions from the Apple Music catalog using a search term.

[`struct MusicCatalogSearchSuggestionsResponse`](/documentation/musickit/musiccatalogsearchsuggestionsresponse)

An object that contains results for a catalog search suggestions request.

[`struct MusicLibraryRequest`](/documentation/musickit/musiclibraryrequest)

A request that your app uses to fetch items from the user’s music library.

[`struct MusicLibraryResponse`](/documentation/musickit/musiclibraryresponse)

An object that contains results for a library request.

[`struct MusicLibrarySearchRequest`](/documentation/musickit/musiclibrarysearchrequest)

A request that your app uses to fetch items from user’s library using a search term.

[`struct MusicLibrarySearchResponse`](/documentation/musickit/musiclibrarysearchresponse)

An object that contains results for a library search request.

[`struct MusicLibrarySection`](/documentation/musickit/musiclibrarysection)

A section for a library sectioned response.

[`struct MusicLibrarySectionedRequest`](/documentation/musickit/musiclibrarysectionedrequest)

A request that your app uses to fetch items grouped by sections from the user’s music library.

[`struct MusicLibrarySectionedResponse`](/documentation/musickit/musiclibrarysectionedresponse)

An object that contains results for a library sectioned request.

[`struct MusicPersonalRecommendation`](/documentation/musickit/musicpersonalrecommendation)

An object that contains recommended items based on the user’s library and listening history.

[`struct MusicPersonalRecommendationsRequest`](/documentation/musickit/musicpersonalrecommendationsrequest)

A request that your app uses to fetch music recommendations based on the user’s library and listening history.

[`struct MusicPersonalRecommendationsResponse`](/documentation/musickit/musicpersonalrecommendationsresponse)

An object that contains results for a personal recommendations request.

[`struct MusicRecentlyPlayedRequest`](/documentation/musickit/musicrecentlyplayedrequest)

A request that your app uses to fetch items the user has recently played.

[`struct MusicRecentlyPlayedResponse`](/documentation/musickit/musicrecentlyplayedresponse)

An object that contains items the user has recently played.

[`struct TitledSection`](/documentation/musickit/titledsection)

A section you can use to request items from the library grouped by title.

### [Type Aliases](/documentation/musickit#Type-Aliases)

[`typealias MusicRecentlyPlayedContainerRequest`](/documentation/musickit/musicrecentlyplayedcontainerrequest)

A request that your app uses to fetch albums, playlists or stations that the user has recently played.

[`typealias MusicRecentlyPlayedContainerResponse`](/documentation/musickit/musicrecentlyplayedcontainerresponse)

An object that contains albums, playlists or stations that the user has recently played.

### [Enumerations](/documentation/musickit#Enumerations)

[`enum AudioVariant`](/documentation/musickit/audiovariant)

Variants that indicate the quality of audio available for an item.

[`enum MusicCatalogChartKind`](/documentation/musickit/musiccatalogchartkind)

The available kinds of catalog charts.

[`enum MusicPropertySource`](/documentation/musickit/musicpropertysource)

An enumeration that specifies which source to use when requesting properties and relationships.

[`enum RecentlyPlayedMusicItem`](/documentation/musickit/recentlyplayedmusicitem)

An item that represents an album, a playlist, or a station that the user has recently played.

## [See Also](/documentation/musickit#see-also)

### [Related Documentation](/documentation/musickit#Related-Documentation)

[Media Player](/documentation/MediaPlayer)

Find and play songs, audio podcasts, audio books, and more from within your app.

[Apple Music API](/documentation/AppleMusicAPI)

Integrate streaming music with catalog and personal content.
