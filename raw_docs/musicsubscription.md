# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicsubscription

- [MusicKit](/documentation/musickit)
- MusicSubscription

Structure

# MusicSubscription

A representation of the current state of the user’s subscription to Apple Music.

iOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+tvOS 15.0+visionOS 1.0+watchOS 8.0+

```
struct MusicSubscription
```

## [Topics](/documentation/musickit/musicsubscription#topics)

### [Structures](/documentation/musickit/musicsubscription#Structures)

[`struct Updates`](/documentation/musickit/musicsubscription/updates)

An asynchronous sequence to use for observing updates to the current state of the user’s subscription to Apple Music.

### [Instance Properties](/documentation/musickit/musicsubscription#Instance-Properties)

[`let canBecomeSubscriber: Bool`](/documentation/musickit/musicsubscription/canbecomesubscriber)

A capability that allows your app to present subscription offers for Apple Music.

[`let canPlayCatalogContent: Bool`](/documentation/musickit/musicsubscription/canplaycatalogcontent)

A capability that allows your app to play subscription content using a music player.

[`let hasCloudLibraryEnabled: Bool`](/documentation/musickit/musicsubscription/hascloudlibraryenabled)

A capability that allows your app to perform modifications to the user’s iCloud Music Library.

### [Type Properties](/documentation/musickit/musicsubscription#Type-Properties)

[`static var current: MusicSubscription`](/documentation/musickit/musicsubscription/current)

The current state of the user’s subscription to Apple Music.

[`static var subscriptionUpdates: MusicSubscription.Updates`](/documentation/musickit/musicsubscription/subscriptionupdates)

An asynchronous sequence to use for observing updates to the current state of the user’s subscription to Apple Music.

### [Enumerations](/documentation/musickit/musicsubscription#Enumerations)

[`enum Error`](/documentation/musickit/musicsubscription/error)

An error that MusicKit can throw upon requesting the current music subscription of the user.

## [Relationships](/documentation/musickit/musicsubscription#relationships)

### [Conforms To](/documentation/musickit/musicsubscription#conforms-to)

- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## [See Also](/documentation/musickit/musicsubscription#see-also)

### [Apple Music Subscription](/documentation/musickit/musicsubscription#Apple-Music-Subscription)

[`struct MusicSubscriptionOffer`](/documentation/musickit/musicsubscriptionoffer)

A type for grouping other types for showing subscription offers for Apple Music.
