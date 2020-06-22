# **Substance Automation Toolkit - Samples** [![License](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=flat)](http://mit-license.org)
This repository contains a few samples for using the [Substance Automation Toolkit](https://docs.substance3d.com/sat) and providing a framework of examples for introducing automation in a content development pipeline. 

The provided examples are split into two categories: 
- using the [Command Line Tools](https://docs.substance3d.com/sat/command-line-tools)
- using the [Python API](https://docs.substance3d.com/sat/pysbs-python-api).


_Note: This repository demonstrates **only** the following concepts: (code can be easily modified to achieve most other available options)_
- _Headless Bent-Normal Map texture baking from a list of [low_poly, high poly] pairs, with outputting the results in a predefined location_
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
## Command Line Tools
### On Windows 10
To use the sample code with the Command Line Tools, first:
#### 1) Have the Substance Suite installed
#### 2) Create the output folder
#### 3) Edit the **source.txt** file contents.
In the text file, each row is a pairing of low and high poly paths separated by a space, as seen below.
```
<path_to_low_poly> <path_to_high _poly>
```
For example:
```
C:\substance_test\lows\my_asset_low.fbx C:\substance_test\highs\my_asset_high.fbx
```
Modify the file to list your matchings.
#### 4) Open the **sbs_bentnormal_baker.bat** with a text editor.
#### 5) Line 18 can be modified to point to a different install path if your Substance installation is not default.
```
18:        cd "C:\Program Files\Allegorithmic\Substance Automation Toolkit" >nul
```
#### 6) Line 25 can be modified to change the output path of the exported bakes.
```
25:        --output-path "C:\bakes\output_folder" ^
```
#### 7) Line 26 can be modified to change the format of the exported name.
```
26:        --output-name "{inputName}_BN" ^
```
#### 8) Other parameters in between lines 23 and 33 can be modified (or added) to change the properties of the bake process.
*  *  *  *  *
### On Mac OS X Catalina
Examples currently unavailable, but can be kickstarted using the Windows 10 examples and the Substance Automation Toolkit documentation.

*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
## Python API (called Pysbs)
The samples setup with **Pysbs Python API** in this repository are using Python 2.7 (more specifically 2.7.18).  The Pysbs Python API requires a bit more setup, but is more extensive and configurable than the Command Line Tools.
*  *  *  *  *
### On Windows 10
Although the complete installation documentation is available on the [SAT Getting Started page](https://docs.substance3d.com/sat/pysbs-python-api/getting-started), I've detailed the important steps below. 

#### 1) Installation
##### a) Installing Python (if it is not installed already)
As mentioned in the Substance by Adobe documentation, the Pysbs API is compatible with Python 2.7 and Python 3.5. These samples use Python 2.7, which for Windows 10 can be downloaded from [here](https://www.python.org/downloads/release/python-2718). 

##### b) Installing Pip (if it is not installed already)
Pip can be obtained using [these instructions](https://pip.pypa.io/en/stable/installing/).

##### c) Installing Pysbs (the Substance Designer Scripting API package)
First, you must obtain the "Pysbs" archive. This archieve is either under the Licence tab on your account on the [Substance Account website](https://store.substance3d.com/user) or in your default Substance install location under the "Pyton Api" directory in the Substance Automation Toolkit directory. 

After you have the .zip archive, you'll need to use the Command Line to install the API. As exemplified in the Substance documentation, use the following command:
```
pip install Pysbs-x.y.z.zip --find-links <apiDir>
```
Below is a better example of what the install command looks like for the default installation of the 2018.2.0 version.
```
pip install "C:\Program Files\Allegorithmic\Substance Automation Toolkit\Python API\Pysbs-2018.2.0.zip"
```

#### 2) Usage
##### a) Setting up
First, the user should customize two files: **user_settings.json** and **config_bentnormal.json**.
###### I) Open  **user_settings.json** in a text editor.
###### II) Edit any of the entries as desired (they are all self explanatory).
```
{
  "substance_automation_toolkit_path": "C:\\Program Files\\Allegorithmic\\Substance Automation Toolkit",
  "output_path": "C:\\substance_test\\output_folder\\",
  "lows_path": "C:\\substance_test\\lows",
  "highs_path": "C:\\substance_test\\highs",
  "input_format": "fbx",
  "output_format": "tga",
  "low_poly_nameflag": "_low",
  "high_poly_nameflag": "_high"
}
``` 
###### III) Open  **config_bentnormal.json** in a text editor.
###### IV) Edit any of the entries as desired, for best baking results.
```
{
  "output_name_flag": "_BentNormal",
  "output_size": 12,
  "antialiasing": 0,
  "ignore_backface": true,
  "self_occlusion": 0,
  "use_lowdef_as_highdef": false,
  "uv_set": 0
}
```
##### b) Running the batch file called **run_win10.bat** by double clicking on it.
The code will go the following operations, in order:
- check if the output path exists and if it doesn't, create the directories
- read the low poly folder and assemble a list of the files that are meshes of the provided type
- read the high poly folder and for each found low poly mesh, determine what the high poly mesh name should be
- if there is a high poly mesh that matches the name conditions of the low poly, create a dictionary of matches (for example: "mesh_low" matches "mesh_high", but "mesh" matches "mesh" if the names are identical as well)
- for each match, go through each provided bake type and execute the bake with the defined parameters
*  *  *  *  *
### On Mac OS X Catalina
Examples currently unavailable, but can be kickstarted using the Windows 10 examples and the Substance Automation Toolkit documentation.
*  *  *  *  *
## Extensibility
The code in the provided sample use a modular design so new bake types can be added to the batch process.
To add a new bake type:
- define a new "config_<bake_name>.json" and create class to handle it in **config_bakes.py**
- add the bake rules to the **entry.py**
*  *  *  *  *
## Useful Resources
- [Substance Automation Toolkit Home](https://docs.substance3d.com/sat)
- [Substance Automation Toolkit Setup and Getting Started](https://docs.substance3d.com/sat/setup-and-getting-started)
