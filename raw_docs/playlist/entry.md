# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/playlist/entry

- [MusicKit](/documentation/musickit)
- [Playlist](/documentation/musickit/playlist)
- Playlist.Entry

Structure

# Playlist.Entry

A music item that represents a playlist entry.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct Entry
```

## [Topics](/documentation/musickit/playlist/entry#topics)

### [Instance Properties](/documentation/musickit/playlist/entry#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/playlist/entry/albumtitle)

The title of the album the playlist entry appears on.

[`var artistName: String`](/documentation/musickit/playlist/entry/artistname)

The artist’s name.

[`var artistURL: URL?`](/documentation/musickit/playlist/entry/artisturl)

The artist’s URL.

[`var artwork: Artwork?`](/documentation/musickit/playlist/entry/artwork)

The artwork of the playlist entry.

[`var contentRating: ContentRating?`](/documentation/musickit/playlist/entry/contentrating)

The rating of the content.

[`var duration: TimeInterval?`](/documentation/musickit/playlist/entry/duration)

The duration of the playlist entry.

[`var editorialNotes: EditorialNotes?`](/documentation/musickit/playlist/entry/editorialnotes)

The editorial notes for the playlist entry.

[`var genreNames: [String]`](/documentation/musickit/playlist/entry/genrenames)

The names of the playlist entry’s associated genres.

[`let id: MusicItemID`](/documentation/musickit/playlist/entry/id)

The unique identifier for the playlist entry.

[`var isrc: String?`](/documentation/musickit/playlist/entry/isrc)

The International Standard Recording Code (ISRC) for the playlist entry.

[`var item: Playlist.Entry.Item?`](/documentation/musickit/playlist/entry/item-swift.property)

The item of the playlist entry.

[`var lastPlayedDate: Date?`](/documentation/musickit/playlist/entry/lastplayeddate)

The date when the user last played the playlist entry on this device.

[`var libraryAddedDate: Date?`](/documentation/musickit/playlist/entry/libraryaddeddate)

The date when the user added the playlist entry to the library.

[`var playCount: Int?`](/documentation/musickit/playlist/entry/playcount)

The number of times the user played the playlist entry.

[`var playParameters: PlayParameters?`](/documentation/musickit/playlist/entry/playparameters)

The parameters to use to play the playlist entry.

[`var position: Int`](/documentation/musickit/playlist/entry/position)

The position of the playlist entry.

[`var previewAssets: [PreviewAsset]?`](/documentation/musickit/playlist/entry/previewassets)

The preview assets for the playlist entry.

[`var releaseDate: Date?`](/documentation/musickit/playlist/entry/releasedate)

The release date (or expected for pre-release) of the playlist entry.

[`var title: String`](/documentation/musickit/playlist/entry/title)

The title of the playlist entry.

[`var url: URL?`](/documentation/musickit/playlist/entry/url)

The URL for the playlist entry.

### [Enumerations](/documentation/musickit/playlist/entry#Enumerations)

[`enum Item`](/documentation/musickit/playlist/entry/item-swift.enum)

An item that corresponds to an entry in a playlist.

### [Default Implementations](/documentation/musickit/playlist/entry#Default-Implementations)

[API Reference

MusicLibraryRequestable Implementations](/documentation/musickit/playlist/entry/musiclibraryrequestable-implementations)

## [Relationships](/documentation/musickit/playlist/entry#relationships)

### [Conforms To](/documentation/musickit/playlist/entry#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`MusicItem`](/documentation/musickit/musicitem)
- [`MusicLibraryAddable`](/documentation/musickit/musiclibraryaddable)
- [`MusicLibraryRequestable`](/documentation/musickit/musiclibraryrequestable)
- [`MusicPlaylistAddable`](/documentation/musickit/musicplaylistaddable)
- [`MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)
- [`PlayableMusicItem`](/documentation/musickit/playablemusicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
