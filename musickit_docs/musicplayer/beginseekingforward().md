# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/beginseekingforward()

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- beginSeekingForward()

Instance Method

# beginSeekingForward()

Begins seeking forward through the music content.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
func beginSeekingForward()
```

## [Discussion](/documentation/musickit/musicplayer/beginseekingforward()#discussion)

Use this method to move the current playback position forward in time at an
accelerated rate. Seeking begins when you call this method, and continues until
you call the [`endSeeking()`](/documentation/musickit/musicplayer/endseeking())
method.

If the player is streaming the underlying content, this method has no effect.
