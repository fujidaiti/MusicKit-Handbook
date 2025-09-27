# Support Types

> Source: Multiple Apple MusicKit documentation pages

This section contains supporting types used for specialized functionality within MusicKit, including sectioned library requests and other utility structures.

## TitledSection
- **Swift Declaration**: `struct TitledSection`
- **Purpose**: A section you can use to request items from the library grouped by title.
- **Source**: [Apple MusicKit Documentation](https://developer.apple.com/documentation/musickit/titledsection)
- **Properties**:
  - `id: MusicItemID`: The unique identifier for the titled section
  - `title: String`: The title of the section
- **Methods**: None specified
- **Usage**: Used with library sectioned requests to organize items alphabetically or by other title-based groupings. For example, when performing a library sectioned request of albums, the library sectioned response will contain albums grouped by the first letter of their title, and the `title` property of this section will be equal to that first letter. This enables efficient navigation and display of large collections organized by title.
- **Conforms To**: `Copyable`, `Equatable`, `Hashable`, `Identifiable`, `MusicLibrarySectionRequestable`, `Sendable`