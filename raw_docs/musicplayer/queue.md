# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/queue

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- MusicPlayer.Queue

Class

# MusicPlayer.Queue

A representation of the playback queue for a music player.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
class Queue
```

## [Topics](/documentation/musickit/musicplayer/queue#topics)

### [Structures](/documentation/musickit/musicplayer/queue#Structures)

[`struct Entry`](/documentation/musickit/musicplayer/queue/entry)

An entry for the playback queue of the music player.

### [Initializers](/documentation/musickit/musicplayer/queue#Initializers)

[`init<S>(S, startingAt: S.Element?)`](/documentation/musickit/musicplayer/queue/init(_:startingat:))

Creates a playback queue with playback queue entries.

[`init(album: Album, startingAt: Track)`](/documentation/musickit/musicplayer/queue/init(album:startingat:))

Creates a playback queue with an album and a specific track for the player to start playback.

[`init<S, PlayableMusicItemType>(for: S, startingAt: S.Element?)`](/documentation/musickit/musicplayer/queue/init(for:startingat:))

Creates a playback queue with playable music items.

[`init(playlist: Playlist, startingAt: Playlist.Entry)`](/documentation/musickit/musicplayer/queue/init(playlist:startingat:))

Creates a playback queue with a playlist and a specific playlist entry for the player to start playback.

### [Instance Properties](/documentation/musickit/musicplayer/queue#Instance-Properties)

[`var currentEntry: MusicPlayer.Queue.Entry?`](/documentation/musickit/musicplayer/queue/currententry)

The currently active entry in the playback queue.

### [Instance Methods](/documentation/musickit/musicplayer/queue#Instance-Methods)

[`func insert<PlayableMusicItemType>(PlayableMusicItemType, position: MusicPlayer.Queue.EntryInsertionPosition) async throws`](/documentation/musickit/musicplayer/queue/insert(_:position:)-186ue)

Inserts a playable music item into the playback queue.

[`func insert<S, PlayableMusicItemType>(S, position: MusicPlayer.Queue.EntryInsertionPosition) async throws`](/documentation/musickit/musicplayer/queue/insert(_:position:)-228pb)

Inserts playable music items into the playback queue.

[`func insert(MusicPlayer.Queue.Entry, position: MusicPlayer.Queue.EntryInsertionPosition) async throws`](/documentation/musickit/musicplayer/queue/insert(_:position:)-3lv7k)

Inserts an entry into the playback queue.

[`func insert<S>(S, position: MusicPlayer.Queue.EntryInsertionPosition) async throws`](/documentation/musickit/musicplayer/queue/insert(_:position:)-58ohm)

Inserts entries into the playback queue.

### [Enumerations](/documentation/musickit/musicplayer/queue#Enumerations)

[`enum EntryInsertionPosition`](/documentation/musickit/musicplayer/queue/entryinsertionposition)

An enumeration for the various supported positions for inserting playable music items or entries in the playback queue.

## [Relationships](/documentation/musickit/musicplayer/queue#relationships)

### [Inherited By](/documentation/musickit/musicplayer/queue#inherited-by)

- [`ApplicationMusicPlayer.Queue`](/documentation/musickit/applicationmusicplayer/queue-swift.class)

### [Conforms To](/documentation/musickit/musicplayer/queue#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`ExpressibleByArrayLiteral`](/documentation/Swift/ExpressibleByArrayLiteral)
- [`Hashable`](/documentation/Swift/Hashable)
- [`ObservableObject`](/documentation/Combine/ObservableObject)
