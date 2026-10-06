@echo off
setlocal
chcp 65001 >nul
set "PYTHONIOENCODING=utf-8"
if exist "%~dp0.venv\Scripts\python.exe" (
    "%~dp0.venv\Scripts\python.exe" "%~dp0menu_bot.py" %*
    exit /b
)
call conda run --no-capture-output -n menu python "%~dp0menu_bot.py" %*
exit /b %errorlevel%
