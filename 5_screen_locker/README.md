###### Requirement

* fbs 0.8.4
* pyinstaller 3.4  pyinstaller-hooks
* python 3.6.7
* pyqt 5.9.2
* PyHook3
* win32gui
* ctypes
* platform

---

###### Purpose

_This program is consist of two parts_

* screen locker `main class`
  * `window object` which takes away the control of your system
  * disable `taskmgr`, `alt+F4`, `win+esc`, `winkey`, etc...
  * the `exit` let user input correct **passwd** in order to get rid off the freezing point
* screen locker `watcher`
  * watching user status
  * if user enters `AFK` more than 30 mins or some, the `locker` program will be triggered
* `SMS` for another `validation`
  * Ali Cloud service for `SMS` validation
  * To-Do...

---

###### Note

* QDialog focus can only be set right after the window is displayed

* `pyinstaller-hooks` must be installed for **non-pyqt program**

* user restriction such as `ctrl+alt-del` can be done by disabling `taskmgr` 

  ```windows batch
  @echo off 
  
  echo Get Administrator permission
  :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  cacls.exe "%SystemDrive%\System Volume Information" >nul 2>nul
  if %errorlevel%==0 goto Admin
  if exist "%temp%\getadmin.vbs" del /f /q "%temp%\getadmin.vbs"
  echo Set RequestUAC = CreateObject^("Shell.Application"^)>"%temp%\getadmin.vbs"
  @echo off
  
  echo RequestUAC.ShellExecute "%~s0","","","runas",1 >>"%temp%\getadmin.vbs"
  echo WScript.Quit >>"%temp%\getadmin.vbs"
  "%temp%\getadmin.vbs" /f
  if exist "%temp%\getadmin.vbs" del /f /q "%temp%\getadmin.vbs"
  exit
   
  :Admin
  echo Get Administrator permission
  ::::::::::::::::::::::修改注册表，关闭UAC::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "ConsentPromptBehaviorAdmin" /t reg_dword /d 0 /F
  reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "EnableLUA" /t reg_dword /d 0 /F
  reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "PromptOnSecureDesktop" /t reg_dword /d 0 /F
  
  reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\system" /v "DisableTaskMgr" /t reg_dword /d 1 /f >nul 
  reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoLogoff" /t reg_dword /d 1 /f >nul 
  reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\system" /v "DisableLockWorkstation" /t reg_dword /d 1 /f >nul 
  reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\system" /v "DisableChangePassword" /t reg_dword /d 1 /f >nul 
  reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "HideFastUserSwitching" /t reg_dword /d 1 /f >nul 
  ```

  

* `qt window flag` such as **Qt.WindowStaysOnTopHint and Qt.FramelessWindowHint** will take effect only when they are written in `one line`

* `ctypes` calls windows `dlls` in order to keep watching user idle time

* _TO-DO_   

  * `second validation` 
  * `watermark`