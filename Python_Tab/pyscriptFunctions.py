#region pyscriptFunctions

from pyscript import document
import asyncio

global sentInput
sentInput = False

def TerminalPrint(text, rgb = [255, 255, 255], end= "<br>"):
    document.querySelector("#outputDisplay").innerHTML += (f'<span style="color:rgb({rgb[0]}, {rgb[1]}, {rgb[2]})">{text}</span>{end}')

def TerminalClear():
    document.querySelector("#outputDisplay").innerHTML = ""

def SendInput(other):
    global sentInput

    sentInput = True

async def TerminalInput(prompt = "", rgb = [255, 255, 255]): 
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    global sentInput

    sentInput = False

    TerminalPrint(prompt, rgb, end= "")

    while sentInput == False:
        await asyncio.sleep(1)

    sentInput = False

    TerminalPrint(document.querySelector("#inputString").value)

    inputBoxValue = document.querySelector("#inputString").value
    document.querySelector("#inputString").value = ""

    return inputBoxValue

async def TerminalSleep(duration):
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    await asyncio.sleep(duration)


#endregion

