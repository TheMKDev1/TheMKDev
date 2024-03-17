#region pyscriptFunctions

from pyscript import document
import asyncio

global sentInput_XO
sentInput_XO = False

def TerminalPrint_XO(text, rgb = [255, 255, 255], end= "<br>"):
    document.querySelector("#outputDisplay_XO").innerHTML += (f'<span style="color:rgb({rgb[0]}, {rgb[1]}, {rgb[2]})">{text}</span>{end}')

def TerminalClear_XO():
    document.querySelector("#outputDisplay_XO").innerHTML = ""

def SendInput_XO(other):
    global sentInput_XO

    sentInput_XO = True

async def TerminalInput_XO(prompt = "", rgb = [255, 255, 255]): 
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    global sentInput_XO

    sentInput_XO = False

    TerminalPrint_XO(prompt, rgb, end= "")

    while sentInput_XO == False:
        await asyncio.sleep(1)

    sentInput_XO = False

    TerminalPrint_XO(document.querySelector("#inputString_XO").value)

    inputBoxValue = document.querySelector("#inputString_XO").value
    document.querySelector("#inputString_XO").value = ""

    return inputBoxValue

async def TerminalSleep_XO(duration):
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    await asyncio.sleep(duration)

#endregion



import operator

global board
global boardColors

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
boardColors = [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]

#possible win conditions
winList = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

XInput = 0
OInput = 0

boardBackgroundColor = [255, 255, 0] #yellow

p1Color = [0, 0, 255]
p2Color = [255, 0, 0]

errorColor = [160,32,240]


def DisplayBoard():

    TerminalPrint_XO("<br>")

    TerminalPrint_XO("  " + str(board[0]), rgb= boardColors[0], end=" "); TerminalPrint_XO("|", boardBackgroundColor, end=" "); TerminalPrint_XO(str(board[1]), rgb= boardColors[1], end=" "); TerminalPrint_XO("|", boardBackgroundColor, end=" "); TerminalPrint_XO(str(board[2]), rgb= boardColors[2])
    TerminalPrint_XO(" ―――", boardBackgroundColor)

    TerminalPrint_XO("  " + str(board[3]), rgb= boardColors[3],  end=" "); TerminalPrint_XO("|", boardBackgroundColor, end=" "); TerminalPrint_XO(str(board[4]), rgb= boardColors[4], end=" "); TerminalPrint_XO("|", boardBackgroundColor, end=" "); TerminalPrint_XO(str(board[5]), rgb= boardColors[5])
    
    TerminalPrint_XO(" ―――", boardBackgroundColor)
    TerminalPrint_XO("  " + str(board[6]), rgb= boardColors[6], end=" "); TerminalPrint_XO("|", boardBackgroundColor, end=" "); TerminalPrint_XO(str(board[7]), rgb= boardColors[7], end=" "); TerminalPrint_XO("|", boardBackgroundColor, end=" "); TerminalPrint_XO(str(board[8]),  rgb= boardColors[8])
    
    TerminalPrint_XO("<br>")

async def XPlays():

    TerminalPrint_XO("<br>")
    XInput = await TerminalInput_XO("Where Would You Like To Place Your X:  ", p1Color)

    try:
        XInput = int(XInput)

    except:
        TerminalClear_XO()

        DisplayBoard()

        TerminalPrint_XO("Your Answer ", errorColor, end=""); TerminalPrint_XO(str(XInput), p1Color, end=""); TerminalPrint_XO(" Is Not Valid", errorColor)

        del(XInput)
        await XPlays()

    else:
        XInput = int(XInput)

        if (XInput < 1) or (XInput > 9) or (board[XInput - 1] == "O") or (board[XInput - 1] == "X"):
            TerminalClear_XO()

            DisplayBoard()

            TerminalPrint_XO("Your Answer ", errorColor, end=""); TerminalPrint_XO(str(XInput), p1Color, end=""); TerminalPrint_XO(" Is Not Valid", errorColor)

            await XPlays()

        else:
            board[XInput - 1] = "X"
            boardColors[XInput - 1] = p1Color

        TerminalPrint_XO("<br>")

async def OPlays():

    TerminalPrint_XO("<br>")
    OInput = await TerminalInput_XO("Where Would You Like To Place Your O:  ", p2Color)

    try:
        OInput = int(OInput)

    except:
        TerminalClear_XO()

        DisplayBoard()

        TerminalPrint_XO("Your Answer ", errorColor, end=""); TerminalPrint_XO(str(OInput), p2Color, end=""); TerminalPrint_XO(" Is Not Valid", errorColor)

        del(OInput)
        await OPlays()

    else:
        OInput = int(OInput)

        if (OInput < 1) or (OInput > 9) or (board[OInput - 1] == "O") or (board[OInput - 1] == "X"):
            TerminalClear_XO()

            DisplayBoard()

            TerminalPrint_XO("Your Answer ", errorColor, end=""); TerminalPrint_XO(str(OInput), p2Color, end=""); TerminalPrint_XO(" Is Not Valid", errorColor)

            await OPlays()

        else:
            board[OInput - 1] = "O"
            boardColors[OInput - 1] = p2Color

        TerminalPrint_XO("<br>")

def CheckXForWin():
    for i in range(8):
        if operator.itemgetter(*winList[i])(board) == ("X","X","X"):
            return True

def CheckOForWin():
    for i in range(8):
        if operator.itemgetter(*winList[i])(board) == ("O","O","O"):
            return True

async def PlayGame():

    for i in range(5):

        TerminalClear_XO()

        DisplayBoard()

        await XPlays()
        if CheckXForWin() == True:
            break

        if i == 4:
            break

        TerminalClear_XO()

        DisplayBoard()

        await OPlays()
        if CheckOForWin() == True:
            break   

def ShowResults():

    if CheckXForWin() == True:

        boardBackgroundColor = p1Color
        DisplayBoard()
        TerminalPrint_XO("X Wins!", p1Color)

    elif CheckOForWin() == True:

        boardBackgroundColor = p2Color
        DisplayBoard()
        TerminalPrint_XO("OWins!", p2Color)

    else:

        boardBackgroundColor = [0, 255, 0]
        DisplayBoard()
        TerminalPrint_XO("Its a Tie!", [0, 255, 0])

async def AskToPlayAgain():

    TerminalPrint_XO("<br>")
    again = await TerminalInput_XO("Do You Want To Play Again?  ")

    if again.lower() == "yes":
            global board
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

            await GameLoop()

    elif again.lower() == "no":
        pass

    else:
        TerminalClear_XO()

        TerminalPrint_XO("Your Answer ", errorColor, end=""); TerminalPrint_XO(str(again), [255, 255, 0], end=""); TerminalPrint_XO(" Is Not Valid", errorColor)

        await AskToPlayAgain()

async def GameLoop():

    await PlayGame() 
    
    TerminalClear_XO()

    ShowResults()

    await AskToPlayAgain()

await GameLoop()    
