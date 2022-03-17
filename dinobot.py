import cv2
import numpy as np
import pyautogui

while True:
    img = pyautogui.screenshot(region = (150, 500, 255, 250))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    black_pixel_count = np.sum(img < 100)
    white_pixel_count = np.sum(img > 100)

    print('Number of white pixels:', white_pixel_count)
    print('Number of black pixels:', black_pixel_count)

    #light mode -> black pixel count should be 4000 to 30000
    if black_pixel_count > 4000 and black_pixel_count < 30000:
        pyautogui.press('up')

    #dark mode ->  white the same
    if white_pixel_count > 4000 and white_pixel_count < 30000:
        pyautogui.press('up')

    cv2.imshow('img', img)
    if cv2.waitKey(25) & ord('q') == False:
        cv2.destroyAllWindows()
        break
