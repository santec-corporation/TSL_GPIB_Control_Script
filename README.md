<p align="right"> <a href="https://www.santec.com/jp/" target="_blank" rel="noreferrer"> <img src="https://www.santec.com/dcms_media/image/common_logo01.png" alt="santec" 
  width="250" height="45"/> </a> </p>

> [!NOTE]
> If you have any [Issues](https://github.com/santec-corporation/TSL_USB_Control_Scripts/issues) related to the code, click [Create New](https://github.com/santec-corporation/TSL_USB_Control_Scripts/issues/new) to create a new issue. 


<h1>TSL GPIB Control Script</h1>

![GitHub top language](https://img.shields.io/github/languages/top/santec-corporation/TSL_USB_Control_Scripts?color=blue)

A GUI Interface to command and manage Santec TSL Device(s) connected via GPIB. <br>
For all TSL Models. Read below for more information.


<h2>Introduction</h2>

The Santec TSL Devices connected via GPIB can be controlled using Python GUI script.

<h2>Requirements</h2>

  - [Python](https://www.python.org/) - any version ( Latest Version advisable ), <br>
    install the latest version [Python Latest](https://www.python.org/downloads/), <br>
    to upgrade existing one ``` pip install --upgrade python ```

  - [PyVISA](https://pyvisa.readthedocs.io/en/latest/) - is a package used to control all kinds of measurement devices.
    Any version ( Latest Version advisable ) <br>
    to install, use ``` pip install pyvisa ``` or ``` pip3 install pyvisa ``` <br>
    to upgrade existing one ``` pip install --upgrade pyvisa ``` <br>
    to install PyVISA backend, ``` pip install pyvisa-py ``` or ``` pip3 install pyvisa-py ```

  - [PyQt5](https://pypi.org/project/PyQt5/) - PyQt5 is a set of Python bindings for the Qt application framework, allowing developers to create cross-platform graphical user interfaces (GUIs) with Qt using Python.
    Any version ( Latest Version advisable ) <br>
    to install, use ``` pip install PyQt5 ``` or ``` pip3 install PyQt5 ``` <br>
    to upgrade existing one ``` pip install --upgrade PyQt5 ```


<h2>Main Scripts</h2>
1) [functions.py] - Script that interacts with the TSL device with the help of the PyVISA library.

2) [TSL_Control_Tool_GUI.py] - GUI Script written in Python with the use of PyQt5 library serves as the frontend of the project.

3) [main.py] - The main script that makes use of the functions.py and TSL_Control_Tool_GUI.py to control the TSL device with a Graphical User Interface (GUI).
 
4) TSL_GPIB_Control_Software.exe - Is an executable of the entire project. This file can be found in the [Releases](https://github.com/santec-corporation/TSL_GPIB_Control_Script/releases).


<br>
<details>
<summary><h2>About Santec Swept Test System</h2></summary>

### What is STS IL PDL?
  The Swept Test System is the photonic solution by Santec Corp. to perform Wavelength 
  Dependent Loss characterization of passive optical devices.
  It consists of:
  - A light source: Santec’s Tunable Semiconductor Laser (TSL);
  - A power meter: Santec’s Multi-port Power Meter (MPM);
   

### For more information on the Swept Test System [CLICK HERE](https://inst.santec.com/products/componenttesting/sts)
</details>


[//]: # (Below are the links to the Python scripts)
[main.py]: <https://github.com/santec-corporation/TSL_GPIB_Control_Script/blob/main/main.py>
[TSL_Control_Tool_GUI.py]: <https://github.com/santec-corporation/TSL_GPIB_Control_Script/blob/main/TSL_Control_Tool_GUI.py>
[functions.py]: <https://github.com/santec-corporation/TSL_GPIB_Control_Script/blob/main/functions.py>
