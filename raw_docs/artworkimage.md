# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/artworkimage

- [MusicKit](/documentation/musickit)
- ArtworkImage

Structure

# ArtworkImage

A view that displays the image for a music item’s artwork.

MusicKitSwiftUIiOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
@MainActor @preconcurrency
struct ArtworkImage
```

## [Overview](/documentation/musickit/artworkimage#overview)

You can create an artwork image with an instance of
[`Artwork`](/documentation/MusicKit/Artwork).

While the artwork’s image data is loading,
[`ArtworkImage`](/documentation/musickit/artworkimage) automatically displays a
placeholder with a solid color that matches the
[`backgroundColor`](/documentation/MusicKit/Artwork/backgroundColor) property of
the artwork to render.

## [Topics](/documentation/musickit/artworkimage#topics)

### [Initializers](/documentation/musickit/artworkimage#Initializers)

[`init(Artwork, height: CGFloat)`](/documentation/musickit/artworkimage/init(_:height:))

Creates an instance with a specified height.

[`init(Artwork, width: CGFloat)`](/documentation/musickit/artworkimage/init(_:width:))

Creates an instance with a specified width.

[`init(Artwork, width: CGFloat, height: CGFloat)`](/documentation/musickit/artworkimage/init(_:width:height:))

Creates an instance with a specified width and height.

## [Relationships](/documentation/musickit/artworkimage#relationships)

### [Conforms To](/documentation/musickit/artworkimage#conforms-to)

- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
- [`View`](/documentation/SwiftUI/View)

## [See Also](/documentation/musickit/artworkimage#see-also)

### [Artwork](/documentation/musickit/artworkimage#Artwork)

[`struct Artwork`](/documentation/musickit/artwork)

An object that represents artwork for a music item.
