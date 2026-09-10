@echo off
REM ============================================================
REM newproject.bat
REM Creates a new uv project folder inside UV-PROJ, strips the
REM embedded .git folder that "uv init" creates, then commits
REM and pushes it to GitHub.
REM
REM Usage:
REM   newproject.bat my-new-folder-name
REM ============================================================

if "%~1"=="" (
    echo Usage: newproject.bat ^<folder-name^>
    exit /b 1
)

set REPO_DIR=C:\Users\faran\Projects\Farana_AgenticAI\UV-PROJ
set FOLDER_NAME=%~1

cd /d "%REPO_DIR%"

echo.
echo === Creating new project: %FOLDER_NAME% ===
uv init "%FOLDER_NAME%"

if not exist "%FOLDER_NAME%" (
    echo ERROR: uv init did not create the folder. Aborting.
    exit /b 1
)

REM Remove embedded git repo that "uv init" creates, so it
REM merges cleanly into the parent repo instead of breaking
REM "git add" with an "embedded repository" error.
if exist "%FOLDER_NAME%\.git" (
    echo Removing embedded .git folder...
    rmdir /s /q "%FOLDER_NAME%\.git"
)

echo.
echo === Staging, committing, and pushing ===
git add "%FOLDER_NAME%"
git commit -m "Add %FOLDER_NAME%"
git push

echo.
echo === Done. "%FOLDER_NAME%" has been pushed to GitHub. ===
