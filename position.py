import pyautogui
import time

print pyautogui.position()

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print positionStr
        print '\b' * len(positionStr)
        time.sleep(1)
        # TODO: Get and print the mouse coordinates.
except KeyboardInterrupt:
    print('\nDone.')
