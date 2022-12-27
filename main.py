import pyautogui

# Coordinate for clicking the checkboxes
x = 1887
c = 0


# Function for clicking the checkbox
def check():
    pyautogui.click(x=2767, y=1028)


# Main loop
while True:
    if pyautogui.locateOnScreen('0.png') is not None:   # Check if '0.png' is on the screen
        check()  # Click the checkbox
        c += 1   # Increment the counter
        print(c)    # Print the counter
    elif pyautogui.locateOnScreen('1.png') is not None:
        # Check if '1.png' is on the screen
        location = pyautogui.locateCenterOnScreen('1.0.png')
        # Find the center of '1.0.png' on the screen
        pyautogui.click(x, location.y)
        # Click the choice at the found location
        check()  # Click the checkbox
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
        print('failed')
