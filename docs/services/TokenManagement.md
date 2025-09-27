# Token Management

> Source: Multiple Apple MusicKit documentation pages

This group contains classes, protocols, and types for managing tokens required to access the Apple Music API through MusicKit.

## MusicTokenProvider (typealias)
- **Swift Declaration**: `typealias MusicTokenProvider = MusicUserTokenProvider & MusicDeveloperTokenProvider`
- **Purpose**: An object that music requests use to access Apple Music API
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musictokenprovider)
- **Usage**: A token provider for MusicKit needs to be a subclass of [MusicUserTokenProvider](#musicusertokenprovider) which conforms to the [MusicDeveloperTokenProvider](#musicdevelopertokenprovider) protocol.

## MusicDeveloperTokenProvider
- **Swift Declaration**: `protocol MusicDeveloperTokenProvider : Sendable`
- **Purpose**: A set of methods that music requests use to access Apple Music API
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicdevelopertokenprovider)
- **Required Methods**:
  - `func developerToken(options: MusicTokenRequestOptions) async throws -> String` - Fetches and returns a developer token for Apple Music API
- **Inheritance**: [`Sendable`](/documentation/Swift/Sendable), [`SendableMetatype`](/documentation/Swift/SendableMetatype)
- **Conforming Types**: [DefaultMusicTokenProvider](#defaultmusictokenprovider)
- **Usage**: Implement this protocol to provide developer tokens for authenticating with the Apple Music API

## MusicUserTokenProvider
- **Swift Declaration**: `class MusicUserTokenProvider`
- **Purpose**: A class that music requests use to fetch user tokens your app requires to access Apple Music API
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musicusertokenprovider)
- **Initializers**:
  - `init()` - Creates a user token provider
- **Methods**:
  - `func userToken(for: String, options: MusicTokenRequestOptions) async throws -> String` - Fetches and returns a user token for Apple Music API
- **Inherited By**: [DefaultMusicTokenProvider](#defaultmusictokenprovider)
- **Usage**: Subclass this class to provide custom user token fetching logic

## DefaultMusicTokenProvider
- **Swift Declaration**: `class DefaultMusicTokenProvider`
- **Purpose**: The default token provider that music requests use to access Apple Music API
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/defaultmusictokenprovider)
- **Initializers**:
  - `init()` - Creates a user token provider
- **Inheritance**: Inherits from [MusicUserTokenProvider](#musicusertokenprovider)
- **Conformances**: [MusicDeveloperTokenProvider](#musicdevelopertokenprovider), [`Sendable`](/documentation/Swift/Sendable), [`SendableMetatype`](/documentation/Swift/SendableMetatype)
- **Usage**: The default implementation that provides both developer and user tokens. This is the standard token provider used by MusicKit unless you provide a custom implementation.

## MusicTokenRequestOptions
- **Swift Declaration**: `struct MusicTokenRequestOptions`
- **Purpose**: Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musictokenrequestoptions)
- **Type Properties**:
  - `static let ignoreCache: MusicTokenRequestOptions` - An option that indicates the token provider needs to discard any cached token and generate a new token
- **Conformances**: [`Equatable`](/documentation/Swift/Equatable), [`ExpressibleByArrayLiteral`](/documentation/Swift/ExpressibleByArrayLiteral), [`OptionSet`](/documentation/Swift/OptionSet), [`RawRepresentable`](/documentation/Swift/RawRepresentable), [`Sendable`](/documentation/Swift/Sendable), [`SendableMetatype`](/documentation/Swift/SendableMetatype), [`SetAlgebra`](/documentation/Swift/SetAlgebra)
- **Usage**: Use these options to control token fetching behavior, such as forcing a refresh of cached tokens

## MusicTokenRequestError
- **Swift Declaration**: `enum MusicTokenRequestError`
- **Purpose**: An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/musictokenrequesterror)
- **Enumeration Cases**:
  - `case developerTokenRequestFailed` - An error that indicates a failure in the process of fetching a developer token for the current app
  - `case permissionDenied` - An error that occurs when the user doesn't consent for the current app to access their Apple Music data
  - `case privacyAcknowledgementRequired` - An error that occurs when the user needs to acknowledge the most recent privacy policy
  - `case unknown` - An error indicating the ocurrence of an unknown or unexpected error
  - `case userNotSignedIn` - An error that occurs when the user isn't signed in with an Apple Music account
  - `case userTokenRequestFailed` - An error that indicates a failure in the process of fetching a user token
  - `case userTokenRevoked` - An error that occurs when the user revokes permission for the current app to access their Apple Music data
- **Conformances**: [`Copyable`](/documentation/Swift/Copyable), [`CustomStringConvertible`](/documentation/Swift/CustomStringConvertible), [`Equatable`](/documentation/Swift/Equatable), [`Error`](/documentation/Swift/Error), [`Hashable`](/documentation/Swift/Hashable), [`LocalizedError`](/documentation/Foundation/LocalizedError), [`RawRepresentable`](/documentation/Swift/RawRepresentable), [`Sendable`](/documentation/Swift/Sendable), [`SendableMetatype`](/documentation/Swift/SendableMetatype)

## Usage Patterns

### Using the Default Token Provider
```swift
// The default token provider is used automatically by MusicKit
// No explicit setup required for basic usage
```

### Custom Token Provider Implementation
```swift
class CustomTokenProvider: MusicUserTokenProvider, MusicDeveloperTokenProvider {
    func developerToken(options: MusicTokenRequestOptions) async throws -> String {
        // Custom logic to fetch developer token
        // This might involve loading from a secure store, network request, etc.
        return "your_developer_token"
    }

    override func userToken(for developerToken: String, options: MusicTokenRequestOptions) async throws -> String {
        // Custom logic to fetch user token
        // This typically involves making a request to Apple's token service
        return try await super.userToken(for: developerToken, options: options)
    }
}
```

### Handling Token Request Errors
```swift
do {
    let token = try await tokenProvider.developerToken(options: [])
} catch MusicTokenRequestError.developerTokenRequestFailed {
    // Handle developer token fetch failure
} catch MusicTokenRequestError.permissionDenied {
    // Handle permission denied
} catch MusicTokenRequestError.userNotSignedIn {
    // Handle user not signed in
} catch MusicTokenRequestError.userTokenRevoked {
    // Handle revoked user token
} catch {
    // Handle other errors
}
```

### Using Token Request Options
```swift
// Force refresh of cached tokens
let options: MusicTokenRequestOptions = .ignoreCache
let freshToken = try await tokenProvider.developerToken(options: options)
```

## Token Flow Overview

1. **Developer Token**: A JWT token that identifies your app to Apple Music API
   - Generated using your private key and team ID
   - Required for all Apple Music API requests
   - Provided through `MusicDeveloperTokenProvider.developerToken(options:)`

2. **User Token**: A token that represents the user's permission to access their Apple Music data
   - Obtained after user authorization
   - Used in conjunction with developer token for user-specific API calls
   - Provided through `MusicUserTokenProvider.userToken(for:options:)`

3. **Token Caching**: MusicKit automatically caches tokens to improve performance
   - Use `MusicTokenRequestOptions.ignoreCache` to force refresh
   - Tokens are automatically refreshed when they expire

## Security Considerations

- Developer tokens should be generated server-side when possible
- Never embed private keys in client applications
- User tokens are automatically managed by MusicKit
- Implement proper error handling for token-related failures
- Consider implementing retry logic for transient token failures