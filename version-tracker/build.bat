@echo off
echo ========================================
echo   Version Tracker - Build Script
echo ========================================
echo.

REM Prüfen ob Python installiert ist
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python nicht gefunden!
    echo Bitte Python 3.10+ installieren: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/3] Installiere Abhängigkeiten...
pip install -r requirements.txt

echo.
echo [2/3] Erstelle .exe Datei...
pyinstaller --onefile --windowed --name "VersionTracker" --icon=icon.ico version_tracker.py 2>nul || pyinstaller --onefile --windowed --name "VersionTracker" version_tracker.py

echo.
echo [3/3] Aufräumen...
rmdir /s /q build 2>nul
del /q VersionTracker.spec 2>nul

echo.
echo ========================================
echo   FERTIG!
echo ========================================
echo.
echo Die .exe Datei findest du im "dist" Ordner.
echo.
pause
