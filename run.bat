@echo off
setlocal

REM Check if Python is installed
where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed. Installing Python...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe' -OutFile 'python-installer.exe'"
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
)

REM Check if pip is available
where pip >nul 2>nul
if errorlevel 1 (
    echo Pip is not installed. Installing pip...
    powershell -Command "Invoke-WebRequest -Uri 'https://bootstrap.pypa.io/get-pip.py' -OutFile 'get-pip.py'"
    python get-pip.py
    del get-pip.py
)

REM Check if google.generativeai is installed
python -c "import google.generativeai" >nul 2>nul
if errorlevel 1 (
    echo google.generativeai is not installed. Installing google.generativeai...
    pip install google-generativeai
)

REM git clone https://github.com/Thepathakarpit/Windows_Automator/
REM cd Windows_Automator

REM Run main.py
echo Running main.py...
python main.py

endlocal
