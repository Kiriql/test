# Drone_Simulation
 Drone Training Simulator Proof of Concept project for CIMSOLUTIONS



---
# Requirements
- [Visual Studio](https://visualstudio.microsoft.com) with the following packages installed
  - Game Development C++
  - Desktop Development C++
  - Python
  - .NET C#
- [Runtime SDK version 3.0](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-3.1.32-windows-x64-installer?cid=getdotnetcore)
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Unreal Engine](https://www.unrealengine.com/en-US/download) 5.0.3, Higher version will require rebuilding of the project files, this comes with risks
  - [Unreal Plugins](https://marketplace-website-node-launcher-prod.ol.epicgames.com/ue/marketplace/en-US/store)
    - [Sirius Utility Nodes](https://marketplace-website-node-launcher-prod.ol.epicgames.com/ue/marketplace/en-US/product/sirius-utility-nodes)
    - [Ryan's Helpful Helpers](https://marketplace-website-node-launcher-prod.ol.epicgames.com/ue/marketplace/en-US/product/ryan-s-helpful-helpers)
    - [Async Loading Screen](https://marketplace-website-node-launcher-prod.ol.epicgames.com/ue/marketplace/en-US/product/async-loading-screen)

# Hardware Requirements
Recommended specs are:
## System
- New-isch CPU with 6+ physical cores
  - Intel i5 11th Gen+
  - AMD Ryzen 7 Gen 3+
- GPU with the capacity for VR applications
  - NVIDIA 20 series GPU or later, recommended with 8GB+ VRAM
  - AMD Cards not tested, but RX 6600XT 8GB VRAM should work

## Memory
- At least 8 GB+ of Main Memory, RAM

## Disk
- At Least 70+ GB of space for the Engine and the project files
- Recommended it being an SSD

Program was developed and tested on 2 PC's with the following specs:

### PC 1: 
- AMD Ryzen 7 5800x
- 32GB 3000mhz RAM 
- NVIDIA 2070 Super 8GB VRAM
- SSD and HDD tested, loading times are a lot better on SSD

### PC 2:
- Intel i5 11400f
- 16GB 2666mhz RAM
- NVIDIA 3060 12GB VRAM
- SSD 



# Getting Started

1. First you want to install [Visual Studio](https://visualstudio.microsoft.com)
   - Using the Visual Studio Installer download the required packages listed above
2. If not already installed on your system download the [Epic Games Launcher](https://www.unrealengine.com/en-US/download)
   - Next, go to the unreal engine tab in the Epic Games Launcher and install the Unreal Engine version 5.0.3. 
   This will take a while.
   - After the engine has finished installing. Find the 3 Plugins listed above in the [Marketplace](https://marketplace-website-node-launcher-prod.ol.epicgames.com/ue/marketplace/en-US/store) and install them into the Engine using the Epic Games Launcher.
3. While waiting for Unreal Engine to install, clone this project repository to a drive on your PC using the following comand. A SSD is recommended for faster loading times for the editor and inside the application.
```
git clone https://github.com/KingPungy/Drone_Simulation_UE.git
```
4. you open the project by either opening the Unreal engine via Epic games and then selecting the .uproject file by hand, OR , launch the project by double clicking the .uproject file in the repository folder.




# Features

## *Making a training*
Placing the *__Module Sequencer__* in a level will allow a developer to create a training with a given Module Order

## *Making a Module*
Making a Child class of the __*Base_Module*__ class allows you to add custom logic to the child and create a new custom module that can be using in a training.
Each Module can have its own way of showing Progress using the Progress Widget Variable with stores a __*User Widget*__

## *Wind Module*
Adding wind to a training is as simple as placing a *__Wind Module__*. Rotating the *__Wind Direction component__* inside the object allows you to decide the way the wind and the wind particles move.

## *Menu*
In the *__Main Menu__*, you can add a new training by adding a new *__Level Preview Widget__* to the Level grid inside the __Play__/*Level Selection Tab*. The level preview widget can be used to open a level and a specific training theirin, this allows the developer to re-use a map for multiple trainings.

## *Level options*
While on the Level Selection menu you can access the *__Level Options__*.   
Here you can change the difficulty of the training by changing the amount of *__Hits__* the drone is allowed to make during a training.    
The *__Time__* can also be changed in 50% increments: 
- *__Easy__*: 50% more time, 
- *__Normal__*: Set time by Training, 
- *__Hard__*: 50% less time, 
- *__Free Flight__*: No Time requirement

## *Tutorial Messages*
All Messages use the same Structure. This structure contains:
- A Title
- An Image
- Text  

Using this tutorial inside a training the developer can give the user extra info about a module aside from the explanation inside the UI.
