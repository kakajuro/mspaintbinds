# Useful link
# https://stackoverflow.com/questions/65311471/returning-an-argument-on-key-press-detection-using-pynput

from pynput.keyboard import Listener
from bindHandler import handleBinds
from win32gui import GetForegroundWindow, GetWindowText

paintFocused = False
listening = True
listener = Listener(on_press=lambda event: on_press(event))
listener.start()

print("MSPaint keybinds running...")

def on_press(key): 
    global listening
    if 'char' in dir(key) and paintFocused:
        res = handleBinds(key.char)
        
        if res == False:
          listening = False

while listening:
    
    try:
      windowTitle = GetWindowText(GetForegroundWindow())
      choppedWindowTitle = windowTitle.strip().split("-")[::-1]

      if choppedWindowTitle[0].strip().lower() == "paint":
        paintFocused = True
      else:
        paintFocused = False
        
    except Exception as e:
      print("Something went wrong.")
    
listener.stop()