# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/artworkimage/init(_:height:)

- [MusicKit](/documentation/musickit)
- [ArtworkImage](/documentation/musickit/artworkimage)
- init(\_:height:)

Initializer

# init(\_:height:)

Creates an instance with a specified height.

MusicKitSwiftUIiOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
nonisolated
init(
    _ artwork: Artwork,
    height: CGFloat
)
```

## [Discussion](/documentation/musickit/artworkimage/init(_:height:)#discussion)

This initializer derives the [`URL`](/documentation/Foundation/URL) for loading
the artwork image from the [`Artwork`](/documentation/MusicKit/Artwork) instance
and the specified sizing parameters, as well as the display scale for the
current environment.

The loaded image and placeholder have constrained frames from these sizing
parameters.

If you provide the height only, the artwork image calculates the width dimension
as a proportional length according to the aspect ratio of the artwork.
