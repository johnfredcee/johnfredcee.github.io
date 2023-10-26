Title: UMG Polyline Editor Widget
Category: Slate, Unreal
Date: 2023-10-23 11:27
Slug: Wrapping Slate Control in UMG
Summary: Implementation a Polyline Editor UMG Widget

The Polyline editor I blogged about last time is a Slate Widget; the ultimate goal is to use it as a UMG control as it enables much faster implementation of useful Editor tools like this one ![Profile Editor Widget]({static}images/profileeditor.png)

Fortunaely this is an even more straightforward process than the creation of the Slate Control. It derives from `UWidget` and not `UUserWidget`. It turns out that `UUserWidget` is for Blueprint classes to derive from and if you derive from this in C++, the widget will NOT appear in the Widget palette; this behaviour is hardcoded into the engine and was the source of some inital confusion. So, here is the code to achive that!


[gist:id=cc077687b9c9172f9d75b7c22761eff6]

[gist:id=b3166d9eabaa70ba3871547a27a8ea85]


The properties of the Slate Control that we want to expose to the user are exposed as UProperties. These are passed to the Slate Control in it's constructor as SLATE_ARGUMENTS and the control is constructed in the `RebuildWidget` method that is overriden from `UWidget`

Other functions that have to be implemented are `ReleaseSlateResources` which destroys the Slate Control; `SynchronizeProperties` which sets the members of the slate control to the values of the UPROPERTIES of the widget, creating a communication conduit from UMG properties to the Slate control members. 

One of the members of the widget is an array of points. In the control the points are deleted, modified and created by mouse clicks, so I implemented a sequence of functions in the widget `HandlePointAdded`, `HandlePointRemoved`. and `HandlePointModified` which call multicast delegates for the user of the control to potentially hook in to.

One last function to override is `GetPaletteCategory` to define what cateogry it appears in, in the UMG Widget palette; I created a new category `Geometry` because my code is so important, it deserves it's own cateogory like that!

