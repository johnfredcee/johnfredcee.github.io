Title: Creating a Data Asset Instancce in Blueprint
Category: Blueprint, Unreal, DataAsset
Slug: Blueprint creation of Data Asset Instance
Summary: How to create a Data Asset Instance in Blueprint

This is just a quick blog, as I saw some people struggling with this and having to use external plugins to do this, and hope Google will direct people to this, post, eventually!

 Creating a Data Asset isd  possible now, in 5.3. I think this will work with 5.0 upwards, as it relies on the Geometry Script implementation to create a unique asset name and path.  You need to enable viewing C++ classes in the content browser to select the data asset class if it's a native class. Also, you do not need a factory, which is just as well as creating a UDataAssetFactory seems to be prolematic in both C++ and Blueprint. 

![Creating A Data Asset Instance]({static}images/creatingdataasset.png)