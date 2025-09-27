# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/applicationmusicplayer/transition

- [MusicKit](/documentation/musickit)
- [ApplicationMusicPlayer](/documentation/musickit/applicationmusicplayer)
- transition

Instance Property

# transition

The transition between items for the application music player.

iOS 18.0+iPadOS 18.0+

```
var transition: MusicPlayer.Transition { get set }
```

## [Discussion](/documentation/musickit/applicationmusicplayer/transition#discussion)

By default, the `transition` is `.none` where there is no transition between
playing items.

Your application should set the desired transition before setting the queue.

The player cannot apply transitions in all scenarios. For example, the player
does not apply a transition between two consecutive tracks in an album.
