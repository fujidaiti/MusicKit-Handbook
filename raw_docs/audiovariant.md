# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/audiovariant

- [MusicKit](/documentation/musickit)
- AudioVariant

Enumeration

# AudioVariant

Variants that indicate the quality of audio available for an item.

iOS 16.0+iPadOS 16.0+Mac Catalyst 16.0+macOS 13.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
enum AudioVariant
```

## [Topics](/documentation/musickit/audiovariant#topics)

### [Enumeration Cases](/documentation/musickit/audiovariant#Enumeration-Cases)

[`case dolbyAtmos`](/documentation/musickit/audiovariant/dolbyatmos)

Dolby Atmos is an immersive audio experience that surrounds you with sound from all sides, including above.

[`case dolbyAudio`](/documentation/musickit/audiovariant/dolbyaudio)

Dolby Audio is a surround sound format that includes Dolby 5.1 and 7.1.

[`case highResolutionLossless`](/documentation/musickit/audiovariant/highresolutionlossless)

Hi-Res Lossless uses Apple Lossless Audio Codec (ALAC) for bit-for-bit accuracy up to 24-bit/192 kHz.

[`case lossless`](/documentation/musickit/audiovariant/lossless)

Lossless uses Apple Lossless Audio Codec (ALAC) for bit-for-bit accuracy up to 24-bit/48 kHz.

[`case lossyStereo`](/documentation/musickit/audiovariant/lossystereo)

Lossy stereo uses compression used to store sound data.

[`case spatialAudio`](/documentation/musickit/audiovariant/spatialaudio)

Spatial audio is a fallback mode if the content is Dolby Atmos or Dolby Audio, but hardware capabilities don’t support them.

## [Relationships](/documentation/musickit/audiovariant#relationships)

### [Conforms To](/documentation/musickit/audiovariant#conforms-to)

- [`CaseIterable`](/documentation/Swift/CaseIterable)
- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
