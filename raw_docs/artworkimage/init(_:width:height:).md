# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/artworkimage/init(_:width:height:)

- [MusicKit](/documentation/musickit)
- [ArtworkImage](/documentation/musickit/artworkimage)
- init(\_:width:height:)

Initializer

# init(\_:width:height:)

Creates an instance with a specified width and height.

MusicKitSwiftUIiOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
nonisolated
init(
    _ artwork: Artwork,
    width: CGFloat,
    height: CGFloat
)
```

## [Discussion](/documentation/musickit/artworkimage/init(_:width:height:)#discussion)

This initializer derives the [`URL`](/documentation/Foundation/URL) for loading
the artwork image from the [`Artwork`](/documentation/MusicKit/Artwork) instance
and the specified sizing parameters, as well as the display scale for the
current environment.

The loaded image and placeholder have constrained frames from these sizing
parameters.
