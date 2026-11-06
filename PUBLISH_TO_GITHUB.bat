@echo off
setlocal
cd /d "%~dp0"
set "REMOTE=https://github.com/Mr2007Virk/Philosophy-0r-so-related-public.git"
where git >nul 2>nul
if errorlevel 1 (echo Install Git for Windows first.& pause& exit /b 1)
if not exist .git (
  git init
  git branch -M main
  git add .
  git commit -m "Initial public portfolio showcase"
)
git remote get-url origin >nul 2>nul
if errorlevel 1 (git remote add origin "%REMOTE%") else (git remote set-url origin "%REMOTE%")
echo Pushing to %REMOTE%
git push -u origin main
if errorlevel 1 (echo Push failed. Create the empty public GitHub repository first and sign in.& pause& exit /b 1)
echo Push complete. Enable GitHub Pages in Settings - Pages - Deploy from main / root.
pause
