# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/endseeking()

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- endSeeking()

Instance Method

# endSeeking()

Ends forward and backward seeking through the music content.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
func endSeeking()
```

## [Discussion](/documentation/musickit/musicplayer/endseeking()#discussion)

Call this method to end a seek operation that begins when you call either the
[`beginSeekingBackward()`](/documentation/musickit/musicplayer/beginseekingbackward())
or
[`beginSeekingForward()`](/documentation/musickit/musicplayer/beginseekingforward())
method. After calling this method, the player returns to its previous state. For
example, if the entry is playing before seeking begins, it continues playing
from the new playhead position after calling this method.
