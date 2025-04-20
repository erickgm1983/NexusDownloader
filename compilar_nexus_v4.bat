
@echo off
title Compilar Nexus Downloader v4
color 0B

echo ==========================================
echo      COMPILADOR NEXUS DOWNLOADER v4
echo ==========================================
echo.

where pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller no está instalado.
    echo Ejecuta: pip install pyinstaller
    pause
    exit /b
)

pyinstaller nexus_gui_descargador_v4.spec

echo.
echo ✅ Empaquetado completado.
echo Busca el .exe en: dist\NexusDownloader_v4\
pause
