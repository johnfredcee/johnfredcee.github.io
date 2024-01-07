Title: Creating a Component At Edit time
Category: Unreal, Components, DetailsPanel
Slug: Creating and making a component visible in the Unreal Editor
Summary: Creating a Component At Edit time and updating the Details Panel

I am currently writing quite a bit of editor code that involves creting and attaching components to Actors at Edit time (yes, more procedural geometry). I have noticed there's a lot of information on doing this, but they all have one flaw: the created component does not become visible in the details panel immediately. 

The component creation sequence goes something like this:
    
```cpp
    HeterogeneousVolumeComponent =
        NewObject<UHeterogeneousVolumeComponent>(this, TEXT("MeshPainterVolumeComponent"));
    if (ensure(HeterogeneousVolumeComponent))
    {
        HeterogeneousVolumeComponent->RegisterComponent();
        HeterogeneousVolumeComponent->AttachToComponent(GetRootComponent(), FAttachmentTransformRules::KeepRelativeTransform);
        HeterogeneousVolumeComponent->CreationMethod = EComponentCreationMethod::Instance;
```

This is the usual sqeuence, but it has one flaw - the details panel of the actor containing the components is not updated. For that you will need the `LevelEditor` module. Which is the module that manages all the details panels, scene outliners and other Slate Windows. We could dig into the SLevelEditor instance and find our details panel and refresh it, but fortunately, it seems there's ComponentEdited event which will do it for us.

```cpp
         FLevelEditorModule* LevelEditorPtr{FModuleManager::Get().LoadModulePtr<FLevelEditorModule>("LevelEditor")};
		if (LevelEditorPtr)
		{
         LevelEditorPtr->BroadcastComponentsEdited();      
		}
    }
```

And that's it; it's a small change but it makes your tool so much more useable!

