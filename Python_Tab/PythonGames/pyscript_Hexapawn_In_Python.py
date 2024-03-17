#region pyscriptFunctions

from pyscript import document
import asyncio

global sentInput_Hexapawn
sentInput_Hexapawn = False


def TerminalPrint_Hexapawn(text, rgb = [255, 255, 255], end= "<br>"):
    document.querySelector("#outputDisplay_Hexapawn").innerHTML += (f'<span style="color:rgb({rgb[0]}, {rgb[1]}, {rgb[2]})">{text}</span>{end}')

def TerminalClear_Hexapawn():
    document.querySelector("#outputDisplay_Hexapawn").innerHTML = ""

def SendInput_Hexapawn(other):
    global sentInput_Hexapawn

    sentInput_Hexapawn = True

async def TerminalInput_Hexapawn(prompt = "", rgb = [255, 255, 255]): 
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    global sentInput_Hexapawn

    sentInput_Hexapawn = False

    TerminalPrint_Hexapawn(prompt, rgb, end= "")

    while sentInput_Hexapawn == False:
        await asyncio.sleep(1)

    sentInput_Hexapawn = False

    TerminalPrint_Hexapawn(document.querySelector("#inputString_Hexapawn").value)

    inputBoxValue = document.querySelector("#inputString_Hexapawn").value
    document.querySelector("#inputString_Hexapawn").value = ""

    return inputBoxValue

async def TerminalSleep_Hexapawn(duration):
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    await asyncio.sleep(duration)


#endregion
    


global board
global boardOutlineColor

p1PossibleMoves = [74, 41, 85, 52, 96, 63]
p1PossibleCaptures = [75, 42, 84, 86, 51, 53, 95, 62]

p2PossibleMoves = [14, 47, 25, 58, 36, 69]
p2PossibleCaptures = [15, 48, 24, 26, 57, 59, 35, 68]

p1PawnColor = [0, 0, 255]
p2PawnColor = [255, 0, 0]
emptyColor = [255, 255, 255]
pawnColors = [emptyColor, p1PawnColor, p2PawnColor]
boardOutlineColor = [255, 255, 0]

board = [pawnColors[2], pawnColors[2], pawnColors[2], pawnColors[0], pawnColors[0], pawnColors[0], pawnColors[1], pawnColors[1], pawnColors[1]]

def DisplayBoard():

    TerminalClear_Hexapawn()

    TerminalPrint_Hexapawn("<br>")

    TerminalPrint_Hexapawn("  " + " ◼  ", board[0], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  ◼  ", board[1], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  ◼ ", board[2])
    TerminalPrint_Hexapawn(" ――――", boardOutlineColor)

    TerminalPrint_Hexapawn("  " + " ◼  ", board[3], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  ◼  ", board[4], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  ◼ ", board[5])

    TerminalPrint_Hexapawn(" ――――", boardOutlineColor)
    TerminalPrint_Hexapawn("  " + " ◼  ", board[6], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  ◼  ", board[7], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  ◼ ", board[8])

    TerminalPrint_Hexapawn("<br>")

    TerminalPrint_Hexapawn("  " + "  1  ", pawnColors[0], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  2  ", pawnColors[0], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  3  ", pawnColors[0])
    TerminalPrint_Hexapawn(" ―――", boardOutlineColor)

    TerminalPrint_Hexapawn("  " + "  4  ", pawnColors[0], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  5  ", pawnColors[0], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  6  ", pawnColors[0])

    TerminalPrint_Hexapawn(" ―――", boardOutlineColor)
    TerminalPrint_Hexapawn("  " + "  7  ", pawnColors[0], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  8  ", pawnColors[0], end=""); TerminalPrint_Hexapawn("|", boardOutlineColor, end=""); TerminalPrint_Hexapawn("  9  ", pawnColors[0])
    TerminalPrint_Hexapawn("<br>")

async def Player1Turn():

    DisplayBoard()

    while True:
        p1Input = await TerminalInput_Hexapawn("\nBlue's turn: ", p1PawnColor)

        try:
            p1Input = int(p1Input)

        except:
            DisplayBoard()

            TerminalPrint_Hexapawn("\nYour answer ", [160,32,240], end=""); TerminalPrint_Hexapawn(str(p1Input), p1PawnColor, end=""); await TerminalInput_Hexapawn(" is not valid, press enter to continue", [160,32,240])
            del(p1Input)            

        else:
            p1Input = int(p1Input)

            twoDigitList = [int(x) for x in str(p1Input)]

            if p1Input in p1PossibleMoves:
                if board[twoDigitList[0] - 1] == pawnColors[1]:
                    if board[twoDigitList[1] -1] == pawnColors[0]:
                        board[twoDigitList[0] - 1] = pawnColors[0]
                        board[twoDigitList[1] - 1] = pawnColors[1]

                        del(p1Input) 
                        del(twoDigitList)
                        break

            elif p1Input in p1PossibleCaptures:
                if board[twoDigitList[0] - 1] == pawnColors[1]:
                    if board[twoDigitList[1] - 1] == pawnColors[2]:
                        board[twoDigitList[0] - 1] = pawnColors[0]
                        board[twoDigitList[1] - 1] = pawnColors[1]

                        del(p1Input) 
                        del(twoDigitList)
                        break
            
            DisplayBoard()

            TerminalPrint_Hexapawn("\nYour answer ", [160,32,240], end=""); TerminalPrint_Hexapawn(str(p1Input), p1PawnColor, end=""); await TerminalInput_Hexapawn(" is not valid, press enter to continue", [160,32,240])
        
            del(p1Input) 
            del(twoDigitList)    

            DisplayBoard()            

async def Player2Turn():

    DisplayBoard()

    while True:
        p2Input = await TerminalInput_Hexapawn("\nRed's turn: ", p2PawnColor)

        try:
            p2Input = int(p2Input)

        except:
            DisplayBoard()

            TerminalPrint_Hexapawn("\nYour answer ", [160,32,240], end=""); TerminalPrint_Hexapawn(str(p2Input), p2PawnColor, end=""); await TerminalInput_Hexapawn(" is not valid, press enter to continue", [160,32,240])
            del(p2Input)            

        else:
            p2Input = int(p2Input)

            twoDigitList = [int(x) for x in str(p2Input)]

            if p2Input in p2PossibleMoves:
                if board[twoDigitList[0] - 1] == pawnColors[2]:
                    if board[twoDigitList[1] -1] == pawnColors[0]:
                        board[twoDigitList[0] - 1] = pawnColors[0]
                        board[twoDigitList[1] - 1] = pawnColors[2]

                        del(p2Input) 
                        del(twoDigitList)
                        break

            elif p2Input in p2PossibleCaptures:
                if board[twoDigitList[0] - 1] == pawnColors[2]:
                    if board[twoDigitList[1] - 1] == pawnColors[1]:
                        board[twoDigitList[0] - 1] = pawnColors[0]
                        board[twoDigitList[1] - 1] = pawnColors[2]

                        del(p2Input) 
                        del(twoDigitList)
                        break
            
            DisplayBoard()

            TerminalPrint_Hexapawn("\nYour answer ", [160,32,240], end=""); TerminalPrint_Hexapawn(str(p2Input), p2PawnColor, end=""); await TerminalInput_Hexapawn(" is not valid, press enter to continue", [160,32,240])
            del(p2Input) 
            del(twoDigitList)    

            DisplayBoard()        

def CheckIfMoveIsPossible(move, player):
    splitMove = [int(x) for x in str(move)]

    if player == 1:
        if move in p1PossibleMoves:
            if board[splitMove[0] - 1] == pawnColors[1]:
                if board[splitMove[1] -1] == pawnColors[0]:
                    return True
        elif move in p1PossibleCaptures:
            if board[splitMove[0] - 1] == pawnColors[1]:
                if board[splitMove[1] -1] == pawnColors[2]:
                    return True
            
    elif player == 2:
        if move in p2PossibleMoves:
            if board[splitMove[0] - 1] == pawnColors[2]:
                if board[splitMove[1] -1] == pawnColors[0]: 
                    return True  
        elif move in p2PossibleCaptures:
            if board[splitMove[0] - 1] == pawnColors[2]:
                if board[splitMove[1] -1] == pawnColors[1]: 
                    return True  
                
    return False

def CheckForP1Win():
    stuckCounter = 0

    if (board[0] == pawnColors[1]) or (board[1] == pawnColors[1]) or (board[2] == pawnColors[1]):
        return True
    else:
        for i in range(len(p2PossibleMoves)):
            if CheckIfMoveIsPossible(p2PossibleMoves[i], 2) == False:
                stuckCounter += 1  
            
        for i in range(len(p2PossibleCaptures)):
            if CheckIfMoveIsPossible(p2PossibleCaptures[i], 2) == False:
                stuckCounter += 1

    if stuckCounter == 14:
        return True           
    
    return False
         
def CheckForP2Win():    
    stuckCounter = 0

    if (board[6] == pawnColors[2]) or (board[7] == pawnColors[2]) or (board[8] == pawnColors[2]):
        return True
    else:
        for i in range(len(p1PossibleMoves)):
            if CheckIfMoveIsPossible(p1PossibleMoves[i], 1) == False:
                stuckCounter += 1
                
            
        for i in range(len(p1PossibleCaptures)):
            if CheckIfMoveIsPossible(p2PossibleCaptures[i], 1) == False:
                stuckCounter += 1

    if stuckCounter == 14:
        return True           
    
    return False

async def GameEnd():
    global board
    global boardOutlineColor
    global p1Win
    global p2Win

    if p1Win == True:
        boardOutlineColor = p1PawnColor
    elif p2Win == True:
        boardOutlineColor = p2PawnColor

    DisplayBoard()

    if p1Win == True:
        TerminalPrint_Hexapawn("Blue Wins!", p1PawnColor)
    elif p2Win == True:
        TerminalPrint_Hexapawn("Red Wins!", p2PawnColor)

    if (await TerminalInput_Hexapawn("\nif you want to play again type 1, if you dont want to play again press send: ", [160,32,240])) == "1":
        board = [pawnColors[2], pawnColors[2], pawnColors[2], pawnColors[0], pawnColors[0], pawnColors[0], pawnColors[1], pawnColors[1], pawnColors[1]]
        
        del(p1Win)
        del(p2Win)
        boardOutlineColor = [255, 255, 0]
        await StartGameLoop()

async def StartGameLoop():
    global p1Win
    global p2Win

    p1Win = False
    p2Win = False

    while True:

        await Player1Turn()

        if CheckForP1Win() == True:
            p1Win = True
            await GameEnd()
            break
    

        await Player2Turn()
        if CheckForP2Win() == True:
            p2Win = True
            await GameEnd()
            break


await StartGameLoop()

TerminalClear_Hexapawn()
TerminalPrint_Hexapawn("Thanks for playing, if you want to play again refresh this page")
#Banana_Power