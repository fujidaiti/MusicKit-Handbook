# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/titledsection

- [MusicKit](/documentation/musickit)
- TitledSection

Structure

# TitledSection

A section you can use to request items from the library grouped by title.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
struct TitledSection
```

## [Overview](/documentation/musickit/titledsection#overview)

For example, when you perform a library sectioned request of albums, the library
sectioned response will contain albums grouped by the first letter of their
title, and the [`title`](/documentation/musickit/titledsection/title) property
of this section will be equal to that first letter.

## [Topics](/documentation/musickit/titledsection#topics)

### [Instance Properties](/documentation/musickit/titledsection#Instance-Properties)

[`var id: MusicItemID`](/documentation/musickit/titledsection/id)

The unique identifier for the titled section.

[`let title: String`](/documentation/musickit/titledsection/title)

The title of the section.

## [Relationships](/documentation/musickit/titledsection#relationships)

### [Conforms To](/documentation/musickit/titledsection#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`MusicLibrarySectionRequestable`](/documentation/musickit/musiclibrarysectionrequestable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
