# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class

- [MusicKit](/documentation/musickit)
- [ApplicationMusicPlayer](/documentation/musickit/applicationmusicplayer)
- ApplicationMusicPlayer.Queue

Class

# ApplicationMusicPlayer.Queue

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
class Queue
```

## [Topics](/documentation/musickit/applicationmusicplayer/queue-swift.class#topics)

### [Structures](/documentation/musickit/applicationmusicplayer/queue-swift.class#Structures)

[`struct Entries`](/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct)

### [Initializers](/documentation/musickit/applicationmusicplayer/queue-swift.class#Initializers)

[`init<S>(S, startingAt: S.Element?)`](/documentation/musickit/applicationmusicplayer/queue-swift.class/init(_:startingat:))

Creates a playback queue with playback queue entries.

[`init(album: Album, startingAt: Track)`](/documentation/musickit/applicationmusicplayer/queue-swift.class/init(album:startingat:))

Creates a playback queue with an album and a specific track for the player to start playback.

[`init(arrayLiteral: any PlayableMusicItem...)`](/documentation/musickit/applicationmusicplayer/queue-swift.class/init(arrayliteral:))

[`init<S, PlayableMusicItemType>(for: S, startingAt: S.Element?)`](/documentation/musickit/applicationmusicplayer/queue-swift.class/init(for:startingat:))

Creates a playback queue with playable music items.

[`init(playlist: Playlist, startingAt: Playlist.Entry)`](/documentation/musickit/applicationmusicplayer/queue-swift.class/init(playlist:startingat:))

Creates a playback queue with a playlist and a specific playlist entry for the player to start playback.

### [Instance Properties](/documentation/musickit/applicationmusicplayer/queue-swift.class#Instance-Properties)

[`var entries: ApplicationMusicPlayer.Queue.Entries`](/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.property)

## [Relationships](/documentation/musickit/applicationmusicplayer/queue-swift.class#relationships)

### [Inherits From](/documentation/musickit/applicationmusicplayer/queue-swift.class#inherits-from)

- [`MusicPlayer.Queue`](/documentation/musickit/musicplayer/queue)

### [Conforms To](/documentation/musickit/applicationmusicplayer/queue-swift.class#conforms-to)

- [`Equatable`](/documentation/Swift/Equatable)
- [`ExpressibleByArrayLiteral`](/documentation/Swift/ExpressibleByArrayLiteral)
- [`Hashable`](/documentation/Swift/Hashable)
- [`ObservableObject`](/documentation/Combine/ObservableObject)
