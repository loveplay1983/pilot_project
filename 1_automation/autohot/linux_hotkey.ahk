#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.



SetTitleMatchMode RegEx
Return


^!t::
IfWinExist ahk_class ConsoleWindowClas
{
    WinActivate
}
else
{
    RunAS, Administrator, pgjdcwn1983
	OpenCmdInCurrent()
}
Return


; Opens the command shell 'cmd' in the directory browsed in Explorer.
; Note: expecting to be run when the active window is Explorer.
;
OpenCmdInCurrent()
{
    ; This is required to get the full path of the file from the address bar
    WinGetText, full_path, A
 
    ; Split on newline (`n)
    StringSplit, word_array, full_path, `n
    ; Take the first element from the array
    full_path = %word_array1%   
 
    ; strip to bare address
    full_path := RegExReplace(full_path, "^Address: ", "")
 
    ; Just in case - remove all carriage returns (`r)
    StringReplace, full_path, full_path, `r, , all
 
 
    IfInString full_path, /
    {
        Run,  cmd /K cd /D "%full_path%"
    }
    else
    {
        Run, cmd /K cd /D "C:/ "
    }
}



::clear::cls