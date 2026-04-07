@echo off
title Git-Repository Bereinigung

echo ============================================================
echo   Git-Repository Bereinigung nach neuer .gitignore
echo ============================================================
echo.
echo Dieses Skript entfernt alle aktuell getrackten Dateien aus
echo dem Git-Index, ohne sie lokal zu löschen.
echo Anschließend werden nur die Dateien wieder hinzugefügt,
echo die NICHT in der .gitignore stehen.
echo.
echo Dies ist notwendig, wenn Dateien wie *.zip, *.log, *.ged
echo oder Build-Ordner weiterhin im Commit erscheinen, obwohl
echo sie in der .gitignore ausgeschlossen wurden.
echo.
echo ------------------------------------------------------------
echo   ACHTUNG:
echo   Die Dateien werden NICHT gelöscht, nur ent-tracked!
echo ------------------------------------------------------------
echo.

set /p confirm="Möchten Sie die Bereinigung jetzt durchführen? (j/n): "

if /I "%confirm%" NEQ "j" (
    echo.
    echo Vorgang abgebrochen.
    pause
    exit /b
)

echo.
echo Entferne alle Dateien aus dem Git-Index...
git rm -r --cached .

echo.
echo Füge Dateien gemäß .gitignore erneut hinzu...
git add .

echo.
echo Erstelle Commit...
git commit -m "automatische Bereinigung des Repositories nach neuer .gitignore"

echo.
echo ------------------------------------------------------------
echo   Bereinigung abgeschlossen!
echo   Das Repository ist jetzt konsistent mit der .gitignore.
echo ------------------------------------------------------------
echo.

pause