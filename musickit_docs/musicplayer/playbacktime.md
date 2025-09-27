# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/playbacktime

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- playbackTime

Instance Property

# playbackTime

The current playback time, in seconds, of the current entry.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
var playbackTime: TimeInterval { get set }
```

## [Discussion](/documentation/musickit/musicplayer/playbacktime#discussion)

Changing the value of this property moves the playhead to the new location. For
content streaming live from a server, this value represents the time from the
beginning of the playlist when it first loads. This property returns `NaN` if
the [`CMTime`](/documentation/CoreMedia/CMTime) is invalid or indefinite.
