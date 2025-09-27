# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/artwork

- [MusicKit](/documentation/musickit)
- Artwork

Structure

# Artwork

An object that represents artwork for a music item.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct Artwork
```

## [Topics](/documentation/musickit/artwork#topics)

### [Instance Properties](/documentation/musickit/artwork#Instance-Properties)

[`let alternateText: String?`](/documentation/musickit/artwork/alternatetext)

A textual description for the image.

[`let backgroundColor: CGColor?`](/documentation/musickit/artwork/backgroundcolor)

The average background color of the image.

[`let maximumHeight: Int`](/documentation/musickit/artwork/maximumheight)

The maximum height available for the image.

[`let maximumWidth: Int`](/documentation/musickit/artwork/maximumwidth)

The maximum width available for the image.

[`let primaryTextColor: CGColor?`](/documentation/musickit/artwork/primarytextcolor)

The primary text color to use when displaying the background color.

[`let quaternaryTextColor: CGColor?`](/documentation/musickit/artwork/quaternarytextcolor)

The final posttertiary text color to use when displaying the background color.

[`let secondaryTextColor: CGColor?`](/documentation/musickit/artwork/secondarytextcolor)

The secondary text color to use when displaying the background color.

[`let tertiaryTextColor: CGColor?`](/documentation/musickit/artwork/tertiarytextcolor)

The tertiary text color to use when displaying the background color.

### [Instance Methods](/documentation/musickit/artwork#Instance-Methods)

[`func url(width: Int, height: Int) -> URL?`](/documentation/musickit/artwork/url(width:height:))

Returns a URL to request the image asset for a specified width and height.

## [Relationships](/documentation/musickit/artwork#relationships)

### [Conforms To](/documentation/musickit/artwork#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Decodable`](/documentation/Swift/Decodable)
- [`Encodable`](/documentation/Swift/Encodable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/artwork#see-also)

### [Artwork](/documentation/musickit/artwork#Artwork)

[`struct ArtworkImage`](/documentation/musickit/artworkimage)

A view that displays the image for a music item’s artwork.
