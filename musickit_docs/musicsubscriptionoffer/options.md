# This page requires JavaScript.

> Source: https://developer.apple.com/documentation/musickit/musicsubscriptionoffer/options

- [MusicKit](/documentation/musickit)
- [MusicSubscriptionOffer](/documentation/musickit/musicsubscriptionoffer)
- MusicSubscriptionOffer.Options

Structure

# MusicSubscriptionOffer.Options

Options for loading subscription offers for Apple Music.

MusicKitSwiftUIiOS 15.0+iPadOS 15.0+Mac Catalyst 15.0+macOS 12.0+

```
struct Options
```

## [Topics](/documentation/musickit/musicsubscriptionoffer/options#topics)

### [Initializers](/documentation/musickit/musicsubscriptionoffer/options#Initializers)

[`init(action: MusicSubscriptionOffer.Action, messageIdentifier: MusicSubscriptionOffer.MessageIdentifier, itemID: MusicItemID?, affiliateToken: String?, campaignToken: String?)`](/documentation/musickit/musicsubscriptionoffer/options/init(action:messageidentifier:itemid:affiliatetoken:campaigntoken:))

Creates options for a subscription offer sheet with specific values for common properties.

### [Instance Properties](/documentation/musickit/musicsubscriptionoffer/options#Instance-Properties)

[`var action: MusicSubscriptionOffer.Action`](/documentation/musickit/musicsubscriptionoffer/options/action)

An action for the subscription offers entry point.

[`var affiliateToken: String?`](/documentation/musickit/musicsubscriptionoffer/options/affiliatetoken)

An affiliate token for the Apple Services affiliate program.

[`var campaignToken: String?`](/documentation/musickit/musicsubscriptionoffer/options/campaigntoken)

A campaign token for the Apple Services affiliate program.

[`var itemID: MusicItemID?`](/documentation/musickit/musicsubscriptionoffer/options/itemid)

An identifier for the music item the user is trying to access, which requires an active subscription.

[`var messageIdentifier: MusicSubscriptionOffer.MessageIdentifier`](/documentation/musickit/musicsubscriptionoffer/options/messageidentifier)

An identifier for selecting the main message that the subscription offer sheet presents to the user.

### [Type Properties](/documentation/musickit/musicsubscriptionoffer/options#Type-Properties)

[`` static let `default`: MusicSubscriptionOffer.Options ``](/documentation/musickit/musicsubscriptionoffer/options/default)

The default set of options for loading subscription offers for Apple Music.

## [Relationships](/documentation/musickit/musicsubscriptionoffer/options#relationships)

### [Conforms To](/documentation/musickit/musicsubscriptionoffer/options#conforms-to)

- [`Copyable`](/documentation/Swift/Copyable)
- [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible)
- [`Equatable`](/documentation/Swift/Equatable)
- [`Hashable`](/documentation/Swift/Hashable)
- [`Sendable`](/documentation/Swift/Sendable)
- [`SendableMetatype`](/documentation/Swift/SendableMetatype)
