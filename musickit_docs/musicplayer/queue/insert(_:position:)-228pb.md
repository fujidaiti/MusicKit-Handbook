# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/queue/insert(_:position:)-228pb

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- - [MusicPlayer](/documentation/musickit/musicplayer)
- [MusicPlayer.Queue](/documentation/musickit/musicplayer/queue)
- insert(\_:position:)

Instance Method

# insert(\_:position:)

Inserts playable music items into the playback queue.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
func insert<S, PlayableMusicItemType>(
    _ playableItems: S,
    position: MusicPlayer.Queue.EntryInsertionPosition
) async throws where S : Sequence, PlayableMusicItemType : PlayableMusicItem, PlayableMusicItemType == S.Element
```
