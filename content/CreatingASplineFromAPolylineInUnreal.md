Title: Creating a Spline Component from a Polyline in Unreal
Category: Blueprint, Unreal, SplineComponent
Slug: C++ creation of a Spline Component in Unreal 
Summary: How to create a Spline Component at runtime in Unreal

The Spline Component API in Unreal is a very fat one with lots of methods in it, and it's not entirely clear how to use it at first glance. Like creating a Data Asset Instance, it's a question that crops up and doesn't always get seem to be answered. After a brief bit of experimentation I found it's much easier than it fist appears. Essentially the only function you actually need is `AddSplinePointAtIndex(InPoint, AddIdx, ESplineCoordinateSpace::Local);`

The main snag with the code below is the fact it's compiled into a game module rather than an editor module and the viewport is not updated when the component is attached to the actor. If you are in editor code, `GEditor->RedrawLevelEditingViewports(true);` should update the viewport for you, but this won't link in a game module, obviously.

Here is the gist!

[gist:id=a75b8c249cfa33c8760d60a10f71f2b6]
