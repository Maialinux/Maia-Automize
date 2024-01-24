import pyautogui

# Pega o tamanho da tela
screenWidth, screenHeight = pyautogui.size()
#print(f"Resolução {screenWidth} x {screenHeight}")
# Pega a posição x e y do mouse na tela
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX,currentMouseY)
#pyautogui.sleep(45)
pyautogui.PAUSE = 1
#pyautogui.alert("Não mexa em nada, seu computador está no processo automático")

 # EMAIL GMAIL https://www.google.com/intl/pt-BR/gmail/about/
if screenWidth == 1680 and screenHeight == 1050:
    pyautogui.sleep(2)  # tempo de espera
    pyautogui.click(283, 63)  # posiciona o mouse e clica 
    pyautogui.hotkey("ctrlleft","t")  # combinação de teclas
    pyautogui.sleep(1)
    pyautogui.write("https://www.google.com/intl/pt-BR/gmail/about/")  # escreve algo
    pyautogui.sleep(2)
    pyautogui.press("enter")  # usa a tecla enter 
    pyautogui.sleep(5)
    pyautogui.click(1310,107)
    pyautogui.sleep(3)
    pyautogui.click(751,505)
    pyautogui.sleep(3)
    pyautogui.write("email")
    pyautogui.sleep(3)
    pyautogui.press("enter")
    pyautogui.sleep(5)
    pyautogui.click(760,557)
    pyautogui.sleep(3)
    pyautogui.write("senha")
    pyautogui.sleep(3)
    pyautogui.press("enter")
    pyautogui.sleep(3)
   