# Data Request API

> Source: Multiple Apple MusicKit documentation pages

The Data Request API provides low-level access to Apple Music API endpoints through direct HTTP requests. This API allows developers to make custom requests to any Apple Music API endpoint and handle raw responses.

## MusicDataRequest

- **Swift Declaration**: `struct MusicDataRequest`
- **Purpose**: A request for loading data from an arbitrary Apple Music API endpoint.
- **Source**: https://developer.apple.com/documentation/musickit/musicdatarequest

### Properties

- `let urlRequest: URLRequest` - The URL request for the data request.

### Type Properties

- `static var currentCountryCode: String` - Fetches the current country code for the user's Apple Music account.
- `static var tokenProvider: any MusicUserTokenProvider & MusicDeveloperTokenProvider` - The shared token provider for fetching tokens that Apple Music API requires.

### Methods

#### Initializers
- `init(urlRequest: URLRequest)` - Creates a data request with a URL request.

#### Response Method
- `func response() async throws -> MusicDataResponse` - Fetches data from the Apple Music API endpoint that the URL request defines.

### Conformances

- `Copyable`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `Sendable`
- `SendableMetatype`

### Nested Types

#### Error
- **Swift Declaration**: `struct Error`
- **Purpose**: An error that the Apple Music API returns.

##### Properties
- `let code: Int` - The specific code for the underlying cause of the error.
- `let detailText: String` - Additional detailed information about the cause of the error.
- `let id: String` - The identifier for the error.
- `let originalResponse: MusicDataResponse` - The original response that contains the error.
- `let source: MusicDataRequest.Error.Source?` - The source of the error.
- `let status: Int` - The HTTP status code for the error.
- `let title: String` - A developer-friendly title for the error.

##### Conformances
- `Copyable`
- `CustomStringConvertible`
- `Error`
- `Sendable`
- `SendableMetatype`

#### Error.Source
- **Swift Declaration**: `enum Source`
- **Purpose**: A representation of the source of an error from Apple Music API.

##### Cases
- `case parameter(String)` - The URI query parameter that causes the error.

##### Conformances
- `Copyable`
- `CustomStringConvertible`
- `Equatable`
- `Sendable`
- `SendableMetatype`

## MusicDataResponse

- **Swift Declaration**: `struct MusicDataResponse`
- **Purpose**: An object containing results for a data request.
- **Source**: https://developer.apple.com/documentation/musickit/musicdataresponse

### Properties

- `let data: Data` - The raw data returned by the Apple Music API endpoint for the originating data request.
- `let urlResponse: HTTPURLResponse` - The URL response returned by the Apple Music API endpoint for the originating data request.

### Conformances

- `Copyable`
- `CustomDebugStringConvertible`
- `CustomStringConvertible`
- `Equatable`
- `Hashable`
- `Sendable`
- `SendableMetatype`

## Usage

The Data Request API provides direct access to Apple Music API endpoints for advanced use cases:

1. **Custom API Endpoints**: Use `MusicDataRequest` when you need to access Apple Music API endpoints that don't have dedicated MusicKit request types.

2. **Raw Data Access**: The API returns raw `Data` objects, allowing you to handle custom response formats or implement your own parsing logic.

3. **Error Handling**: Comprehensive error information is provided through the nested `Error` type, including HTTP status codes, error details, and parameter-specific error sources.

4. **Token Management**: The API automatically handles authentication tokens through the shared `tokenProvider`, simplifying access to authenticated endpoints.

This API is particularly useful for:
- Accessing new or experimental Apple Music API endpoints
- Implementing custom caching strategies
- Building wrapper libraries or custom abstractions
- Handling specialized response formats not covered by higher-level MusicKit APIs