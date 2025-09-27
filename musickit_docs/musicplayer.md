# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer

- [MusicKit](/documentation/musickit)
- MusicPlayer

Class

# MusicPlayer

An object your app uses to play music.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
class MusicPlayer
```

## [Topics](/documentation/musickit/musicplayer#topics)

### [Classes](/documentation/musickit/musicplayer#Classes)

[`class Queue`](/documentation/musickit/musicplayer/queue)

A representation of the playback queue for a music player.

[`class State`](/documentation/musickit/musicplayer/state-swift.class)

An object that exposes the observable properties of a music player.

### [Instance Properties](/documentation/musickit/musicplayer#Instance-Properties)

[`var isPreparedToPlay: Bool`](/documentation/musickit/musicplayer/ispreparedtoplay)

A Boolean value that indicates whether a music player is ready to play.

[`var playbackTime: TimeInterval`](/documentation/musickit/musicplayer/playbacktime)

The current playback time, in seconds, of the current entry.

[`let state: MusicPlayer.State`](/documentation/musickit/musicplayer/state-swift.property)

An object that exposes the observable properties of the music player.

### [Instance Methods](/documentation/musickit/musicplayer#Instance-Methods)

[`func beginSeekingBackward()`](/documentation/musickit/musicplayer/beginseekingbackward())

Begins seeking backward through the music content.

[`func beginSeekingForward()`](/documentation/musickit/musicplayer/beginseekingforward())

Begins seeking forward through the music content.

[`func endSeeking()`](/documentation/musickit/musicplayer/endseeking())

Ends forward and backward seeking through the music content.

[`func pause()`](/documentation/musickit/musicplayer/pause())

Pauses playback of the current entry.

[`func play() async throws`](/documentation/musickit/musicplayer/play())

Initiates playback from the current queue.

[`func prepareToPlay() async throws`](/documentation/musickit/musicplayer/preparetoplay())

Prepares the current queue for playback, interrupting any active (nonmixable) audio sessions.

[`func restartCurrentEntry()`](/documentation/musickit/musicplayer/restartcurrententry())

Restarts playback at the beginning of the currently playing entry.

[`func skipToNextEntry() async throws`](/documentation/musickit/musicplayer/skiptonextentry())

Starts playback of the next entry in the playback queue.

[`func skipToPreviousEntry() async throws`](/documentation/musickit/musicplayer/skiptopreviousentry())

Starts playback of the previous entry in the playback queue.

[`func stop()`](/documentation/musickit/musicplayer/stop())

Ends playback of the current entry.

### [Enumerations](/documentation/musickit/musicplayer#Enumerations)

[`enum PlaybackStatus`](/documentation/musickit/musicplayer/playbackstatus)

The music player playback status modes.

[`enum RepeatMode`](/documentation/musickit/musicplayer/repeatmode)

The repeat modes for the music player.

[`enum ShuffleMode`](/documentation/musickit/musicplayer/shufflemode)

The shuffle modes for the music player.

[`enum Transition`](/documentation/musickit/musicplayer/transition)

The transition applied between playing items.

## [Relationships](/documentation/musickit/musicplayer#relationships)

### [Inherited By](/documentation/musickit/musicplayer#inherited-by)

- [`ApplicationMusicPlayer`](/documentation/musickit/applicationmusicplayer)
- [`SystemMusicPlayer`](/documentation/musickit/systemmusicplayer)

## [See Also](/documentation/musickit/musicplayer#see-also)

### [Playback](/documentation/musickit/musicplayer#Playback)

[`class ApplicationMusicPlayer`](/documentation/musickit/applicationmusicplayer)

An object your app uses to play music in a way that doesn’t affect the Music app’s state.

[`class SystemMusicPlayer`](/documentation/musickit/systemmusicplayer)

An object your app uses to play music by controlling the Music app’s state.

[`protocol PlayableMusicItem`](/documentation/musickit/playablemusicitem)

A set of properties that a music player uses to initiate playback for a music item.

[`struct PlayParameters`](/documentation/musickit/playparameters)

An opaque object that represents parameters to initiate playback of a playable music item using a music player.
