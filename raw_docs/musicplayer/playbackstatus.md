# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/playbackstatus

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- MusicPlayer.PlaybackStatus

Enumeration

# MusicPlayer.PlaybackStatus

The music player playback status modes.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
enum PlaybackStatus
```

## [Overview](/documentation/musickit/musicplayer/playbackstatus#overview)

You determine a music player’s state by checking the
[`playbackStatus`](/documentation/musickit/musicplayer/state-swift.class/playbackstatus)
property. Depending on the property’s value, you can update your app’s user
interface or take other appropriate action.

## [Topics](/documentation/musickit/musicplayer/playbackstatus#topics)

### [Enumeration Cases](/documentation/musickit/musicplayer/playbackstatus#Enumeration-Cases)

[`case interrupted`](/documentation/musickit/musicplayer/playbackstatus/interrupted)

The music player is in an interrupted state, such as from an incoming phone call.

[`case paused`](/documentation/musickit/musicplayer/playbackstatus/paused)

The music player is in a paused state.

[`case playing`](/documentation/musickit/musicplayer/playbackstatus/playing)

The music player is playing.

[`case seekingBackward`](/documentation/musickit/musicplayer/playbackstatus/seekingbackward)

The music player is seeking backward.

[`case seekingForward`](/documentation/musickit/musicplayer/playbackstatus/seekingforward)

The music player is seeking forward.

[`case stopped`](/documentation/musickit/musicplayer/playbackstatus/stopped)

The music player is in a stopped state.

## [Relationships](/documentation/musickit/musicplayer/playbackstatus#relationships)

### [Conforms To](/documentation/musickit/musicplayer/playbackstatus#conforms-to)

- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
