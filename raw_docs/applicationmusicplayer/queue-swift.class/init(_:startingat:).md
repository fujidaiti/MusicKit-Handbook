# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/init(_:startingat:)

- [MusicKit](/documentation/musickit)
- [ApplicationMusicPlayer](/documentation/musickit/applicationmusicplayer)
- - [ApplicationMusicPlayer](/documentation/musickit/applicationmusicplayer)
- [ApplicationMusicPlayer.Queue](/documentation/musickit/applicationmusicplayer/queue-swift.class)
- init(\_:startingAt:)

Initializer

# init(\_:startingAt:)

Creates a playback queue with playback queue entries.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
required init<S>(
    _ entries: S,
    startingAt startEntry: S.Element? = nil
) where S : Sequence, S.Element == MusicPlayer.Queue.Entry
```
