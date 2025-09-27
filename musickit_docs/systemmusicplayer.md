# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/systemmusicplayer

- [MusicKit](/documentation/musickit)
- SystemMusicPlayer

Class

# SystemMusicPlayer

An object your app uses to play music by controlling the Music app’s state.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+tvOS 15.0+visionOS 1.0+

```
class SystemMusicPlayer
```

## [Overview](/documentation/musickit/systemmusicplayer#overview)

The system music player employs the Music app on your behalf. When your app
accesses the system music player for the first time, it assumes the current
Music app state and controls it as your app runs. The shared state includes the
following:

- Repeat mode (see
  [`MusicPlayer.RepeatMode`](/documentation/musickit/musicplayer/repeatmode))
- Shuffle mode (see
  [`MusicPlayer.ShuffleMode`](/documentation/musickit/musicplayer/shufflemode))
- Playback status (see `MusicPlayer/PlaybackStatus`)

The system music player doesn’t share other aspects of the Music app’s state.
Music that’s playing continues to play when your app moves to the background.

## [Topics](/documentation/musickit/systemmusicplayer#topics)

### [Instance Properties](/documentation/musickit/systemmusicplayer#Instance-Properties)

[`var queue: MusicPlayer.Queue`](/documentation/musickit/systemmusicplayer/queue)

The playback queue for the system music player.

### [Type Properties](/documentation/musickit/systemmusicplayer#Type-Properties)

[`static let shared: SystemMusicPlayer`](/documentation/musickit/systemmusicplayer/shared)

The shared system music player, which controls the Music app’s state.

## [Relationships](/documentation/musickit/systemmusicplayer#relationships)

### [Inherits From](/documentation/musickit/systemmusicplayer#inherits-from)

- [`MusicPlayer`](/documentation/musickit/musicplayer)

## [See Also](/documentation/musickit/systemmusicplayer#see-also)

### [Playback](/documentation/musickit/systemmusicplayer#Playback)

[`class ApplicationMusicPlayer`](/documentation/musickit/applicationmusicplayer)

An object your app uses to play music in a way that doesn’t affect the Music app’s state.

[`class MusicPlayer`](/documentation/musickit/musicplayer)

An object your app uses to play music.

[`protocol PlayableMusicItem`](/documentation/musickit/playablemusicitem)

A set of properties that a music player uses to initiate playback for a music item.

[`struct PlayParameters`](/documentation/musickit/playparameters)

An opaque object that represents parameters to initiate playback of a playable music item using a music player.
