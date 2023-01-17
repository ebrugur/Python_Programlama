import pyautogui

# Ekran Çözünürlüğü
screenWidth, screenHeight = pyautogui.size()
print("Ekran Çözünürlüğü :", screenWidth, screenHeight)

# Fare Pozisyonu
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)