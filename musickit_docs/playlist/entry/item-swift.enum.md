# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/playlist/entry/item-swift.enum

- [MusicKit](/documentation/musickit)
- [Playlist](/documentation/musickit/playlist)
- - [Playlist](/documentation/musickit/playlist)
- [Playlist.Entry](/documentation/musickit/playlist/entry)
- Playlist.Entry.Item

Enumeration

# Playlist.Entry.Item

An item that corresponds to an entry in a playlist.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
enum Item
```

## [Topics](/documentation/musickit/playlist/entry/item-swift.enum#topics)

### [Enumeration Cases](/documentation/musickit/playlist/entry/item-swift.enum#Enumeration-Cases)

[`case musicVideo(MusicVideo)`](/documentation/musickit/playlist/entry/item-swift.enum/musicvideo(_:))

An item that corresponds to a music video.

[`case song(Song)`](/documentation/musickit/playlist/entry/item-swift.enum/song(_:))

An item that corresponds to a song.

### [Instance Properties](/documentation/musickit/playlist/entry/item-swift.enum#Instance-Properties)

[`var albumTitle: String?`](/documentation/musickit/playlist/entry/item-swift.enum/albumtitle)

The title of the album the playlist entry’s item appears on.

[`var artistName: String`](/documentation/musickit/playlist/entry/item-swift.enum/artistname)

The artist’s name.

[`var artistURL: URL?`](/documentation/musickit/playlist/entry/item-swift.enum/artisturl)

The artist’s URL.

[`var artwork: Artwork?`](/documentation/musickit/playlist/entry/item-swift.enum/artwork)

The artwork for the playlist entry’s item.

[`var contentRating: ContentRating?`](/documentation/musickit/playlist/entry/item-swift.enum/contentrating)

The rating of the content.

[`var duration: TimeInterval?`](/documentation/musickit/playlist/entry/item-swift.enum/duration)

The duration of the playlist entry’s item.

[`var editorialNotes: EditorialNotes?`](/documentation/musickit/playlist/entry/item-swift.enum/editorialnotes)

The editorial notes for the playlist entry’s item.

[`var genreNames: [String]`](/documentation/musickit/playlist/entry/item-swift.enum/genrenames)

The names of the playlist entry’s item associated genres.

[`var id: MusicItemID`](/documentation/musickit/playlist/entry/item-swift.enum/id)

The unique identifier for the playlist entry item.

[`var isrc: String?`](/documentation/musickit/playlist/entry/item-swift.enum/isrc)

The International Standard Recording Code (ISRC) for the playlist entry’s item.

[`var lastPlayedDate: Date?`](/documentation/musickit/playlist/entry/item-swift.enum/lastplayeddate)

The date when the user last played the playlist entry’s item on this device.

[`var libraryAddedDate: Date?`](/documentation/musickit/playlist/entry/item-swift.enum/libraryaddeddate)

The date when the user added the playlist entry’s item to the library.

[`var playCount: Int?`](/documentation/musickit/playlist/entry/item-swift.enum/playcount)

The number of times the user played the playlist entry’s item.

[`var playParameters: PlayParameters?`](/documentation/musickit/playlist/entry/item-swift.enum/playparameters)

The parameters to use to play the playlist entry’s item.

[`var previewAssets: [PreviewAsset]?`](/documentation/musickit/playlist/entry/item-swift.enum/previewassets)

The preview assets for the playlist entry’s item.

[`var releaseDate: Date?`](/documentation/musickit/playlist/entry/item-swift.enum/releasedate)

The release date of the playlist entry’s item.

[`var title: String`](/documentation/musickit/playlist/entry/item-swift.enum/title)

The title of the playlist entry’s item.

[`var url: URL?`](/documentation/musickit/playlist/entry/item-swift.enum/url)

The URL for the playlist entry’s item.

## [Relationships](/documentation/musickit/playlist/entry/item-swift.enum#relationships)

### [Conforms To](/documentation/musickit/playlist/entry/item-swift.enum#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`MusicItem`](/documentation/musickit/musicitem)
- [`MusicPropertyContainer`](/documentation/musickit/musicpropertycontainer)
- [`PlayableMusicItem`](/documentation/musickit/playablemusicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
