# Automating stuff
import pyautogui

x = 1887
c = 0


def check():
    pyautogui.click(x=2767, y=1028)


while True:
    if pyautogui.locateOnScreen('0.png') is not None:
        check()
        c += 1
        print(c)
    elif pyautogui.locateOnScreen('1.png') is not None:
        location = pyautogui.locateCenterOnScreen('1.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('2.png') is not None:
        location = pyautogui.locateCenterOnScreen('2.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('3.png') is not None:
        location = pyautogui.locateCenterOnScreen('3.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('4.png') is not None:
        location = pyautogui.locateCenterOnScreen('4.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('5.png') is not None:
        location = pyautogui.locateCenterOnScreen('5.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('6.png') is not None:
        location = pyautogui.locateCenterOnScreen('6.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('7.png') is not None:
        location = pyautogui.locateCenterOnScreen('7.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('8.png') is not None:
        location = pyautogui.locateCenterOnScreen('8.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('9.png') is not None:
        location = pyautogui.locateCenterOnScreen('9.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('10.png') is not None:
        location = pyautogui.locateCenterOnScreen('10.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('11.png') is not None:
        location = pyautogui.locateCenterOnScreen('11.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('12.png') is not None:
        location = pyautogui.locateCenterOnScreen('12.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    elif pyautogui.locateOnScreen('13.png') is not None:
        location = pyautogui.locateCenterOnScreen('13.0.png')
        pyautogui.click(x, location.y)
        check()
        check()
    else:
        pyautogui.click(2591, 407)
