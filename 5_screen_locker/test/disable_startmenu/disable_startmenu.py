from win32gui import FindWindow, ShowWindow

start_menu = FindWindow('Windows.UI.Core.CoreWindow',None)
task_mgr = FindWindow('Shell_TrayWnd', None)

ShowWindow(start_menu, 1)
ShowWindow(task_mgr, 1)