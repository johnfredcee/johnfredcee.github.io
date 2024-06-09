Title: Using Visual Studio Code and other ClangD based Editors with Unreal
Date: 2024-06-09 15:45
Category: Unreal, VisualStudioCode, UnrealBuildTool, Clangd
Slug: Using compilation databases with Visual Studio Code
Summary: How to use UBT to generate useful compile_commands.json files

I very much like Visual Studio Code: as an old Emacs (and Vi!) hand I have a thing about editor responsiveness. I'm conviced there's a sweet spot involving the speed of human cognition and a programs response time, or perhaps I'm just an impatient git.

The problem with Visual Studio Code is that the Microsft C++ plugin and Unreal's Visual Studio Code generator leads to a poor experience.

For non-Unreal based projects I use a thing called [ClangD](https://clangd.llvm.org/), which when coupled with it's Visual Studio Code [plugin](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd) which results in very fast autocompletion and project navigation. Orders of magnitude faster than the Microsoft plugin, and catches lots of compilationm errors on the fly, as it's a compilation server compiling your code in the background, and calling you out when you make a mistake. The trouble is, that to do this it needs a compilation database in a file called `compile_commands.json`, containing the command line used to compile each .cpp file in the project. 

The Unreal Engine VSCode generator is not set up to take advantage of this; it breaks the `compile_commands.json` files into multiple files, each per Unreal build target as an individual C++ project: which suits the Microsoft C++ plugin. However, the Clangd server completely fails to work with it.

After a lot of poking about in the Unreal Source and writing my own generator, I realised that there is a way to generate a compilation database suitable for the Visual Studio Code ClangD plugin (and other editors that use the compilation database - there are quite a few).

Here is the recipie, as tested with the latest version of 5.4 off github (so, probably 5.4.2)

First and most obviously your Source Code Editor Setting needs to be set to Visual Studio Code.

Secondly, some parameters have to be passed to the Visual Studio Code project generator, to ensure it doesn't try to create it's own Microsoft-centric compilation databases. To do this you need to create an `.xml` file at `%USERPROFILE%\AppData\Roaming\Unreal Engine\UnrealBuildTool` called `BuildConfiguration.xml` - this controls the behavior of Unreal Build Tool. It shuld look like this.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Configuration xmlns="https://www.unrealengine.com/BuildConfiguration">
  <ProjectFileGenerator>
	<Format>VisualStudioCode</Format>
  </ProjectFileGenerator>
    <VSCodeProjectFileGenerator>
        <AddDebugAttachConfig>true</AddDebugAttachConfig>
        <NoCompileCommands>true</NoCompileCommands>
    </VSCodeProjectFileGenerator>
</Configuration>
```

This stops the Visual Studio Code project file generator creating any compile_command.json files, and also adds a handy debug target for just attching to a process into the Visual Studio Code debug configuration.

So, now, how do you generate the compilation database? Well, there is a mode in the UnrealBuildTool to do exactly that. For some reason, it's not a project file generator, which is a bit strange, but there are probably architectural reasons.

In my case I generate the compilation database with the following batch file - called `GenerateClangDatabase.bat` - in the root folder of my project engine installation. Sandbox is the name of my generic Sandbox game project. It lives in the Projects\ folder under the Unreal Engine root directory. It's not a foreign project in a uproject filr outside of the engine source tree. I am unsure if this setup will work with those - if anyone does try it and gets it to work, I'd love to know.  

```bat
dotnet .\Engine\Binaries\DotNet\UnrealBuildTool\UnrealBuildTool.dll -Mode=GenerateProjectFiles SandboxEditor Development Win64
dotnet .\Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.dll -Mode=GenerateClangDatabase -NoPCH -DisableUnity -NoExecCodeGenActions SandboxEditor Development Win64
```

The `-NoPCH` and `-DisableUnity` command lines appear to be important; the unity build and shared pchs upset the database generator which likes to work file by file. Generating the database takes about 50 seconds on my machine (it's not actually compiling anyting). The `-NoExecCodeGenActions` prevents the databse generator building some generated files, and speeds up the generation process. So far, the lack of these has not been a problem.

Note also, it is important to use the version of clangd that matches the version of Clang that Epic is currently using - at present, that was version 15, which cam be downloaded [here](https://github.com/llvm/llvm-project/releases/tag/llvmorg-15.0.6). You have to install your own version of LLVM, and put it on your PATH - do not download the latest version when prompted to by the plugin! 

It's somewhat fiddly, I admit - but the results are worth it, in my opinion. VSCode is not an IDE, but this gets it within spitting distance, without sacrificing responsiveness. It's how I like it!
