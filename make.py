import os
import filecmp
import shutil
import time



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
















####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

# CXX             --> The compiler used
# FLAGS           --> The Flags used during compilation
# VERSION         --> The cpp version used
# EXECUTABLE_NAME --> The final executable will have this name
# OBJ_OUTPUT      --> Where The .o files will be created
# OUTPUT          --> Where the final project will be created(executable + ressources + close files(.dll, .a, etc...))
# SRC_DIR         --> Where your Project's cpp files are located(it will also look in subdirectories)
# INCLUDES        --> The Include folders
# LIB             --> The Library folders
# DEPENDENCIES    --> The name of the dependencies
# RESSOURCE_DIR   --> Where you ressource folder is(can contain images, fonts, etc...)
# EXE_CLOSE_FILES --> The files that have to be in the same dir as the executable like .dll files or others
# APP_TYPE        --> Define if you want to build a dll file or an exe file.


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


OBJ_OUTPUT = "Build"
PROJ_OUTPUT = "bin"
FILES = []
compiled = 0

def compile():
    global compiled
    current = 1
    total = len(FILES)
    command = 0
    for file in FILES:
        nameLen = len(file[1])
        len_bfr_fract = 30
        spacesCount = len_bfr_fract - nameLen
        spaces = ''
        while(spacesCount > 0):
            spaces += ' '
            spacesCount -= 1

        print(f"{HEADER}compiling...  {ENDC}{OKBLUE}{file[1]}{ENDC}{spaces}{WARNING}{current}/{total}{ENDC}")
        if os.path.exists(f"./{BUILD_OUTPUT}/{OBJ_OUTPUT}/obj/{file[1]}.o"):
            if os.path.exists(f"./{BUILD_OUTPUT}/{OBJ_OUTPUT}/ref/{file[1]}.cpp"):
                if filecmp.cmp(f"./{BUILD_OUTPUT}/{OBJ_OUTPUT}/ref/{file[1]}.cpp" , file[0]) == False:
                    command = os.system(f'cmd /c "{CXX} {FLAGS} {MACROS} -g --std={VERSION} {INCLUDES} -c {file[0]} -o ./{BUILD_OUTPUT}/{OBJ_OUTPUT}/obj/{file[1]}.o"')
                    if command == 0:
                        compiled +=  1
                    else:
                        break
            else:
                command = os.system(f'cmd /c "{CXX} {FLAGS} {MACROS} -g --std={VERSION} {INCLUDES} -c {file[0]} -o ./{BUILD_OUTPUT}/{OBJ_OUTPUT}/obj/{file[1]}.o"')
                if command == 0:
                    compiled +=  1
                else:
                    break
        else:
            command = os.system(f'cmd /c "{CXX} {FLAGS} {MACROS} -g --std={VERSION} {INCLUDES} -c {file[0]} -o ./{BUILD_OUTPUT}/{OBJ_OUTPUT}/obj/{file[1]}.o"')
            if command == 0:
                compiled +=  1
            else:
                break
        current += 1

    print(f"Compiled {compiled} files")
    if command == 0:
        if APP_TYPE == "exe":
            link()
        elif APP_TYPE == "dll":
            linkDLL()
        else:
            print(f"{FAIL}[FAILED] Cannot Link {APP_TYPE} app type!!{ENDC}")
    else:
        print(f"{FAIL}[FAILED] Compilation {ENDC}")

def link():
    print(f"{HEADER}linking...{ENDC}")
    if(os.path.exists(".\\" + BUILD_OUTPUT+ "\\" + PROJ_OUTPUT)):
        shutil.rmtree(".\\" + BUILD_OUTPUT + "\\" + PROJ_OUTPUT)     
    os.system(f'cmd /c "mkdir .\\{BUILD_OUTPUT}\\{PROJ_OUTPUT}"')   
    command = os.system(f'cmd /c "{CXX} {FLAGS} -g --std={VERSION} {BUILD_OUTPUT}/{OBJ_OUTPUT}/obj/*.o -o {BUILD_OUTPUT}/{PROJ_OUTPUT}/{EXECUTABLE_NAME} {LIB} {DEPENDENCIES}')
    if command == 0:
        print(f"{OKGREEN}Successfully Created {ENDC}{BOLD}{EXECUTABLE_NAME}.exe{ENDC}")
        copy()
        # run()
    else:
        print(f"{FAIL}[FAILED] Linking {ENDC}")


def linkDLL():
    print(f"{HEADER}linking dll...{ENDC}")
    if(os.path.exists(".\\" + BUILD_OUTPUT+ "\\" + PROJ_OUTPUT)):
        shutil.rmtree(".\\" + BUILD_OUTPUT + "\\" + PROJ_OUTPUT)     
    os.system(f'cmd /c "mkdir .\\{BUILD_OUTPUT}\\{PROJ_OUTPUT}"')   
    command = os.system(f'cmd /c "{CXX} {FLAGS} -g --std={VERSION} -shared -o {BUILD_OUTPUT}/{PROJ_OUTPUT}/{EXECUTABLE_NAME}.dll  {BUILD_OUTPUT}/{OBJ_OUTPUT}/obj/*.o -Wl,--out-implib,{BUILD_OUTPUT}/{PROJ_OUTPUT}/lib{EXECUTABLE_NAME}_lib.a  {LIB} {DEPENDENCIES} ')
    if command == 0:
        print(f"{OKGREEN}Successfully Created {ENDC}{BOLD}{EXECUTABLE_NAME}.dll{ENDC}")
        copy()
    else:
        print(f"{FAIL}[FAILED] Linking DLL{ENDC}")

def run():
    print(f"{HEADER}running... {ENDC}{BOLD}{EXECUTABLE_NAME}{ENDC}")
    os.system(f'cmd /c "cd {BUILD_OUTPUT}\\{PROJ_OUTPUT} &&  start {EXECUTABLE_NAME}.exe"')




def copy():
    dir = os.listdir(f"{BUILD_OUTPUT}/{OBJ_OUTPUT}/ref")
    if len(dir) > 0:
        os.system(f'cmd /c "del .\\{BUILD_OUTPUT}\\{OBJ_OUTPUT}\\ref\\*.cpp"')
    for file in FILES:
        f = open(f"{BUILD_OUTPUT}/{OBJ_OUTPUT}/ref/{file[1]}.cpp", "w")
        shutil.copyfile(file[0], f"{BUILD_OUTPUT}/{OBJ_OUTPUT}/ref/{file[1]}.cpp")
    
    if os.path.exists(RESSOURCE_DIR):
        name = RESSOURCE_DIR.split("/")[-1]
        shutil.copytree(f"./{RESSOURCE_DIR}/", f"./{BUILD_OUTPUT}/{PROJ_OUTPUT}/{name}/")

    if os.path.exists(EXE_CLOSE_FILES):
        for file in os.listdir(EXE_CLOSE_FILES):
            f = open(BUILD_OUTPUT + "/" + PROJ_OUTPUT + "/" + file, "w")
            shutil.copyfile(EXE_CLOSE_FILES + "/" + file, f"{BUILD_OUTPUT}/{PROJ_OUTPUT}/{file}")


def main():
    print(os.getcwd())
    start = time.time()

    if os.path.exists(f'{BUILD_OUTPUT}') == False:
        os.system(f'cmd /c "mkdir {BUILD_OUTPUT}"')

    if os.path.exists(f"{BUILD_OUTPUT}/{OBJ_OUTPUT}") == False:
        os.system(f'cmd /c "mkdir .\\{BUILD_OUTPUT}\\{OBJ_OUTPUT}"')

    if os.path.exists(f'{BUILD_OUTPUT}/{OBJ_OUTPUT}/obj') == False:
        os.system(f'cmd /c "mkdir .\\{BUILD_OUTPUT}\\{OBJ_OUTPUT}\\obj"')

    if os.path.exists(f'{BUILD_OUTPUT}/{OBJ_OUTPUT}/ref') == False:
        os.system(f'cmd /c "mkdir .\\{BUILD_OUTPUT}\\{OBJ_OUTPUT}\\ref"')

    for root, dirs, files in os.walk(SRC_DIR):
        for filename in files:
            if ".cpp" in filename:
                root = root.replace("\\", "/")
                FILES.append([os.path.join(root, filename).replace("\\", "/"), filename.split(".cpp")[0]])


    compile()

    end = time.time()

    duration = round(end - start, 4)

    print(f"{WARNING}[TIME] Ended in: {ENDC}{OKCYAN}{duration} seconds{ENDC}")


if "__main__" == __name__:
    main()


