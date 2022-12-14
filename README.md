# Cpp-compiler
Cpp compiler made in python.


# To use it Run "python make.py"

Make sure to fill these variables before. Only CXX(compiler like g++, clang++, etc...), VERSION and SRC_DIR are mandatory to fill

``` python
CXX ="g++"
FLAGS = "-Wall"
VERSION="c++20"
EXECUTABLE_NAME = "Application"
SRC_DIR = ''
BUILD_OUTPUT = 'out'

INCLUDES = ""
LIB = ""
DEPENDENCIES =  ""

RESSOURCE_DIR = ""
EXE_CLOSE_FILES = ""

APP_TYPE = "exe"
MACROS = ""


# CXX             --> The compiler used
# FLAGS           --> The Flags used during compilation
# VERSION         --> The cpp version used
# EXECUTABLE_NAME --> The final executable will have this name
# OBJ_OUTPUT      --> Where The .o files will be created
# PROJ_OUTPUT     --> Where the final project will be created(executable + ressources + close files(.dll, .a, etc...))
# SRC_DIR         --> Where your Project's cpp files are located(it will also look in subdirectories)
# BUILD_OUTPUT    --> Where the build files and The Bin folder will be created
# INCLUDES        --> The Include folders : -Iinclude_folder
# LIB             --> The Library folders : -Llib_folder
# DEPENDENCIES    --> The name of the dependencies : -ldependencie_name
# RESSOURCE_DIR   --> Where you ressource folder is(can contain images, fonts, etc...)
# EXE_CLOSE_FILES --> The files that have to be in the same dir as the executable like .dll files or others
# APP_TYPE        --> Define wheter the app should be built as a "dll" or "exe" file
# MACROS          --> Prepocessors that gets defined during compilation : use -Dmacros_name


```


# Tools

Python : 3.10.6                                                                                                                          
packages : os, filecmp, shutil                                                                       
mingw32 : https://sourceforge.net/projects/mingw/                                                                                              
Tested with mingw32 g++ only. clang++ was not tested yet so I cannot guarantee it's functionality. 


# Notice

When adding files path in your cpp code make sure to do it relative to the executable's location and not the cpp file's location. You can take it as if the foler in which all your code is location is the reference point;

For a project where you have one  MAIN.cpp file in a src folder and then a res folder

``` bash
Proj
|--src 
|     |---MAIN.cpp
| res 
|     |---image.png

```

  You would do this
  
 ``` cpp
  Whatever_function_you_have("./res/image.png");
 ```
 
  In any cases do not do this
  
 ``` cpp
    Whatever_function_you_have("../res/image.png");
 ```
