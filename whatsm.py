import pyautogui
import time

print pyautogui.position()

pyautogui.doubleClick(156,187)
time.sleep(3)

pyautogui.typewrite('Askim')
time.sleep(3)



pyautogui.click(156,240)
pyautogui.typewrite('30 nolu masa 252,00 TL')
pyautogui.typewrite('\n')