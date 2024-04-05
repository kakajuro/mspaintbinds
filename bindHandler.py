import pyautogui as pg
import pyscreeze

def changeColour(col:str):
  startPos = pg.position()

  try:
    button = pyscreeze.locateCenterOnScreen(f'imgs/{col}.png')
    
    if button:
      pg.moveTo(button)
      pg.leftClick()
      pg.moveTo(startPos.x, startPos.y)
      print(f"Changed colour to: {col.capitalize()}")
    else:
      print(f"{col.capitalize()} not located.")
  except Exception as e:
    print(f"An error occurred: {e}")
  
def changeTool(tool:str):
  startPos = pg.position()
  button = pyscreeze.locateCenterOnScreen(f'imgs/{tool}.png')
  
  if button:
    pg.moveTo(button)
    pg.leftClick()
    pg.moveTo(startPos.x, startPos.y)
    print(f"Changed tool to: {tool.capitalize()}")
  else:
    print(f"{tool.capitalize()} not located.")
  
def handleBinds(incoming):
  match incoming:
    case "q":
      print("Quitting program...")
      return False
    case "1":
      changeColour("black")
    case "2":
      changeColour("grey")
    case "3":
      changeColour("brown")
    case "4":
      changeColour("red")
    case "5":
      changeColour("orange")
    case "6":
      changeColour("yellow")
    case "7":
      changeColour("green")
    case "8":
      changeColour("lightblue")
    case "9":
      changeColour("blue")
    case "0":
      changeColour("purple")
    case "-":
      changeColour("white")
    case "[":
      changeTool("brush")
    case "]":
      changeTool("select")
    case "s":
      changeTool("select")
    case "t":
      changeTool("text")
    case "f":
      changeTool("fill")
    case "b":
      changeTool("brush")
    case _:
      pass
    
