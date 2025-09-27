# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/applicationmusicplayer

- [MusicKit](/documentation/musickit)
- ApplicationMusicPlayer

Class

# ApplicationMusicPlayer

An object your app uses to play music in a way that doesn’t affect the Music app’s state.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
class ApplicationMusicPlayer
```

## [Overview](/documentation/musickit/applicationmusicplayer#overview)

The application music player plays music specifically for your app, and doesn’t
affect the Music app’s state.

If your app includes a background audio mode in your `Info.plist` file, the
application music player continues playing the current music item when your app
moves to the background.

## [Topics](/documentation/musickit/applicationmusicplayer#topics)

### [Classes](/documentation/musickit/applicationmusicplayer#Classes)

[`class Queue`](/documentation/musickit/applicationmusicplayer/queue-swift.class)

### [Instance Properties](/documentation/musickit/applicationmusicplayer#Instance-Properties)

[`var queue: ApplicationMusicPlayer.Queue`](/documentation/musickit/applicationmusicplayer/queue-swift.property)

The playback queue for the application music player.

[`var transition: MusicPlayer.Transition`](/documentation/musickit/applicationmusicplayer/transition)

The transition between items for the application music player.

### [Type Properties](/documentation/musickit/applicationmusicplayer#Type-Properties)

[`static let shared: ApplicationMusicPlayer`](/documentation/musickit/applicationmusicplayer/shared)

The shared application music player, which plays music specifically for your app.

## [Relationships](/documentation/musickit/applicationmusicplayer#relationships)

### [Inherits From](/documentation/musickit/applicationmusicplayer#inherits-from)

- [`MusicPlayer`](/documentation/musickit/musicplayer)

## [See Also](/documentation/musickit/applicationmusicplayer#see-also)

### [Playback](/documentation/musickit/applicationmusicplayer#Playback)

[`class SystemMusicPlayer`](/documentation/musickit/systemmusicplayer)

An object your app uses to play music by controlling the Music app’s state.

[`class MusicPlayer`](/documentation/musickit/musicplayer)

An object your app uses to play music.

[`protocol PlayableMusicItem`](/documentation/musickit/playablemusicitem)

A set of properties that a music player uses to initiate playback for a music item.

[`struct PlayParameters`](/documentation/musickit/playparameters)

An opaque object that represents parameters to initiate playback of a playable music item using a music player.
