# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/queue/entry

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- - [MusicPlayer](/documentation/musickit/musicplayer)
- [MusicPlayer.Queue](/documentation/musickit/musicplayer/queue)
- MusicPlayer.Queue.Entry

Structure

# MusicPlayer.Queue.Entry

An entry for the playback queue of the music player.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
struct Entry
```

## [Topics](/documentation/musickit/musicplayer/queue/entry#topics)

### [Initializers](/documentation/musickit/musicplayer/queue/entry#Initializers)

[`init(any PlayableMusicItem, startTime: TimeInterval?, endTime: TimeInterval?)`](/documentation/musickit/musicplayer/queue/entry/init(_:starttime:endtime:))

Creates an entry of the playback queue with a playable music item, and optional start and end times.

### [Instance Properties](/documentation/musickit/musicplayer/queue/entry#Instance-Properties)

[`var artwork: Artwork?`](/documentation/musickit/musicplayer/queue/entry/artwork)

The artwork of this entry of the playback queue.

[`var endTime: TimeInterval?`](/documentation/musickit/musicplayer/queue/entry/endtime)

An optional end time for this entry of the playback queue.

[`let id: String`](/documentation/musickit/musicplayer/queue/entry/id)

The unique identifier of this entry of the playback queue.

[`var isTransient: Bool`](/documentation/musickit/musicplayer/queue/entry/istransient)

A Boolean value that indicates whether this entry of the playback queue has a transient music item.

[`var item: MusicPlayer.Queue.Entry.Item?`](/documentation/musickit/musicplayer/queue/entry/item-swift.property)

A music item that corresponds to this entry of the playback queue, such as a song or a music video.

[`var startTime: TimeInterval?`](/documentation/musickit/musicplayer/queue/entry/starttime)

An optional start time for this entry of the playback queue.

[`var subtitle: String?`](/documentation/musickit/musicplayer/queue/entry/subtitle)

The subtitle of this entry of the playback queue.

[`var title: String`](/documentation/musickit/musicplayer/queue/entry/title)

The title of this entry of the playback queue.

[`var transientItem: (any PlayableMusicItem)?`](/documentation/musickit/musicplayer/queue/entry/transientitem)

A music item that corresponds to a recently inserted entry in the playback queue that has underlying items the music player still needs to resolve.

### [Enumerations](/documentation/musickit/musicplayer/queue/entry#Enumerations)

[`enum Item`](/documentation/musickit/musicplayer/queue/entry/item-swift.enum)

An item that corresponds to an entry in the playback queue.

## [Relationships](/documentation/musickit/musicplayer/queue/entry#relationships)

### [Conforms To](/documentation/musickit/musicplayer/queue/entry#conforms-to)

- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
