#region pyscriptFunctions

from pyscript import document
import asyncio

global sentInput_BattleShip
sentInput_BattleShip = False


def SendInput_BattleShip(other):
    global sentInput_BattleShip

    sentInput_BattleShip = True

def TerminalPrint_BattleShip(text, rgb = [255, 255, 255], end= "<br>"):
    document.querySelector("#outputDisplay_BattleShip").innerHTML += (f'<span style="color:rgb({rgb[0]}, {rgb[1]}, {rgb[2]})">{text}</span>{end}')

def TerminalClear_BattleShip():
    document.querySelector("#outputDisplay_BattleShip").innerHTML = ""

async def TerminalInput_BattleShip(prompt = "", rgb = [255, 255, 255]): 
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    global sentInput_BattleShip

    sentInput_BattleShip = False

    TerminalPrint_BattleShip(prompt, rgb, end= "")

    while sentInput_BattleShip == False:
        await asyncio.sleep(1)

    sentInput_BattleShip = False

    TerminalPrint_BattleShip(document.querySelector("#inputString_BattleShip").value)

    inputBoxValue = document.querySelector("#inputString_BattleShip").value
    document.querySelector("#inputString_BattleShip").value = ""

    return inputBoxValue

async def TerminalSleep_BattleShip(duration):
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    await asyncio.sleep(duration)

#endregion



p1ShipColor = [0, 0, 255]
p2ShipColor = [255, 0, 0]
emptyColor = [255, 255, 255]
brokenShipColor = [160, 32, 240]
missedMissileColor = [255, 255, 0]
hitMissileColor = [0, 255, 0]
mineColor = [100, 100, 100]
brokenMineColor = [255, 111, 0]
errorColor = [160,32,240]


global totalP1MissileCount
global totalP2MissileCount

global totalSmallShipCount
global totalLargeShipCount

global totalMineCount


global currentTurn

mineMissilePenalty = 1
hitShipBoost = 1

acceptablePositions = ("A1 A2 A3 A4 A5 A6 B1 B2 B3 B4 B5 B6 C1 C2 C3 C4 C5 C6 D1 D2 D3 D4 D5 D6 E1 E2 E3 E4 E5 E6 F1 F2 F3 F4 F5 F6").split()


def GetIndexFromPosition(pos):
    for i in range(len(acceptablePositions)):
        if acceptablePositions[i] == pos:
            return i
       
async def PrivacyScreen(currentPlayerTurn):
    TerminalClear_BattleShip()
    
    if currentPlayerTurn == "P1":
        TerminalPrint_BattleShip("It's " , end=""); TerminalPrint_BattleShip("Player one's ", p1ShipColor, end=""); await TerminalInput_BattleShip("turn, press enter to continue ")
    if currentPlayerTurn == "P2":
        TerminalPrint_BattleShip("It's " , end=""); TerminalPrint_BattleShip("Player two's ", p2ShipColor, end=""); await TerminalInput_BattleShip("turn, press enter to continue ")

def IsDeadCheck(playerToCheck):

    if playerToCheck == "P1":
        
        livingShipCount = 0

        for i in range(len(p1HomeBoard)):

            if p1HomeBoard[i][1] == p1ShipColor:
                livingShipCount += 1
        
        if livingShipCount > 0:
            del(livingShipCount)
            return False
        else:
            del(livingShipCount)
            return True


    elif playerToCheck == "P2":
        
        livingShipCount = 0

        for i in range(len(p2HomeBoard)):

            if p2HomeBoard[i][1] == p2ShipColor:
                livingShipCount += 1
        
        if livingShipCount > 0:
            del(livingShipCount)
            return False
        else:
            del(livingShipCount)
            return True


def DisplayP1HomeBoard():

    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])
    TerminalPrint_BattleShip("┃", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⌂", p1ShipColor, end=""); TerminalPrint_BattleShip(" ⠀ ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 1 ⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 2⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 3⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 4⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 5⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 6⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀A⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[0][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[1][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[2][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[3][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[4][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[5][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀B⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[6][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[7][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[8][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[9][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[10][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[11][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀C⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[12][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[13][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[14][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[15][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[16][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[17][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀D⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[18][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[19][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[20][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[21][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[22][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[23][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀E⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[24][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[25][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[26][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[27][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[28][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀ ", p1HomeBoard[29][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀F⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[30][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀", p1HomeBoard[31][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[32][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[33][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1HomeBoard[34][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀ ", p1HomeBoard[35][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("<br>") 

def DisplayP1AttackBoard():

    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])
    TerminalPrint_BattleShip("┃", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⚔", p1ShipColor, end=""); TerminalPrint_BattleShip(" ⠀ ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 1 ⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 2⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 3⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 4⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 5⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 6⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀A⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[0][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[1][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[2][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[3][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[4][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[5][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀B⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[6][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[7][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[8][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[9][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[10][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[11][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀C⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[12][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[13][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[14][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[15][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[16][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[17][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀D⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[18][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[19][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[20][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[21][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[22][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[23][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀E⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[24][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[25][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[26][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[27][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[28][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀ ", p1AttackBoard[29][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀F⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[30][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀", p1AttackBoard[31][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[32][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[33][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p1AttackBoard[34][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀ ", p1AttackBoard[35][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0]) 



def DisplayP2HomeBoard():

    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])
    TerminalPrint_BattleShip("┃", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⌂", p2ShipColor, end=""); TerminalPrint_BattleShip(" ⠀ ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 1 ⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 2⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 3⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 4⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 5⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 6⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀A⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[0][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[1][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[2][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[3][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[4][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[5][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀B⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[6][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[7][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[8][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[9][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[10][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[11][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀C⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[12][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[13][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[14][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[15][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[16][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[17][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀D⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[18][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[19][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[20][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[21][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[22][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[23][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀E⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[24][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[25][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[26][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[27][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[28][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀ ", p2HomeBoard[29][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀F⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[30][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀", p2HomeBoard[31][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[32][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[33][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2HomeBoard[34][1], end=""); TerminalPrint_BattleShip(" ┃ ", [0, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀ ", p2HomeBoard[35][1], end=""); TerminalPrint_BattleShip("┃", [0, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [0, 255, 0])

    TerminalPrint_BattleShip("<br>") 

def DisplayP2AttackBoard():
    
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])
    TerminalPrint_BattleShip("┃", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⚔", p2ShipColor, end=""); TerminalPrint_BattleShip(" ⠀ ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 1 ⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 2⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 3⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 4⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 5⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀ ⠀ 6⠀ ⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀A⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[0][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[1][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[2][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[3][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[4][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[5][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀B⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[6][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[7][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[8][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[9][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[10][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[11][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀C⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[12][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[13][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[14][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[15][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[16][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[17][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀D⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[18][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[19][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[20][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[21][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[22][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[23][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀E⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[24][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[25][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[26][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[27][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[28][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀ ", p2AttackBoard[29][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0])

    TerminalPrint_BattleShip("┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀F⠀", [230, 83, 0], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[30][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀", p2AttackBoard[31][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[32][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[33][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip("⠀⠀ ◼ ⠀⠀", p2AttackBoard[34][1], end=""); TerminalPrint_BattleShip(" ┃ ", [255, 255, 0], end=""); TerminalPrint_BattleShip(" ⠀⠀ ◼ ⠀⠀ ", p2AttackBoard[35][1], end=""); TerminalPrint_BattleShip("┃", [255, 255, 0])
    TerminalPrint_BattleShip("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃⠀", [255, 255, 0]) 


async def PlaceP1SmallShips():
    for i in range(totalSmallShipCount):
        while True:

            try:

                TerminalClear_BattleShip()
                DisplayP1HomeBoard()

                inputedLoc = await TerminalInput_BattleShip("<br>Type where you would like the head of your 2 units long small ship to go and which direction the tail should be: ", p1ShipColor)
                inputedLoc = inputedLoc.split()

            except:
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(inputedLoc)

            else:

                if len(inputedLoc) > 1:

                    if inputedLoc[0] in acceptablePositions:

                        match inputedLoc[1].lower():

                            case "up":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 2, 3, 4, 5]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] == emptyColor:

                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] = p1ShipColor
                                            break

                            case "down":

                                if GetIndexFromPosition(inputedLoc[0]) not in [30, 31, 32, 33, 34, 35]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] == emptyColor:
                                                                                    
                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] = p1ShipColor
                                            break

                            case "left":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 6, 12, 18, 24, 30]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] == emptyColor:

                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] = p1ShipColor
                                            break

                            case "right":

                                if GetIndexFromPosition(inputedLoc[0]) not in [5, 11, 17, 23, 29, 35]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] == emptyColor:

                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] = p1ShipColor
                                            break
                            
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedLoc)

                    else:
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedLoc)
                else: 
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(inputedLoc)

async def PlaceP2SmallShips():
    for i in range(totalSmallShipCount):
        while True:

            try:

                TerminalClear_BattleShip()
                DisplayP2HomeBoard()

                inputedLoc = await TerminalInput_BattleShip("<br>Type where you would like the head of your 2 units long small ship to go and which direction the tail should be: ", p2ShipColor)
                inputedLoc = inputedLoc.split()

            except:
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(inputedLoc)

            else:

                if len(inputedLoc) > 1:

                    if inputedLoc[0] in acceptablePositions:

                        match inputedLoc[1].lower():

                            case "up":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 2, 3, 4, 5]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] == emptyColor:

                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] = p2ShipColor
                                            break

                            case "down":

                                if GetIndexFromPosition(inputedLoc[0]) not in [30, 31, 32, 33, 34, 35]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] == emptyColor:

                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] = p2ShipColor
                                            break

                            case "left":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 6, 12, 18, 24, 30]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] == emptyColor:

                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] = p2ShipColor
                                            break

                            case "right":

                                if GetIndexFromPosition(inputedLoc[0]) not in [5, 11, 17, 23, 29, 35]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] == emptyColor:

                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] = p2ShipColor
                                            break
                            
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedLoc)

                    else:
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedLoc)
                else: 
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(inputedLoc)

async def PlaceP1LargeShips():

    for i in range(totalLargeShipCount):
        while True:

            try:

                TerminalClear_BattleShip()
                DisplayP1HomeBoard()

                inputedLoc = await TerminalInput_BattleShip("<br>Type where you would like the head of your 3 units long large ship to go and which direction the tail should be: ", p1ShipColor)
                inputedLoc = inputedLoc.split()

            except:
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(inputedLoc)

            else:

                if len(inputedLoc) > 1:

                    if inputedLoc[0] in acceptablePositions:

                        match inputedLoc[1].lower():

                            case "up":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] == emptyColor:

                                            if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 12][1] == emptyColor:

                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 12][1] = p1ShipColor
                                                break

                            case "down":

                                if GetIndexFromPosition(inputedLoc[0]) not in [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor: 

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] == emptyColor:

                                            if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 12][1] == emptyColor:

                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] = p1ShipColor                                            
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 12][1] = p1ShipColor
                                                break

                            case "left":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 6, 7, 12, 13, 18, 19, 24, 25, 30, 31]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:                         

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] == emptyColor:   

                                            if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 2][1] == emptyColor:

                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 2][1] = p1ShipColor
                                                break

                            case "right":

                                if GetIndexFromPosition(inputedLoc[0]) not in [4, 5, 10, 11, 16, 17, 22, 23, 28, 29, 34, 35]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] == emptyColor:

                                            if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 2][1] == emptyColor:

                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] = p1ShipColor                                            
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 2][1] = p1ShipColor
                                                break
                            
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedLoc)

                    else:
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedLoc)
                else: 
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(inputedLoc)

async def PlaceP2LargeShips():

    for i in range(totalLargeShipCount):
        while True:

            try:

                TerminalClear_BattleShip()
                DisplayP2HomeBoard()

                inputedLoc = await TerminalInput_BattleShip("<br>Type where you would like the head of your 3 units long large ship to go and which direction the tail should be: ", p2ShipColor)
                inputedLoc = inputedLoc.split()

            except:
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(inputedLoc)

            else:

                if len(inputedLoc) > 1:

                    if inputedLoc[0] in acceptablePositions:

                        match inputedLoc[1].lower():

                            case "up":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:  

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] == emptyColor:

                                            if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 12][1] == emptyColor:

                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 12][1] = p2ShipColor
                                                break

                            case "down":

                                if GetIndexFromPosition(inputedLoc[0]) not in [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] == emptyColor:

                                            if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 12][1] == emptyColor:

                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 12][1] = p2ShipColor
                                                break

                            case "left":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 6, 7, 12, 13, 18, 19, 24, 25, 30, 31]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] == emptyColor:
                                            
                                            if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 2][1] == emptyColor:

                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 2][1] = p2ShipColor
                                                break

                            case "right":

                                if GetIndexFromPosition(inputedLoc[0]) not in [4, 5, 10, 11, 16, 17, 22, 23, 28, 29, 34, 35]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:                     

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] == emptyColor:

                                            if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 2][1] == emptyColor:

                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 2][1] = p2ShipColor
                                                break
                            
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedLoc)

                    else:
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedLoc)
                else: 
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(inputedLoc)

async def PlaceP1Mines():
    for i in range(totalMineCount):

        while True:

            try:
                
                TerminalClear_BattleShip()
                DisplayP1HomeBoard()

                inputedMineLoc = await TerminalInput_BattleShip("<br>Type where you would like to place your mine: ", p1ShipColor)
                inputedMineLoc = inputedMineLoc.split()

            except:
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(inputedMineLoc)

            else:

                if len(inputedMineLoc) > 0:

                    if inputedMineLoc[0] in acceptablePositions:

                        if p1HomeBoard[GetIndexFromPosition(inputedMineLoc[0])][1] == emptyColor:

                            p1HomeBoard[GetIndexFromPosition(inputedMineLoc[0])][1] = mineColor
                            break

                        else:
                            TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedMineLoc)
            
                    else:
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedMineLoc)

                else:
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(inputedMineLoc)

    TerminalClear_BattleShip()
    DisplayP1HomeBoard()

    TerminalPrint_BattleShip("This is your home board", p1ShipColor, end=""); await TerminalInput_BattleShip(", press send to continue ")

async def PlaceP2Mines():
    for i in range(totalMineCount):

        while True:

            try:
                
                TerminalClear_BattleShip()
                DisplayP2HomeBoard()

                inputedMineLoc = await TerminalInput_BattleShip("<br>Type where you would like to place your mine: ", p2ShipColor)
                inputedMineLoc = inputedMineLoc.split()

            except:
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(inputedMineLoc)

            else:

                if len(inputedMineLoc) > 0:

                    if inputedMineLoc[0] in acceptablePositions:

                        if p2HomeBoard[GetIndexFromPosition(inputedMineLoc[0])][1] == emptyColor:
                            
                            p2HomeBoard[GetIndexFromPosition(inputedMineLoc[0])][1] = mineColor
                            break

                        else:
                            TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedMineLoc)
            
                    else:
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedMineLoc)

                else:
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(inputedMineLoc)

    TerminalClear_BattleShip()
    DisplayP2HomeBoard()

    TerminalPrint_BattleShip("This is your home board", p2ShipColor, end=""); await TerminalInput_BattleShip(", press send to continue ")


async def P1AttackTurn():
    global totalP1MissileCount
    global currentTurn
    global P1Gamble
    global P2Gamble

    await PrivacyScreen("P1")

    currentP1MissileCount = totalP1MissileCount

    if currentTurn > 2:

        while True:

            try:
                TerminalClear_BattleShip()

                DisplayP1AttackBoard()

                p1Belief = await TerminalInput_BattleShip(f"<br>Player 2 says there is a ship at {P2Gamble}, if you think he is bluffing type 1, if you think he isn't type 2: ", p1ShipColor)

            except:
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(p1Belief)

            else:
                if p1Belief == "1":

                    if p2HomeBoard[GetIndexFromPosition(P2Gamble)][1] == p2ShipColor:

                        TerminalPrint_BattleShip(f"<br>You were wrong, there is a ship at {P2Gamble}, so you lose a missile this round", p1ShipColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        currentP1MissileCount -= 1
                        break

                    else:

                        TerminalPrint_BattleShip(f"<br>You were right, there isn't a ship at {P2Gamble}, so you get an extra missile this round", p1ShipColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        currentP1MissileCount += 1
                        break

                elif p1Belief == "2":

                    if p2HomeBoard[GetIndexFromPosition(P2Gamble)][1] == p2ShipColor:

                        TerminalPrint_BattleShip(f"<br>You were right, there is a ship at {P2Gamble}, so you get an extra missile this round", p1ShipColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        currentP1MissileCount += 1
                        break

                    else:

                        TerminalPrint_BattleShip(f"<br>You were wrong, there isn't a ship at {P2Gamble}, so you lose a missile this round", p1ShipColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        currentP1MissileCount -= 1
                        break         

                else:
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(p1Belief)

    for i in range(currentP1MissileCount):  

        while True:
            try:
                
                TerminalClear_BattleShip()
                DisplayP1AttackBoard()
                DisplayP1HomeBoard()

                if (currentP1MissileCount - i) > 1: 
                    inputedAttackLoc = await TerminalInput_BattleShip(f"You have {currentP1MissileCount - i} missiles, where you would like to launch your missile: ", p1ShipColor)

                else:
                    inputedAttackLoc = await TerminalInput_BattleShip(f"You have {currentP1MissileCount - i} missile left, where you would like to launch your last missile: ", p1ShipColor)

            except:
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(inputedAttackLoc)

            else:
                if len(inputedAttackLoc) > 0:

                    if inputedAttackLoc in acceptablePositions:

                        if p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == p2ShipColor:

                            p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenShipColor
                            p1AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = hitMissileColor

                            TerminalClear_BattleShip()
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()


                            if IsDeadCheck("P2") == True:

                                TerminalPrint_BattleShip("<br>You destroyed all enemy ships!", p1ShipColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                                del(inputedAttackLoc)

                                return True
                            
                            else:
                                totalP1MissileCount += hitShipBoost

                                TerminalPrint_BattleShip(f"<br>You hit a ship!, and you now have {totalP1MissileCount} total missiles to use next round", p1ShipColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                                del(inputedAttackLoc)

                                break

                        elif p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == brokenShipColor:

                            TerminalClear_BattleShip()
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()

                            TerminalPrint_BattleShip("<br>You already hit that ship!", p1ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedAttackLoc)

                        elif p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == brokenMineColor:

                            TerminalClear_BattleShip()
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()

                            TerminalPrint_BattleShip("<br>You already hit that mine!", p1ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedAttackLoc)

                        elif p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == missedMissileColor:

                            TerminalClear_BattleShip()
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()

                            TerminalPrint_BattleShip("<br>You already launched a missle here!", p1ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedAttackLoc)

                        elif p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == mineColor:

                            if (totalP1MissileCount - mineMissilePenalty) > 0:
                                totalP1MissileCount -= mineMissilePenalty

                            p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenMineColor
                            p1AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenMineColor

                            TerminalClear_BattleShip()
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()

                            TerminalPrint_BattleShip(f"<br>You hit a mine!, and you now have {totalP1MissileCount} total missiles to use next round", p1ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedAttackLoc)
                        
                            break

                        else:

                            p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = missedMissileColor
                            p1AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = missedMissileColor

                            TerminalClear_BattleShip()
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()

                            TerminalPrint_BattleShip("<br>You Missed!", p1ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedAttackLoc)

                            break

                    else:
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedAttackLoc)

                else:
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(inputedAttackLoc)
    
    return False

async def P2AttackTurn():
    global totalP2MissileCount
    global P1Gamble
    global P2Gamble

    await PrivacyScreen("P2")

    currentP2MissileCount = totalP2MissileCount

    if currentTurn > 2:

        while True:

            try:       
                TerminalClear_BattleShip()

                DisplayP2AttackBoard()

                p2Belief = await TerminalInput_BattleShip(f"<br>Player 1 says there is a ship at {P1Gamble}, if you think he is bluffing type 1, if you think he isn't type 2: ", p2ShipColor)

            except:
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(p2Belief)

            else:
                if p2Belief == "1":

                    if p1HomeBoard[GetIndexFromPosition(P1Gamble)][1] == p1ShipColor:

                        TerminalPrint_BattleShip(f"<br>You were wrong, there is a ship at {P1Gamble}, so you lose a missile this round", p2ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                        currentP2MissileCount -= 1
                        break

                    else:

                        TerminalPrint_BattleShip(f"<br>You were right, there isn't a ship at {P1Gamble}, so you get an extra missile this round", p2ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                        currentP2MissileCount += 1
                        break

                elif p2Belief == "2":

                    if p1HomeBoard[GetIndexFromPosition(P1Gamble)][1] == p1ShipColor:

                        TerminalPrint_BattleShip(f"<br>You were right, there is a ship at {P1Gamble}, so you get an extra missile this round", p2ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                        currentP2MissileCount += 1
                        break

                    else:

                        TerminalPrint_BattleShip(f"<br>You were wrong, there isn't a ship at {P1Gamble}, so you lose a missile this round", p2ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                        currentP2MissileCount -= 1       
                        break         

                else:
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(p2Belief)

    for i in range(currentP2MissileCount):  

        while True:
            try:
                
                TerminalClear_BattleShip()
                DisplayP2AttackBoard()
                DisplayP2HomeBoard()

                if (currentP2MissileCount - i) > 1: 
                    inputedAttackLoc = await TerminalInput_BattleShip(f"You have {currentP2MissileCount - i} missiles, where you would like to launch your missile: ", p2ShipColor)

                else:
                    inputedAttackLoc = await TerminalInput_BattleShip(f"You have {currentP2MissileCount - i} missile left, where you would like to launch your last missile: ", p2ShipColor)

            except:
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(inputedAttackLoc)

            else:
                if len(inputedAttackLoc) > 0:

                    if inputedAttackLoc in acceptablePositions:

                        if p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == p1ShipColor:

                            p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenShipColor
                            p2AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = hitMissileColor

                            TerminalClear_BattleShip()
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            if IsDeadCheck("P1") == True:

                                TerminalPrint_BattleShip("<br>You destroyed all enemy ships!", p2ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                                del(inputedAttackLoc)

                                return True
                            
                            else:
                                totalP2MissileCount += hitShipBoost

                                TerminalPrint_BattleShip(f"<br>You hit a ship!, and you now have {totalP2MissileCount} total missiles to use next round", p2ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                                del(inputedAttackLoc)

                                break

                        elif p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == brokenShipColor:

                            TerminalClear_BattleShip()
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            TerminalPrint_BattleShip("<br>You already hit that ship!", p2ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedAttackLoc)

                        elif p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == brokenMineColor:

                            TerminalClear_BattleShip()
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            TerminalPrint_BattleShip("<br>You already hit that mine!", p2ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedAttackLoc)

                        elif p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == missedMissileColor:

                            TerminalClear_BattleShip()
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            TerminalPrint_BattleShip("<br>You already launched a missle here!", p2ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedAttackLoc)

                        elif p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == mineColor:

                            if (totalP2MissileCount - mineMissilePenalty) > 0:
                                totalP2MissileCount -= mineMissilePenalty
                            
                            p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenMineColor
                            p2AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenMineColor

                            TerminalClear_BattleShip()
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            TerminalPrint_BattleShip(f"<br>You hit a mine!, and you now have {totalP2MissileCount} total missiles to use next round", p2ShipColor); await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedAttackLoc)

                            break

                        else:

                            p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = missedMissileColor
                            p2AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = missedMissileColor

                            TerminalClear_BattleShip()
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            TerminalPrint_BattleShip("<br>You Missed!", p2ShipColor);await TerminalInput_BattleShip(", press send to continue ")
                            del(inputedAttackLoc)

                            break

                    else:
                        TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                        del(inputedAttackLoc)

                else:
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(inputedAttackLoc)
    
    return False


async def P1GambleTurn():
    global P1Gamble
    global P2Gamble
    
    while True:

        try:
            TerminalClear_BattleShip()

            DisplayP1HomeBoard()

            P1Gamble = await TerminalInput_BattleShip("<br>Type the position you want to gamble: ", p1ShipColor)

        except:
            TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
            del(P1Gamble)

        else:

            if len(P1Gamble) > 0:

                if P1Gamble in acceptablePositions:
                    break

                else:
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(P1Gamble)

            else: 
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(P1Gamble)

async def P2GambleTurn():
    global P1Gamble
    global P2Gamble
    
    while True:

        try:
            TerminalClear_BattleShip()
    
            DisplayP2HomeBoard()

            P2Gamble = await TerminalInput_BattleShip("<br>Type the position you want to gamble: ", p2ShipColor)

        except:
            TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
            del(P2Gamble)

        else:

            if len(P2Gamble) > 0:

                if P2Gamble in acceptablePositions:
                    break

                else:
                    TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                    del(P2Gamble)

            else: 
                TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
                del(P2Gamble)               


async def GameLoop():

    totalSmallShipCount = 2
    totalLargeShipCount = 2

    totalP1MissileCount = 3
    totalP2MissileCount = 3

    totalMineCount = 4


    currentTurn = 0


    p1HomeBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
            ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
            ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
            ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
            ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
            ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

    p1AttackBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
            ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
            ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
            ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
            ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
            ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

    p2HomeBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
            ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
            ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
            ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
            ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
            ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

    p2AttackBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
            ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
            ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
            ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
            ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
            ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

    await PlaceP1SmallShips()

    await PlaceP1LargeShips()

    await PlaceP1Mines()

    await PlaceP2SmallShips()

    await PlaceP2LargeShips()

    await PlaceP2Mines()

    while True:

        currentTurn += 1

        if (await P1AttackTurn() == True):
            
            TerminalClear_BattleShip()
            DisplayP1AttackBoard()
            DisplayP1HomeBoard()

            TerminalPrint_BattleShip("Player One Wins!", p1ShipColor, end=""); await TerminalInput_BattleShip(", press send to continue ")

            break

        if currentTurn > 2:
            await P1GambleTurn()

        if (await P2AttackTurn() == True):

            TerminalClear_BattleShip()
            DisplayP2AttackBoard()
            DisplayP2HomeBoard()

            TerminalPrint_BattleShip("Player Two Wins!", p2ShipColor, end=""); await TerminalInput_BattleShip(", press send to continue ")

            break
        if currentTurn > 1:
            await P2GambleTurn()

    while True:

        try:        
            TerminalClear_BattleShip()
            askToPlayAgain = await TerminalInput_BattleShip("<br>Do you want to play again?  ", errorColor)

        except:
            TerminalPrint_BattleShip("<br>That's invalid", errorColor, end=""); await TerminalInput_BattleShip(", press send to continue ")
            del(askToPlayAgain)

        else:

            if (askToPlayAgain.lower() == "yes") or (askToPlayAgain.lower() == "no"):
                break

    if askToPlayAgain.lower() == "yes":
        del(askToPlayAgain)
        await GameLoop()

    elif askToPlayAgain.lower() == "no":
        TerminalPrint_BattleShip("Thanks for Playing!")

totalSmallShipCount = 2
totalLargeShipCount = 2

totalP1MissileCount = 3
totalP2MissileCount = 3

totalMineCount = 4


currentTurn = 0


p1HomeBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
        ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
        ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
        ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
        ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
        ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

p1AttackBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
        ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
        ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
        ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
        ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
        ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

p2HomeBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
        ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
        ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
        ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
        ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
        ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

p2AttackBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
        ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
        ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
        ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
        ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
        ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

await GameLoop()
        
#banana_power