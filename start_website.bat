@echo off
echo Starting Nimrah Build Care Solutions website...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in your PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b
)

echo Python is installed. Starting web server...
echo.

REM Run the Python server script
python start_server.py

pause