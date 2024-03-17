#region pyscriptFunctions

from pyscript import document
import asyncio

global sentInput_BigTac
sentInput_BigTac = False

def TerminalPrint_BigTac(text, rgb = [255, 255, 255], end= "<br>"):
    document.querySelector("#outputDisplay_BigTac").innerHTML += (f'<span style="color:rgb({rgb[0]}, {rgb[1]}, {rgb[2]})">{text}</span>{end}')

def TerminalClear_BigTac():
    document.querySelector("#outputDisplay_BigTac").innerHTML = ""

def SendInput_BigTac(other):
    global sentInput_BigTac

    sentInput_BigTac = True

async def TerminalInput_BigTac(prompt = "", rgb = [255, 255, 255]): 
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    global sentInput_BigTac

    sentInput_BigTac = False

    TerminalPrint_BigTac(prompt, rgb, end= "")

    while sentInput_BigTac == False:
        await asyncio.sleep(1)

    sentInput_BigTac = False

    TerminalPrint_BigTac(document.querySelector("#inputString_BigTac").value)

    inputBoxValue = document.querySelector("#inputString_BigTac").value
    document.querySelector("#inputString_BigTac").value = ""

    return inputBoxValue

async def TerminalSleep_BigTac(duration):
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    await asyncio.sleep(duration)


#endregion

from operator import itemgetter

global unselectedBoardColor
global selectedBoardColor
global bigBoardColor
global XColor
global OColor
global triColor
global emptyColor
global invalidText
global normalText
global board
global colorBoard
global innerBoardColors
global validPositions
global currentSelectedBoard
global validEmptyPositions
global winList


unselectedBoardColor = [200, 200, 200] #white
selectedBoardColor = [0, 255, 0] #yellow
bigBoardColor = [128, 0, 255] #purple

XColor = [0, 0, 255] #blue
OColor = [255, 0, 0] #red
triColor = [0, 255, 0] #green
emptyColor = [175, 175, 175] #gray

invalidText = [128, 0, 255] #purple
normalText = [255, 255, 255] #white

board = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]

outerBoard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

colorBoard = [[emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor], [emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor], [emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor], [emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor], [emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor], [emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor], [emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor], [emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor], [emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor, emptyColor]]

innerBoardColors = [unselectedBoardColor, unselectedBoardColor, unselectedBoardColor, unselectedBoardColor, unselectedBoardColor, unselectedBoardColor, unselectedBoardColor, unselectedBoardColor, unselectedBoardColor]

validPositions = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]

validEmptyPositions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

winList = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

currentSelectedBoard = -1


def DisplayBoard(): # Finshed line 102 continue from 104
    global innerBoardColors

    TerminalPrint_BigTac("")
    TerminalPrint_BigTac(f"⠀ ⠀ ⠀{board[0][0]}⠀⠀", colorBoard[0][0], end = ""); TerminalPrint_BigTac("|", innerBoardColors[0], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[0][1]}⠀⠀", colorBoard[0][1], end=""); TerminalPrint_BigTac("|", innerBoardColors[0], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[0][2]}⠀⠀", colorBoard[0][2], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[1][0]}⠀⠀", colorBoard[1][0], end = ""); TerminalPrint_BigTac("|", innerBoardColors[1], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[1][1]}⠀⠀", colorBoard[1][1], end=""); TerminalPrint_BigTac("|", innerBoardColors[1], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[1][2]}⠀⠀", colorBoard[1][2], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[2][0]}⠀⠀", colorBoard[2][0], end = ""); TerminalPrint_BigTac("|", innerBoardColors[2], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[2][1]}⠀⠀", colorBoard[2][1], end=""); TerminalPrint_BigTac("|", innerBoardColors[2], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[2][2]}⠀⠀", colorBoard[2][2])
    TerminalPrint_BigTac("⠀-----------|---------|---------", innerBoardColors[0], end=""); TerminalPrint_BigTac("|", bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|---------", innerBoardColors[1], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|--------", innerBoardColors[2])
    TerminalPrint_BigTac(f"⠀ ⠀ ⠀{board[0][3]}⠀⠀", colorBoard[0][3], end = ""); TerminalPrint_BigTac("|", innerBoardColors[0], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[0][4]}⠀⠀", colorBoard[0][4], end=""); TerminalPrint_BigTac("|", innerBoardColors[0], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[0][5]}⠀⠀", colorBoard[0][5], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[1][3]}⠀⠀", colorBoard[1][3], end = ""); TerminalPrint_BigTac("|", innerBoardColors[1], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[1][4]}⠀⠀", colorBoard[1][4], end=""); TerminalPrint_BigTac("|", innerBoardColors[1], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[1][5]}⠀⠀", colorBoard[1][5], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[2][3]}⠀⠀", colorBoard[2][3], end = ""); TerminalPrint_BigTac("|", innerBoardColors[2], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[2][4]}⠀⠀", colorBoard[2][4], end=""); TerminalPrint_BigTac("|", innerBoardColors[2], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[2][5]}⠀⠀", colorBoard[2][5])
    TerminalPrint_BigTac("⠀-----------|---------|---------", innerBoardColors[0], end=""); TerminalPrint_BigTac("|", bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|---------", innerBoardColors[1], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|--------", innerBoardColors[2])
    TerminalPrint_BigTac(f"⠀ ⠀ ⠀{board[0][6]}⠀⠀", colorBoard[0][6], end = ""); TerminalPrint_BigTac("|", innerBoardColors[0], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[0][7]}⠀⠀", colorBoard[0][7], end=""); TerminalPrint_BigTac("|", innerBoardColors[0], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[0][8]}⠀⠀", colorBoard[0][8], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[1][6]}⠀⠀", colorBoard[1][6], end = ""); TerminalPrint_BigTac("|", innerBoardColors[1], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[1][7]}⠀⠀", colorBoard[1][7], end=""); TerminalPrint_BigTac("|", innerBoardColors[1], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[1][8]}⠀⠀", colorBoard[1][8], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[2][6]}⠀⠀", colorBoard[2][6], end = ""); TerminalPrint_BigTac("|", innerBoardColors[2], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[2][7]}⠀⠀", colorBoard[2][7], end=""); TerminalPrint_BigTac("|", innerBoardColors[2], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[2][8]}⠀⠀", colorBoard[2][8])
    #TerminalPrint_BigTac("               |               |               ", bigBoardColor)

    TerminalPrint_BigTac("⠀-------------------------------|-----------------------------|------------------------------", bigBoardColor)

    TerminalPrint_BigTac(f"⠀ ⠀ ⠀{board[3][0]}⠀⠀", colorBoard[3][0], end = ""); TerminalPrint_BigTac("|", innerBoardColors[3], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[3][1]}⠀⠀", colorBoard[3][1], end=""); TerminalPrint_BigTac("|", innerBoardColors[3], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[3][2]}⠀⠀", colorBoard[3][2], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[4][0]}⠀⠀", colorBoard[4][0], end = ""); TerminalPrint_BigTac("|", innerBoardColors[4], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[4][1]}⠀⠀", colorBoard[4][1], end=""); TerminalPrint_BigTac("|", innerBoardColors[4], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[4][2]}⠀⠀", colorBoard[4][2], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[5][0]}⠀⠀", colorBoard[5][0], end = ""); TerminalPrint_BigTac("|", innerBoardColors[5], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[5][1]}⠀⠀", colorBoard[5][1], end=""); TerminalPrint_BigTac("|", innerBoardColors[5], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[5][2]}⠀⠀", colorBoard[5][2])
    TerminalPrint_BigTac("⠀-----------|---------|---------", innerBoardColors[3], end=""); TerminalPrint_BigTac("|", bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|---------", innerBoardColors[4], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|--------", innerBoardColors[5])
    TerminalPrint_BigTac(f"⠀ ⠀ ⠀{board[3][3]}⠀⠀", colorBoard[3][3], end = ""); TerminalPrint_BigTac("|", innerBoardColors[3], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[3][4]}⠀⠀", colorBoard[3][4], end=""); TerminalPrint_BigTac("|", innerBoardColors[3], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[3][5]}⠀⠀", colorBoard[3][5], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[4][3]}⠀⠀", colorBoard[4][3], end = ""); TerminalPrint_BigTac("|", innerBoardColors[4], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[4][4]}⠀⠀", colorBoard[4][4], end=""); TerminalPrint_BigTac("|", innerBoardColors[4], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[4][5]}⠀⠀", colorBoard[4][5], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[5][3]}⠀⠀", colorBoard[5][3], end = ""); TerminalPrint_BigTac("|", innerBoardColors[5], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[5][4]}⠀⠀", colorBoard[5][4], end=""); TerminalPrint_BigTac("|", innerBoardColors[5], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[5][5]}⠀⠀", colorBoard[5][5])
    TerminalPrint_BigTac("⠀-----------|---------|---------", innerBoardColors[3], end=""); TerminalPrint_BigTac("|", bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|---------", innerBoardColors[4], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|--------", innerBoardColors[5])
    TerminalPrint_BigTac(f"⠀ ⠀ ⠀{board[3][6]}⠀⠀", colorBoard[3][6], end = ""); TerminalPrint_BigTac("|", innerBoardColors[3], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[3][7]}⠀⠀", colorBoard[3][7], end=""); TerminalPrint_BigTac("|", innerBoardColors[3], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[3][8]}⠀⠀", colorBoard[3][8], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[4][6]}⠀⠀", colorBoard[4][6], end = ""); TerminalPrint_BigTac("|", innerBoardColors[4], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[4][7]}⠀⠀", colorBoard[4][7], end=""); TerminalPrint_BigTac("|", innerBoardColors[4], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[4][8]}⠀⠀", colorBoard[4][8], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[5][6]}⠀⠀", colorBoard[5][6], end = ""); TerminalPrint_BigTac("|", innerBoardColors[5], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[5][7]}⠀⠀", colorBoard[5][7], end=""); TerminalPrint_BigTac("|", innerBoardColors[5], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[5][8]}⠀⠀", colorBoard[5][8])
   
    TerminalPrint_BigTac("⠀-------------------------------|-----------------------------|------------------------------", bigBoardColor)

    TerminalPrint_BigTac(f"⠀ ⠀ ⠀{board[6][0]}⠀⠀", colorBoard[6][0], end = ""); TerminalPrint_BigTac("|", innerBoardColors[6], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[6][1]}⠀⠀", colorBoard[6][1], end=""); TerminalPrint_BigTac("|", innerBoardColors[6], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[6][2]}⠀⠀", colorBoard[6][2], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[7][0]}⠀⠀", colorBoard[7][0], end = ""); TerminalPrint_BigTac("|", innerBoardColors[7], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[7][1]}⠀⠀", colorBoard[7][1], end=""); TerminalPrint_BigTac("|", innerBoardColors[7], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[7][2]}⠀⠀", colorBoard[7][2], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[8][0]}⠀⠀", colorBoard[8][0], end = ""); TerminalPrint_BigTac("|", innerBoardColors[8], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[8][1]}⠀⠀", colorBoard[8][1], end=""); TerminalPrint_BigTac("|", innerBoardColors[8], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[8][2]}⠀⠀", colorBoard[8][2])
    TerminalPrint_BigTac("⠀-----------|---------|---------", innerBoardColors[6], end=""); TerminalPrint_BigTac("|", bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|---------", innerBoardColors[7], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|--------", innerBoardColors[8])
    TerminalPrint_BigTac(f"⠀ ⠀ ⠀{board[6][3]}⠀⠀", colorBoard[6][3], end = ""); TerminalPrint_BigTac("|", innerBoardColors[6], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[6][4]}⠀⠀", colorBoard[6][4], end=""); TerminalPrint_BigTac("|", innerBoardColors[6], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[6][5]}⠀⠀", colorBoard[6][5], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[7][3]}⠀⠀", colorBoard[7][3], end = ""); TerminalPrint_BigTac("|", innerBoardColors[7], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[7][4]}⠀⠀", colorBoard[7][4], end=""); TerminalPrint_BigTac("|", innerBoardColors[7], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[7][5]}⠀⠀", colorBoard[7][5], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[8][3]}⠀⠀", colorBoard[8][3], end = ""); TerminalPrint_BigTac("|", innerBoardColors[8], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[8][4]}⠀⠀", colorBoard[8][4], end=""); TerminalPrint_BigTac("|", innerBoardColors[8], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[8][5]}⠀⠀", colorBoard[8][5])
    TerminalPrint_BigTac("⠀-----------|---------|---------", innerBoardColors[6], end=""); TerminalPrint_BigTac("|", bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|---------", innerBoardColors[7], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac("----------|---------|--------", innerBoardColors[8])
    TerminalPrint_BigTac(f"⠀ ⠀ ⠀{board[6][6]}⠀⠀", colorBoard[6][6], end = ""); TerminalPrint_BigTac("|", innerBoardColors[6], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[6][7]}⠀⠀", colorBoard[6][7], end=""); TerminalPrint_BigTac("|", innerBoardColors[6], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[6][8]}⠀⠀", colorBoard[6][8], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[7][6]}⠀⠀", colorBoard[7][6], end = ""); TerminalPrint_BigTac("|", innerBoardColors[7], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[7][7]}⠀⠀", colorBoard[7][7], end=""); TerminalPrint_BigTac("|", innerBoardColors[7], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[7][8]}⠀⠀", colorBoard[7][8], end=""); TerminalPrint_BigTac("|", rgb= bigBoardColor, end =""); TerminalPrint_BigTac(f"⠀⠀{board[8][6]}⠀⠀", colorBoard[8][6], end = ""); TerminalPrint_BigTac("|", innerBoardColors[8], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[8][7]}⠀⠀", colorBoard[8][7], end=""); TerminalPrint_BigTac("|", innerBoardColors[8], end= ""); TerminalPrint_BigTac(f"⠀⠀{board[8][8]}⠀⠀", colorBoard[8][8])


async def XPlays():
    global innerBoardColors
    global currentSelectedBoard


    while True:      
        TerminalClear_BigTac()

        DisplayBoard()

        Xinput = await TerminalInput_BigTac("<br>Where do you want to play your X:  ", XColor)

        if (Xinput.isdigit()):
            if (int(Xinput) in validPositions):
                if (((currentSelectedBoard == -1) | ((currentSelectedBoard == int(Xinput[0])-1)) & (board[int(Xinput[0])-1][int(Xinput[1])-1] in validEmptyPositions))):
                    break
        
        del(Xinput)  
        await TerminalInput_BigTac("<br>That's invalid, press send to try again", invalidText)

    Xinput = [int(Xinput[0]), int(Xinput[1])]

    board[Xinput[0]-1][Xinput[1]-1] = "x"
    colorBoard[Xinput[0]-1][Xinput[1]-1] = XColor


    for i in range(len(innerBoardColors)):
        if innerBoardColors[i] == selectedBoardColor:
            innerBoardColors[i] = unselectedBoardColor

    innerBoardColors[Xinput[1]-1] = selectedBoardColor

    InnerWinCheck()

    if ((innerBoardColors[Xinput[1]-1] == XColor) | (innerBoardColors[Xinput[1]-1] == OColor)):
        currentSelectedBoard = -1
    else:
        currentSelectedBoard = Xinput[1]-1


async def OPlays():
    global innerBoardColors
    global currentSelectedBoard


    while True:
        TerminalClear_BigTac()

        DisplayBoard()

        Oinput = await TerminalInput_BigTac("<br>Where do you want to play your O:  ", OColor)
        
        if (Oinput.isdigit()):
            if (int(Oinput) in validPositions):
                if (((currentSelectedBoard == -1) | ((currentSelectedBoard == int(Oinput[0])-1)) & (board[int(Oinput[0])-1][int(Oinput[1])-1] in validEmptyPositions))):
                    break
        
        del(Oinput)  
        await TerminalInput_BigTac("<br>That's invalid, press send to try again", invalidText)

    Oinput = [int(Oinput[0]), int(Oinput[1])]

    board[Oinput[0]-1][Oinput[1]-1] = "o"
    colorBoard[Oinput[0]-1][Oinput[1]-1] = OColor

    for i in range(len(innerBoardColors)):
        if innerBoardColors[i] == selectedBoardColor:
            innerBoardColors[i] = unselectedBoardColor

    innerBoardColors[Oinput[1]-1] = selectedBoardColor

    InnerWinCheck()

    if ((innerBoardColors[Oinput[1]-1] == XColor) | (innerBoardColors[Oinput[1]-1] == OColor)):
        currentSelectedBoard = -1
    else:
        currentSelectedBoard = Oinput[1]-1


def InnerWinCheck():     

    for i in range(9):
        for j in range(8):
            if itemgetter(*winList[j])(board[i]) == ("x","x","x"):
                innerBoardColors[i] = XColor
                outerBoard[i] = "x"

                for k in range(9):
                    board[i][k] = "x"
                    colorBoard[i][k] = XColor
    
    for i in range(9):
        for j in range(8):
            if itemgetter(*winList[j])(board[i]) == ("o","o","o"):
                innerBoardColors[i] = OColor
                outerBoard[i] = "o"

                for k in range(9):
                    board[i][k] = "o"
                    colorBoard[i][k] = OColor


def OuterWinCheckX():

    for i in range(8):
        if itemgetter(*winList[i])(outerBoard) == ("x","x","x"):
            return True
        
    return False


def OuterWinCheckO():

    for i in range(8):
        if itemgetter(*winList[i])(outerBoard) == ("o","o","o"):
            return True
    
    return False


async def GameLoop():

    if OuterWinCheckO() == False:
        await XPlays()

    if OuterWinCheckX() == False:
        await OPlays()

    if OuterWinCheckX() == True:
        TerminalClear_BigTac()
        TerminalPrint_BigTac("X Wins!", XColor)

    elif OuterWinCheckO() == True:
        TerminalClear_BigTac()
        TerminalPrint_BigTac("O Wins!", OColor)

    else:
        await GameLoop()

await GameLoop() 

#banana_power