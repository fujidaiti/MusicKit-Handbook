# Getting Started with MusicKit

> Source: Multiple Apple MusicKit documentation pages

This guide provides essential information for getting started with MusicKit development.

## Using MusicKit to Integrate with Apple Music

> Source: https://developer.apple.com/documentation/musickit/using_musickit_to_integrate_with_apple_music

Find an album in Apple Music that corresponds to a CD in a user's collection, and present the information for the album.

[Download Sample Code](https://docs-assets.developer.apple.com/published/d249435221/UsingMusicKitToIntegrateWithAppleMusic.zip)

**Requirements:** iOS 15.0+, iPadOS 15.0+, Xcode 13.0+

### Overview

**Note:** This sample code project is associated with WWDC21 session [10294: Meet MusicKit for Swift](https://developer.apple.com/wwdc21/10294/).

### Configure the Sample Code Project

This sample code project must be run on a physical device.

Before you run the sample code project in Xcode, perform the following steps:

1. In the Project navigator, select the project and click the *Signing & Capabilities* tab.
2. Select your developer team from the *Team* menu.
3. Choose a new bundle identifier for the `MusicAlbums` target, and enter it in the Bundle Identifier field. The bundle identifier within the project has an associated App ID, so you need a unique identifier to create your own App ID. Use a reverse-DNS format for your identifier, as [Preparing your app for distribution](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution) describes.
4. In Safari, visit the [Certificates, Identifiers, and Profiles](https://developer.apple.com/account/resources) section of the developer web site.
5. Select *Identifiers* and click the Add button to create a new App ID for `MusicAlbums`. Follow the steps until you reach the *Register an App ID* page.
6. For the Bundle ID, select *Explicit*, and enter the bundle identifier from step 2.
7. Click the *App Services* tab, and select the MusicKit checkbox.
8. Complete the App ID creation process.

After creating your App ID, your Xcode project needs no additional configuration. The MusicKit App Service is a run-time service that automatically associates with your app's bundle ID.

## Automatic Token Generation Setup

> Source: https://developer.apple.com/documentation/musickit/using-automatic-token-generation-for-apple-music-api

Enable your app's integration with the MusicKit App Service in the developer portal.

### Overview

MusicKit accelerates the way you integrate your app with Apple Music API by automatically generating the developer token on behalf of your app. It then includes the developer token in requests that it issues to Apple Music API for your app.

To benefit from this automatic behavior, just enable the MusicKit App Service in the developer portal for your app. The MusicKit App Service is a runtime service that automatically associates with your app's bundle identifier.

### Enable the MusicKit App Service

1. In Safari, visit the [Certificates, Identifiers, and Profiles](https://developer.apple.com/account/resources) section of the developer web site.
2. In the Identifiers subsection, open the App ID for your app and begin editing its configuration, or create a new one.
3. On the Register an App ID page, select the Explicit option for the bundle ID of your app.
4. Click or tap the App Services tab, and select the Enabled checkbox for MusicKit.
   ![Enable MusicKit App Service](https://docs-assets.developer.apple.com/published/15116a1f8bdf6b3ea80e61fbd7bf8857/Enable-MusicKit-App-Service%402x.png)
5. Complete the App ID creation process, or save the changes.

Be sure to set the bundle identifier of your app target to the same value you use for your App ID in these steps.

## Exploring More Content

> Source: https://developer.apple.com/documentation/musickit/explore_more_content_with_musickit

Track your outdoor runs with access to the Apple Music catalog, personal recommendations, and your own personal music library.

[Download Sample Code](https://docs-assets.developer.apple.com/published/4a4767bbca/ExploreMoreContentWithMusicKit.zip)

**Requirements:** iOS 16.0+, iPadOS 16.0+, Xcode 14.0+

### Overview

**Note:** This sample code project is associated with WWDC22 session [110347: Explore more content with MusicKit](https://developer.apple.com/wwdc22/110347/).

### Configure the Sample Code Project

This sample code project doesn't work in the simulator. Before you run the sample code project in Xcode, perform the following steps:

1. In Xcode's Project navigator, select the project, and click the Signing & Capabilities tab.
2. From the Team pop-up menu, choose your developer team.
3. In the Bundle Identifier field, enter a new bundle ID for the MusicMarathon target. The bundle identifier for the project has an associated App ID, so you need a unique identifier to create your own App ID. Use a reverse-DNS format for your identifier, as [Preparing your app for distribution](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution) describes.
4. In Safari, visit the [Certificates, Identifiers, and Profiles](https://developer.apple.com/account/resources) section of the Apple Developer website.
5. Select Identifiers, and click the Add button to create a new App ID for `MusicMarathon`. Follow the steps until you reach the Register an App ID page.
6. For the Bundle ID, select Explicit, and enter the bundle ID from step 2.
7. Click the App Services tab, and select the MusicKit checkbox.
8. Complete the App ID creation process.

After creating your App ID, your Xcode project needs no additional configuration. The MusicKit app service is a runtime service that automatically associates with your app's bundle ID.

## Related Resources

### Essential Documentation
- [Using Automatic Developer Token Generation for Apple Music API](#automatic-token-generation-setup)
- [Using MusicKit to Integrate with Apple Music](#using-musickit-to-integrate-with-apple-music)
- [NSAppleMusicUsageDescription](/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) - A message that tells people why the app is requesting access to their media library.

### WWDC Sessions
- [WWDC21 Session 10294: Meet MusicKit for Swift](https://developer.apple.com/wwdc21/10294/)
- [WWDC22 Session 110347: Explore more content with MusicKit](https://developer.apple.com/wwdc22/110347/)

### Sample Code Downloads
- [Using MusicKit to Integrate with Apple Music](https://docs-assets.developer.apple.com/published/d249435221/UsingMusicKitToIntegrateWithAppleMusic.zip)
- [Explore More Content with MusicKit](https://docs-assets.developer.apple.com/published/4a4767bbca/ExploreMoreContentWithMusicKit.zip)