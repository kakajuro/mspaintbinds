from pynput.keyboard import Listener
from threading import Event
from infi.systray import SysTrayIcon
from bindHandler import handleBinds
from win32gui import GetForegroundWindow, GetWindowText
import webbrowser as web

paintFocused = False
listening = True
listener = Listener(on_press=lambda event: on_press(event))
listener.start()

quit_event = Event()

print("MSPaint keybinds running...")

def openRepo(systray):
    web.open("https://github.com/kakajuro/mspaintbinds")

def qcallback(systray):
    global listening
    quit_event.set()
    listening = False
    
def on_press(key): 
    global listening
    if 'char' in dir(key) and paintFocused:
        res = handleBinds(key.char)
        
        if res == False:
          listening = False

menu_options = (("Source Code Repository", None, openRepo, ),)
systray = SysTrayIcon("imgs/paintlogo.ico", "MSPaint Binds", menu_options, on_quit=qcallback)

with systray:
    
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
print("Closing program...")