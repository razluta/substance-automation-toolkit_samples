# **Substance Automation Toolkit - Samples**
This repository contains a few samples for using the [Substance Automation Toolkit](https://docs.substance3d.com/sat) and providing a framework of examples for introducing automation in a content development pipeline. 

The provided examples are split into two categories: 
- using the [Command Line Tools](https://docs.substance3d.com/sat/command-line-tools)
- using the [Python API](https://docs.substance3d.com/sat/pysbs-python-api).


_Note: This repository demonstrates **only** the following concepts: (code can be easily modified to achieve most other available options)_
- _Headless Normal Map texture baking from a list of [low_poly, high poly] pairs, with outputting the results in a predefined location_
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
## Command Line Tools
### On Windows 10
_(Create all output folders before running the .bat file)_
To use the ...

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
##### a) Setting up the sources
##### b) Running the batch file
*  *  *  *  *
### On Mac OS X Catalina
Examples currently unavailable, but can be kickstarted using the Windows 10 examples and the Substance Automation Toolkit documentation.
*  *  *  *  *
## Useful Resources
- [Substance Automation Toolkit Home](https://docs.substance3d.com/sat)
- [Substance Automation Toolkit Setup and Getting Started](https://docs.substance3d.com/sat/setup-and-getting-started)
