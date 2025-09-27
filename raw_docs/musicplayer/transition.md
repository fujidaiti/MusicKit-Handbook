# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicplayer/transition

- [MusicKit](/documentation/musickit)
- [MusicPlayer](/documentation/musickit/musicplayer)
- MusicPlayer.Transition

Enumeration

# MusicPlayer.Transition

The transition applied between playing items.

iOS 18.0+iPadOS 18.0+

```
enum Transition
```

## [Topics](/documentation/musickit/musicplayer/transition#topics)

### [Structures](/documentation/musickit/musicplayer/transition#Structures)

[`struct CrossfadeOptions`](/documentation/musickit/musicplayer/transition/crossfadeoptions)

The options for the crossfade transition.

### [Enumeration Cases](/documentation/musickit/musicplayer/transition#Enumeration-Cases)

[`case crossfade(options: MusicPlayer.Transition.CrossfadeOptions)`](/documentation/musickit/musicplayer/transition/crossfade(options:))

A smooth overlap between the currently playing item and the next item.

[`case none`](/documentation/musickit/musicplayer/transition/none)

No transition.

### [Type Properties](/documentation/musickit/musicplayer/transition#Type-Properties)

[`static let crossfade: MusicPlayer.Transition`](/documentation/musickit/musicplayer/transition/crossfade)

A smooth overlap between the currently playing item and the next item with default options.

### [Type Methods](/documentation/musickit/musicplayer/transition#Type-Methods)

[`static func crossfade(duration: TimeInterval?) -> MusicPlayer.Transition`](/documentation/musickit/musicplayer/transition/crossfade(duration:))

A smooth overlap between the currently playing item and the next item with a specified duration.

## [Relationships](/documentation/musickit/musicplayer/transition#relationships)

### [Conforms To](/documentation/musickit/musicplayer/transition#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
