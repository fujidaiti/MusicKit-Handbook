# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/queue/entry/item-swift.enum

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- [MusicPlayer.Queue](/documentation/musickit/musicplayer/queue)
- - [MusicPlayer](/documentation/musickit/musicplayer)
  - [MusicPlayer.Queue](/documentation/musickit/musicplayer/queue)
- [MusicPlayer.Queue.Entry](/documentation/musickit/musicplayer/queue/entry)
- MusicPlayer.Queue.Entry.Item

Enumeration

# MusicPlayer.Queue.Entry.Item

An item that corresponds to an entry in the playback queue.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
enum Item
```

## [Topics](/documentation/musickit/musicplayer/queue/entry/item-swift.enum#topics)

### [Enumeration Cases](/documentation/musickit/musicplayer/queue/entry/item-swift.enum#Enumeration-Cases)

[`case musicVideo(MusicVideo)`](/documentation/musickit/musicplayer/queue/entry/item-swift.enum/musicvideo(_:))

An item that corresponds to a music video.

[`case song(Song)`](/documentation/musickit/musicplayer/queue/entry/item-swift.enum/song(_:))

An item that corresponds to a song.

### [Instance Properties](/documentation/musickit/musicplayer/queue/entry/item-swift.enum#Instance-Properties)

[`var id: MusicItemID`](/documentation/musickit/musicplayer/queue/entry/item-swift.enum/id)

The unique identifier for the music player item.

[`var playParameters: PlayParameters?`](/documentation/musickit/musicplayer/queue/entry/item-swift.enum/playparameters)

The parameters to use to play the item.

## [Relationships](/documentation/musickit/musicplayer/queue/entry/item-swift.enum#relationships)

### [Conforms To](/documentation/musickit/musicplayer/queue/entry/item-swift.enum#conforms-to)

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
