# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicpropertycontainer/with(_:preferredsource:)-9wqhc

- [MusicKit](/documentation/musickit)
- [MusicPropertyContainer](/documentation/musickit/musicpropertycontainer)
- with(\_:preferredSource:)

Instance Method

# with(\_:preferredSource:)

Loads a new instance of the music item that includes the specified properties.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
func with(
    _ properties: PartialMusicAsyncProperty<Self>...,
    preferredSource: MusicPropertySource
) async throws -> Self
```

**Required**

## [Discussion](/documentation/musickit/musicpropertycontainer/with(_:preferredsource:)-9wqhc#discussion)

This asynchronous method fetches a more complete representation of the receiver,
loading the contents for each property you request from either the Apple Music
catalog or the user’s library, depending on the preferred source as well the
availability of the content in those respective data sources.

For example, if you want to load the
[`tracks`](/documentation/musickit/partialmusicproperty/tracks-9mk2l)
relationship for an [`Album`](/documentation/musickit/album), as found in the
user’s library, as well as other associations of content that only live in the
Apple Music catalog, like the
[`recordLabels`](/documentation/musickit/partialmusicproperty/recordlabels) and
[`relatedAlbums`](/documentation/musickit/partialmusicproperty/relatedalbums)
associations, you can use this code:

```
let album: Album = …
let detailedAlbum = try await album.with(
    .tracks,
    .recordLabels,
    .relatedAlbums, 
    preferredSource: .library
)
```

Here, because the
[`tracks`](/documentation/musickit/partialmusicproperty/tracks-9mk2l)
relationship for an [`Album`](/documentation/musickit/album) is supported in
both the library and the catalog, and because the this code specifically
requests
[`MusicPropertySource.library`](/documentation/musickit/musicpropertysource/library)
as the preferred source, the framework will load the tracks from the user’s
library. However, because the
[`recordLabels`](/documentation/musickit/partialmusicproperty/recordlabels) and
[`relatedAlbums`](/documentation/musickit/partialmusicproperty/relatedalbums)
associations are only available in the Apple Music catalog, the framework will
also issue a network request to Apple Music API to fetch those associations of
content from the catalog.
