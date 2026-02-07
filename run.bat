@echo off
echo ====================================
echo PropModCreator Launcher
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from python.org
    echo.
    pause
    exit /b 1
)

REM Check if requirements are installed
pip show customtkinter >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo.
)

REM Run the application
echo Starting PropModCreator...
echo.
python prop_mod_creator.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Application failed to start
    echo Check the error messages above
    pause
)
