@echo off
echo ============================================
echo   GedTidy Build Script
echo ============================================

echo.
echo [0/5] Version aus src\gedtidy\version.py auslesen...

for /f "tokens=2 delims== " %%a in ('findstr APP_VERSION src\gedtidy\version.py') do set VERSION=%%a
set VERSION=%VERSION:"=%

echo Aktuelle Version: %VERSION%
echo Stelle sicher, dass du diese Version in src\gedtidy\version.py angepasst hast.
echo.

choice /m "Moechtest du den Build mit dieser Version fortsetzen"
if errorlevel 2 (
    echo Build abgebrochen.
    choice /m "Moechtest du die version.py jetzt anpassen"
    if errorlevel 1 (
        edit src\gedtidy\version.py
        exit /b 1
    )
    echo Bitte version.py anpassen und Build erneut starten.
    pause
    exit /b 0
)

echo.
echo [1/5] Alte Build-Ordner loeschen...
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul

echo.
echo [2/5] PyInstaller starten...
pyinstaller GedTidy.spec
if %errorlevel% neq 0 (
    echo FEHLER: PyInstaller ist fehlgeschlagen.
    pause
    exit /b 1
)

echo.
echo [3/5] Pruefe, ob EXE existiert...
if not exist dist\GedTidy.exe (
    echo FEHLER: dist\GedTidy.exe wurde nicht erzeugt.
    pause
    exit /b 1
)

echo.
echo [4/5] Erzeuge finale gedtidy.iss...
powershell -Command ^
    "(Get-Content gedtidy_template.iss) -replace '@@VERSION@@', '%VERSION%' | Set-Content gedtidy.iss"

echo Finale ISS-Datei erzeugt: gedtidy.iss

echo.
echo [5/5] Inno Setup Compiler starten...
"C:\Users\dieec\AppData\Local\Programs\Inno Setup 6\ISCC.exe" gedtidy.iss
if %errorlevel% neq 0 (
    echo FEHLER: Inno Setup ist fehlgeschlagen.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   Build erfolgreich abgeschlossen!
echo   Version: %VERSION%
echo   EXE: dist\GedTidy.exe
echo   Installer: installer\GedTidy_Setup_%VERSION%.exe
echo ============================================

pause