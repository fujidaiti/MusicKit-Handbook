# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/playablemusicitem

- [MusicKit](/documentation/musickit)
- PlayableMusicItem

Protocol

# PlayableMusicItem

A set of properties that a music player uses to initiate playback for a music item.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 14.0+tvOS 15.0+visionOS 1.0+

```
protocol PlayableMusicItem : MusicItem
```

## [Topics](/documentation/musickit/playablemusicitem#topics)

### [Instance Properties](/documentation/musickit/playablemusicitem#Instance-Properties)

[`var playParameters: PlayParameters?`](/documentation/musickit/playablemusicitem/playparameters)

The parameters to use to play the music item.

**Required**

## [Relationships](/documentation/musickit/playablemusicitem#relationships)

### [Inherits From](/documentation/musickit/playablemusicitem#inherits-from)

- [`MusicItem`](/documentation/musickit/musicitem)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

### [Conforming Types](/documentation/musickit/playablemusicitem#conforming-types)

- [`Album`](/documentation/musickit/album)
- [`MusicPlayer.Queue.Entry.Item`](/documentation/musickit/musicplayer/queue/entry/item-swift.enum)
- [`Playlist`](/documentation/musickit/playlist)
- [`Playlist.Entry`](/documentation/musickit/playlist/entry)
- [`Playlist.Entry.Item`](/documentation/musickit/playlist/entry/item-swift.enum)
- [`RecentlyPlayedMusicItem`](/documentation/musickit/recentlyplayedmusicitem)
- [`Song`](/documentation/musickit/song)
- [`Station`](/documentation/musickit/station)
- [`Track`](/documentation/musickit/track)

## [See Also](/documentation/musickit/playablemusicitem#see-also)

### [Playback](/documentation/musickit/playablemusicitem#Playback)

[`class ApplicationMusicPlayer`](/documentation/musickit/applicationmusicplayer)

An object your app uses to play music in a way that doesn’t affect the Music app’s state.

[`class SystemMusicPlayer`](/documentation/musickit/systemmusicplayer)

An object your app uses to play music by controlling the Music app’s state.

[`class MusicPlayer`](/documentation/musickit/musicplayer)

An object your app uses to play music.

[`struct PlayParameters`](/documentation/musickit/playparameters)

An opaque object that represents parameters to initiate playback of a playable music item using a music player.
