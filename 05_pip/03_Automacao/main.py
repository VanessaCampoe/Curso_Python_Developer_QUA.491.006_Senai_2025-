import pyautogui as auto
import time


def main():
    auto.PAUSE = 1
    auto.press("win")  # Press the Windows key
    #  preciosar um tecla 
    auto.write("edge")  # Type "edge"
    auto.press("enter")  # Press the Enter key
    
    time.sleep(2)  # Wait for Notepad to open
    auto.hotkey("alt","space")  # Paste clipboard content
      # Wait for the paste action
    auto.press("x")  # Type "Hello, World!"
    auto.write("github.com")
    auto.press("enter")
    auto.press("enter")
    

if __name__ == "__main__":
    main()