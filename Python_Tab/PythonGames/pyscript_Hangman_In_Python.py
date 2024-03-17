#region pyscriptFunctions

from pyscript import document
import asyncio

global sentInput_Hangman
sentInput_Hangman = False

def TerminalPrint_Hangman(text, rgb = [255, 255, 255], end= "<br>"):
    document.querySelector("#outputDisplay_Hangman").innerHTML += (f'<span style="color:rgb({rgb[0]}, {rgb[1]}, {rgb[2]})">{text}</span>{end}')

def TerminalClear_Hangman():
    document.querySelector("#outputDisplay_Hangman").innerHTML = ""

def SendInput_Hangman(other):
    global sentInput_Hangman

    sentInput_Hangman = True

async def TerminalInput_Hangman(prompt = "", rgb = [255, 255, 255]): 
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    global sentInput_Hangman

    sentInput_Hangman = False

    TerminalPrint_Hangman(prompt, rgb, end= "")

    while sentInput_Hangman == False:
        await asyncio.sleep(1)

    sentInput_Hangman = False

    TerminalPrint_Hangman(document.querySelector("#inputString_Hangman").value)

    inputBoxValue = document.querySelector("#inputString_Hangman").value
    document.querySelector("#inputString_Hangman").value = ""

    return inputBoxValue

async def TerminalSleep_Hangman(duration):
    #you have to add await before calling this function cause asyncio stuff, don't mind the errors
    await asyncio.sleep(duration)


#endregion


import random

global acceptableLetters
acceptableLetters = (' a b c d e f g h i j k l m n o p q r s t u v w x y z ').split()

global guess
guess = ""

global word
word = ""

global wordLength
wordLength = 0

global splitWord
splitWord = ""

global guessedLetters
guessedLetters = []

global incorrectLetters
incorrectLetters = []

global misses
misses = 0

global hangmanColor
hangmanColor = [255, 128, 0]

global backgroundColor
backgroundColor = [255, 255, 0]

global guessedLettersColor
guessedLettersColor = [0, 255, 0]

errorColor = [160,32,240]


def Display():


    TerminalPrint_Hangman("<br>")

    TerminalPrint_Hangman("________", backgroundColor)
    TerminalPrint_Hangman("||⠀⠀⠀⠀⠀|", backgroundColor)
    TerminalPrint_Hangman("||⠀⠀⠀⠀⠀", backgroundColor, end = ""); TerminalPrint_Hangman("O", hangmanColor) if misses >= 1 else TerminalPrint_Hangman("")
    TerminalPrint_Hangman("||⠀⠀⠀⠀", backgroundColor, end = "")
    
    if misses >= 2:
        TerminalPrint_Hangman("/", hangmanColor, end = "")

    if misses >=3:
        TerminalPrint_Hangman("|", hangmanColor, end = "")

    if misses >= 4:
        TerminalPrint_Hangman("\⠀", hangmanColor, end = "")

    TerminalPrint_Hangman("")

    TerminalPrint_Hangman("||⠀⠀⠀⠀⠀", backgroundColor, end = ""); TerminalPrint_Hangman("|", hangmanColor) if misses >= 5 else TerminalPrint_Hangman("")
    TerminalPrint_Hangman("||⠀⠀⠀⠀", backgroundColor, end = "")

    if misses >= 6:
        TerminalPrint_Hangman("/", hangmanColor, end = "")
    
    if misses >= 7:
        TerminalPrint_Hangman(" \ ", hangmanColor, end = "")
    
    TerminalPrint_Hangman("")

    TerminalPrint_Hangman("||__",backgroundColor)

    TerminalPrint_Hangman("<br>")


async def GuessInput():
    global guess
    global splitWord
    global guessedLetters
    global acceptableLetters
    global misses

    for i in range(len(word)):

        if guess == splitWord[i] and guess != guessedLetters[i]:

            guessedLetters.pop(i)
            guessedLetters.insert(i, guess)

        TerminalPrint_Hangman(" " + guessedLetters[i] + " ", guessedLettersColor, end= "")
     


    if misses >= 7 or guessedLetters == splitWord:
        pass
    else:

        TerminalPrint_Hangman("<br>")
        guess = await TerminalInput_Hangman("Guess a letter:  ", [0, 0, 255])
        guess = guess.lower()

        if guess.isalpha() == True and len(guess) == 1 and guess in acceptableLetters and guess in splitWord and guess not in incorrectLetters:
            pass

        elif guess.isalpha() == True and len(guess) == 1 and guess in acceptableLetters and guess not in splitWord and guess not in incorrectLetters:
            misses += 1

            incorrectLetters.append(guess)

        elif guess.isalpha() == True and len(guess) == 1 and guess in acceptableLetters and guess not in splitWord and guess in incorrectLetters:
            TerminalClear_Hangman()

            TerminalPrint_Hangman('<br>')

            Display()

            TerminalPrint_Hangman(f"you already guessed {guess}<br>", errorColor)

            await GuessInput()

        else:
            TerminalClear_Hangman()

            TerminalPrint_Hangman('<br>')

            Display()

            TerminalPrint_Hangman(str(guess), backgroundColor, end=""); TerminalPrint_Hangman(" Is Not Valid<br>", errorColor)

            await GuessInput()

async def GameLoop():

    global guessedLetters
    global splitWord

    TerminalClear_Hangman()
    
    if guessedLetters == splitWord or misses >= 7:
        pass
    else:

        Display()

        await GuessInput()

        await GameLoop() 


#game start
async def Start():

    global guess
    global word
    global wordLength
    global splitWord
    global guessedLetters
    global misses
    global hangmanColor
    global backgroundColor
    global guessedLettersColor


    TerminalClear_Hangman()

    word = await TerminalInput_Hangman("<br>Write the word you would like to guess: <br><br>", errorColor)

    word = " ".join(word)
    word = word.lower().split()

    splitWord = [*word]

    for i in range(len(word)):

        if splitWord[i] == " ":
            guessedLetters.append(" ")

        else:
            guessedLetters.append(" __")


    await GameLoop()


    TerminalPrint_Hangman("")

    TerminalClear_Hangman()
    Display()


    if misses >= 7:
        TerminalPrint_Hangman(f'<br>The word was {"".join(word)}', [255, 0, 0])
    else:
        TerminalPrint_Hangman(f'<br>You correctly guessed {"".join(word)}', [0, 255, 0])

    await TerminalInput_Hangman("<br>press send to continue", errorColor)


    while True:

        TerminalClear_Hangman()

        ask = await TerminalInput_Hangman("<br><br>Do You Want To Play Again? ", [0, 0, 255])
        ask = ask.lower()

        if ask == "yes":

            guess = ""
            word = ""
            wordLength = 0
            splitWord = ""
            guessedLetters = []
            misses = 0
            hangmanColor = [255, 128, 0]
            backgroundColor = [255, 255, 0]
            guessedLettersColor = errorColor

            await Start()
        elif ask == "no":
            break
        else:
            pass

await Start()