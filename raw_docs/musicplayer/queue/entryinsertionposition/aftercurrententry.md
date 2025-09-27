# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/queue/entryinsertionposition/aftercurrententry

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- [MusicPlayer.Queue](/documentation/musickit/musicplayer/queue)
- - [MusicPlayer](/documentation/musickit/musicplayer)
  - [MusicPlayer.Queue](/documentation/musickit/musicplayer/queue)
- [MusicPlayer.Queue.EntryInsertionPosition](/documentation/musickit/musicplayer/queue/entryinsertionposition)
- MusicPlayer.Queue.EntryInsertionPosition.afterCurrentEntry

Case

# MusicPlayer.Queue.EntryInsertionPosition.afterCurrentEntry

A position that allows prepending entries in the playback queue, similar to the Play Next feature in the Music app.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
case afterCurrentEntry
```

## [Discussion](/documentation/musickit/musicplayer/queue/entryinsertionposition/aftercurrententry#discussion)

Inserting entries after the current one merely enqueues them to play next, and
lets the current entry finish playing to the end.

Alternatively, you may change the current entry programmatically by setting the
`currentEntry` property of the
[`queue`](/documentation/musickit/applicationmusicplayer/queue-swift.property)
or [`queue`](/documentation/musickit/systemmusicplayer/queue).
