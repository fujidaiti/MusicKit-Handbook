# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/queue/insert(_:position:)-186ue

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- - [MusicPlayer](/documentation/musickit/musicplayer)
- [MusicPlayer.Queue](/documentation/musickit/musicplayer/queue)
- insert(\_:position:)

Instance Method

# insert(\_:position:)

Inserts a playable music item into the playback queue.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
func insert<PlayableMusicItemType>(
    _ playableItem: PlayableMusicItemType,
    position: MusicPlayer.Queue.EntryInsertionPosition
) async throws where PlayableMusicItemType : PlayableMusicItem
```
