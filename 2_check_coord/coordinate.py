import pyautogui as auto

print('按 CTRL-C 退出')

try:
    while True:
        x, y  = auto.position()
        current_location = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(current_location, end='')
        print('\b' * len(current_location), end='', flush=True)
except KeyboardInterrupt:
    print('\n')