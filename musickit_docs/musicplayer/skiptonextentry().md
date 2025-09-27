# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/skiptonextentry()

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- skipToNextEntry()

Instance Method

# skipToNextEntry()

Starts playback of the next entry in the playback queue.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
func skipToNextEntry() async throws
```

## [Discussion](/documentation/musickit/musicplayer/skiptonextentry()#discussion)

If the music player isn’t playing, this method designates the next entry as the
next to play.

When you call this method, playback ends if the music player is already at the
last entry in the playback queue.
