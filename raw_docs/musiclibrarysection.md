# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musiclibrarysection

- [MusicKit](/documentation/musickit)
- MusicLibrarySection

Structure

# MusicLibrarySection

A section for a library sectioned response.

iOS 16.0+iPadOS 16.0+Mac Catalyst 17.0+macOS 14.0+tvOS 16.0+visionOS 1.0+watchOS 9.0+

```
@dynamicMemberLookup
struct MusicLibrarySection<SectionType, MusicItemType> where SectionType : MusicLibrarySectionRequestable, MusicItemType : MusicLibraryRequestable
```

## [Overview](/documentation/musickit/musiclibrarysection#overview)

Your app can access any property of the requested section type directly on this
library section object.

Your app can also access the items contained in a library section with the
[`items`](/documentation/musickit/musiclibrarysection/items) property.

## [Topics](/documentation/musickit/musiclibrarysection#topics)

### [Instance Properties](/documentation/musickit/musiclibrarysection#Instance-Properties)

[`let items: MusicItemCollection<MusicItemType>`](/documentation/musickit/musiclibrarysection/items)

A collection of items that correspond to the children of the section.

### [Subscripts](/documentation/musickit/musiclibrarysection#Subscripts)

[`subscript<T>(dynamicMember _: KeyPath<SectionType, T>) -> T`](/documentation/musickit/musiclibrarysection/subscript(dynamicmember:))

A subscript that allows your app to access any property of the requested section type directly on this library section object.

## [Relationships](/documentation/musickit/musiclibrarysection#relationships)

### [Conforms To](/documentation/musickit/musiclibrarysection#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomDebugStringConvertible`](/documentation/Swift/CustomDebugStringConvertible)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Identifiable`](/documentation/Swift/Identifiable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
