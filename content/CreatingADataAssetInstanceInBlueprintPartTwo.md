Title: Creating a Data Asset Instance in Blueprint Again
Category: Blueprint, Unreal, DataAsset
Slug: Blueprint creation of Data Asset Instance Again
Summary: Creating a Data Asset Instance in Blueprint at Runtime

It turns out there's a better way to create a Data Asset instance at runtime than the blog I posted earlier, which relied on a function in the Geometry Scripting Library. There is a function in the Asset Tools Library which also creates unique asset names, but in true Epic fashion it's tricky to use and undocumented.

The Asset Tools function, `CreateUniqueAssetName` is bit of a strange one. It takes a base package name, including an asset name and appends a suffix. If the suffix is numeric and about one, the suffix will auto-increment to the fist available suffix value each time a new asset is created. Which is completely not a use-confounding way to things!

Without further ado, I present the right way to create an asset at edit time  without needing an asset fractory, in Blueprint. Hope it helps some poor sod who stumbles on this via their search engine.

You will want to open the image in a new tab to see it in all it's glory!

![Creating A Data Asset Instance With Asset Tools]({static}images/creatingdataassetredux.png)