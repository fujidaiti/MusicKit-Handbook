# Authorization & Subscription

> Source: Multiple Apple MusicKit documentation pages

This group contains classes and structures for managing user authorization and subscription status for Apple Music access in MusicKit.

## MusicAuthorization
- **Swift Declaration**: `struct MusicAuthorization`
- **Purpose**: A type that allows you to request the user's informed consent for your app to access their music data
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicauthorization)
- **Type Properties**:
  - `static var currentStatus: MusicAuthorization.Status` - The authorization status the user sets for accessing MusicKit
- **Type Methods**:
  - `static func request() async -> MusicAuthorization.Status` - Asks the user for permission for the current app to access MusicKit
- **Nested Types**:
  - `enum Status` - A value that indicates the authorization status the user sets for the current app to access their Apple Music data
- **Usage**: Use this structure to check the current authorization status and request permission from users to access their Apple Music data

## MusicAuthorization.Status
- **Swift Declaration**: `enum Status`
- **Purpose**: A value that indicates the authorization status the user sets for the current app to access their Apple Music data
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicauthorization/status)
- **Enumeration Cases**:
  - `case authorized` - The user granted permission for the current app to use MusicKit
  - `case denied` - The user denied permission for the current app to use MusicKit
  - `case notDetermined` - The user has yet to decide whether to authorize the current app to use MusicKit
  - `case restricted` - Apps on this device can't access MusicKit in a way that the user can't change
- **Conformances**: [`Copyable`](/documentation/Swift/Copyable), [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible), [`Equatable`](/documentation/Swift/Equatable), [`Hashable`](/documentation/Swift/Hashable), [`RawRepresentable`](/documentation/Swift/RawRepresentable), [`Sendable`](/documentation/Swift/Sendable), [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## MusicSubscription
- **Swift Declaration**: `struct MusicSubscription`
- **Purpose**: A representation of the current state of the user's subscription to Apple Music
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicsubscription)
- **Instance Properties**:
  - `let canBecomeSubscriber: Bool` - A capability that allows your app to present subscription offers for Apple Music
  - `let canPlayCatalogContent: Bool` - A capability that allows your app to play subscription content using a music player
  - `let hasCloudLibraryEnabled: Bool` - A capability that allows your app to perform modifications to the user's iCloud Music Library
- **Type Properties**:
  - `static var current: MusicSubscription` - The current state of the user's subscription to Apple Music
  - `static var subscriptionUpdates: MusicSubscription.Updates` - An asynchronous sequence to use for observing updates to the current state of the user's subscription to Apple Music
- **Nested Types**:
  - `struct Updates` - An asynchronous sequence to use for observing updates to the current state of the user's subscription to Apple Music
  - `enum Error` - An error that MusicKit can throw upon requesting the current music subscription of the user
- **Conformances**: [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible), [`Equatable`](/documentation/Swift/Equatable), [`Hashable`](/documentation/Swift/Hashable), [`Sendable`](/documentation/Swift/Sendable), [`SendableMetatype`](/documentation/Swift/SendableMetatype)
- **Usage**: Use this structure to determine what Apple Music capabilities are available to the user and observe changes to their subscription status

## MusicSubscription.Error
- **Swift Declaration**: `enum Error`
- **Purpose**: An error that MusicKit can throw upon requesting the current music subscription of the user
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicsubscription/error)
- **Enumeration Cases**:
  - `case permissionDenied` - An error indicating that the user doesn't consent for your app to access their Apple Music data
  - `case privacyAcknowledgementRequired` - An error indicating that the user needs to acknowledge the most-recent privacy policy for Apple Music
  - `case unknown` - An error indicating the ocurrence of an unknown or unexpected error
- **Conformances**: [`Copyable`](/documentation/Swift/Copyable), [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible), [`Equatable`](/documentation/Swift/Equatable), [`Error`](/documentation/Swift/Error), [`Hashable`](/documentation/Swift/Hashable), [`LocalizedError`](/documentation/Foundation/LocalizedError), [`RawRepresentable`](/documentation/Swift/RawRepresentable), [`Sendable`](/documentation/Swift/Sendable), [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## MusicSubscriptionOffer
- **Swift Declaration**: `struct MusicSubscriptionOffer`
- **Purpose**: A type for grouping other types for showing subscription offers for Apple Music
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicsubscriptionoffer)
- **Nested Types**:
  - `struct Action` - A representation of the entry point for the sheet with subscription offers for Apple Music
  - `struct MessageIdentifier` - An identifier for the main message that the subscription offer sheet presents to the user
  - `struct Options` - Options for loading subscription offers for Apple Music
- **Usage**: Use this structure to present subscription offers to users who are not Apple Music subscribers
- **Framework**: Available in MusicKitSwiftUI

## MusicSubscriptionOffer.Action
- **Swift Declaration**: `struct Action`
- **Purpose**: A representation of the entry point for the sheet with subscription offers for Apple Music
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicsubscriptionoffer/action)

## MusicSubscriptionOffer.MessageIdentifier
- **Swift Declaration**: `struct MessageIdentifier`
- **Purpose**: An identifier for the main message that the subscription offer sheet presents to the user
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicsubscriptionoffer/messageidentifier)

## MusicSubscriptionOffer.Options
- **Swift Declaration**: `struct Options`
- **Purpose**: Options for loading subscription offers for Apple Music
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicsubscriptionoffer/options)

## Usage Patterns

### Checking Authorization Status
```swift
let status = MusicAuthorization.currentStatus
switch status {
case .authorized:
    // User has granted permission
case .denied:
    // User has denied permission
case .notDetermined:
    // Request permission
    let newStatus = await MusicAuthorization.request()
case .restricted:
    // Access is restricted
}
```

### Checking Subscription Capabilities
```swift
let subscription = MusicSubscription.current
if subscription.canPlayCatalogContent {
    // User can play Apple Music catalog content
}
if subscription.hasCloudLibraryEnabled {
    // User can modify their iCloud Music Library
}
if subscription.canBecomeSubscriber {
    // User can be presented with subscription offers
}
```

### Observing Subscription Updates
```swift
for await subscription in MusicSubscription.subscriptionUpdates {
    // Handle subscription status changes
}
```