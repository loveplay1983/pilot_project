from pyHook import GetKeyState, HookConstants, HookManager
import pythoncom


# def on_mouse_event(event):
#     if (event.MessageName != 'mouse move'):
#         print(event.MessageName)
#     return True

def on_keyboard_event(event):
    # print(event.Key)

    # print(GetKeyState(HookConstants.VKeyToID('VK_MENU')))
    # print(HookConstants.VKeyToID('VK_MENU'))
    # event.KeyID == HookConstants.VKeyToID('VK_ESCAPE'):
    if GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and GetKeyState(HookConstants.VKeyToID('VK_MENU')) and \
            event.KeyID == HookConstants.VKeyToID('VK_DELETE'):
        print('ctrl alt del')
    return True

def main():
    hm = HookManager()
    hm.KeyDown = on_keyboard_event
    hm.HookKeyboard()

    pythoncom.PumpMessages()


if __name__ == '__main__':
    main()
