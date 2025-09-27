# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/init(for:startingat:)

- [MusicKit](/documentation/musickit)
- [ApplicationMusicPlayer](/documentation/musickit/applicationmusicplayer)
- - [ApplicationMusicPlayer](/documentation/musickit/applicationmusicplayer)
- [ApplicationMusicPlayer.Queue](/documentation/musickit/applicationmusicplayer/queue-swift.class)
- init(for:startingAt:)

Initializer

# init(for:startingAt:)

Creates a playback queue with playable music items.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
required init<S, PlayableMusicItemType>(
    for playableItems: S,
    startingAt startPlayableItem: S.Element? = nil
) where S : Sequence, PlayableMusicItemType : PlayableMusicItem, PlayableMusicItemType == S.Element
```
