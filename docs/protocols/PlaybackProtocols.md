# Playback Protocols

> Source: Multiple Apple MusicKit documentation pages

These protocols define capabilities for music items related to playback and library management in MusicKit.

## Overview

The playback protocols enable developers to work with music items that can be played, added to playlists, or added to the user's music library. These protocols extend the base MusicItem protocol to provide specific capabilities for different types of music content interactions.

## Protocols

### PlayableMusicItem
- **Swift Declaration**: `protocol PlayableMusicItem : MusicItem`
- **Purpose**: A set of properties that a music player uses to initiate playback for a music item.
- **Source**: [https://developer.apple.com/documentation/musickit/playablemusicitem](https://developer.apple.com/documentation/musickit/playablemusicitem)
- **Requirements**:
  - `var playParameters: [PlayParameters](../utilities/CoreDataTypes.md#playparameters)?` (Required) - The parameters to use to play the music item.
- **Used By**:
  - [`Album`](../core-types/Album.md)
  - [`MusicPlayer.Queue.Entry.Item`](../services/MusicPlayers.md#musicplayer)
  - [`Playlist`](../core-types/Playlist.md)
  - [`Playlist.Entry`](../core-types/Playlist.md#playlist-entry)
  - [`Playlist.Entry.Item`](../core-types/Playlist.md#playlist-entry-item)
  - [`RecentlyPlayedMusicItem`](../utilities/Enumerations.md#recentlyplayedmusicitem)
  - [`Song`](../core-types/Song.md)
  - [`Station`](../core-types/Station.md)
  - [`Track`](../core-types/Track.md)

### MusicPlaylistAddable
- **Swift Declaration**: `protocol MusicPlaylistAddable : MusicItem`
- **Purpose**: A protocol for music items that your app can add to a playlist.
- **Source**: [https://developer.apple.com/documentation/musickit/musicplaylistaddable](https://developer.apple.com/documentation/musickit/musicplaylistaddable)
- **Requirements**: None specified beyond MusicItem inheritance
- **Used By**:
  - [`Album`](../core-types/Album.md)
  - [`MusicVideo`](../core-types/MusicVideo.md)
  - [`Playlist`](../core-types/Playlist.md)
  - [`Playlist.Entry`](../core-types/Playlist.md#playlist-entry)
  - [`Song`](../core-types/Song.md)
  - [`Track`](../core-types/Track.md)

### MusicLibraryAddable
- **Swift Declaration**: `protocol MusicLibraryAddable : MusicItem`
- **Purpose**: A protocol for music items that your app can add to the music library.
- **Source**: [https://developer.apple.com/documentation/musickit/musiclibraryaddable](https://developer.apple.com/documentation/musickit/musiclibraryaddable)
- **Requirements**: None specified beyond MusicItem inheritance
- **Used By**:
  - [`Album`](../core-types/Album.md)
  - [`MusicVideo`](../core-types/MusicVideo.md)
  - [`Playlist`](../core-types/Playlist.md)
  - [`Playlist.Entry`](../core-types/Playlist.md#playlist-entry)
  - [`Song`](../core-types/Song.md)
  - [`Track`](../core-types/Track.md)