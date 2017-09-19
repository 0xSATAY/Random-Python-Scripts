def countLetters(letter,word):
    total = 0
    for i in word:
        if letter == i:
            total += 1
    return total


def displayBlanks(word,lettersGuessedArray):
    stringArray = []
    for i in word:
        stringArray.append("_ ")
    for j in range(len(word)):
        if word[j] in lettersGuessedArray:
            stringArray[j] = word[j]+" "
    string = ""
    for i in stringArray:
        string+=i
    print(string+'\n')


def displayLettersGuessed(lettersGuessed):
    string = "Letters guessed: "
    for i in lettersGuessed:
        string += i + " "
    print(string)

    
def displayMenuOptions():
    print("========================================\nChoose an option:\n1. Start game\n2. Quit game\n")


def displayWelcome():
    print("Welcome to Hangman!")


def enterWord(playerOrGM,*lettersGuessed):
    isValidWord = True
    word = ''
    while True:
        if playerOrGM == 1:
            word = input("Please enter your secret word: ")
        else:
            word = input("Please enter a word or a character: ")
        for i in word:
            if not i.isalpha():
                if playerOrGM == 1:
                    print("Please re-enter a valid word that contains only letters from a-z!")
                else:
                    print("Please re-enter a valid word or letter that contains only letters from a-z!")
                isValidWord = False
        if isValidWord:
            return word
        isValidWord = True


def hangman(playerNames):
    GM = playerNames[0]
    print("\nRules: " + GM + " will be coming up with a secret word that all other players will have to guess\nAll players have only 15 turns total to guess the word else " + GM + " wins.")
    word = enterWord(1)
    parsedWord = parseWord(word)
    playerNames = playerNames[1:]
    lettersGuessed = []
    correctGuesses = []
    turnsLeft = 15
    done = False
    while not done:
        for i in playerNames:
            print("=====================There are " + str(turnsLeft) + " turns left=====================\n")
            print(i + "'s turn:")
            turnsLeft -= 1
            if playerTurn(i,word,lettersGuessed,correctGuesses):
                done = True
                break
            if turnsLeft == 0:
                print("Game over! " + GM + " wins!")
                done = True
                break


def parseWord(word):
    newlst = []
    for i in word:
        if i not in newlst:
            newlst.append(i)
    newlst.sort()
    return newlst


def playerSolve(word,lettersGuessed,correctLetters):
    done = False
    while True:
        while not done:
            displayLettersGuessed(lettersGuessed)
            inpt = enterWord(0)
            if len(inpt) == 1:
                if inpt in lettersGuessed:
                    print("Letter has already been Guessed!")
                else:
                    lettersGuessed.append(inpt)
                    done = True
                    if inpt in word:
                        print("Correct! There are " + str(countLetters(inpt,word)) + " " + inpt + "(s) in the word!")
                        correctLetters.append(inpt)
                        correctLetters.sort()
                        if parseWord(word) == correctLetters:
                            return True
                    else:
                        print("Wrong!\n")
                    return False
            else:
                if inpt == word:
                    return True
                else:
                    print("Wrong!\n")
                    return False


def playerTurn(playerName,word,lettersGuessed,correctGuesses):
    displayBlanks(word,lettersGuessed)
    if playerSolve(word,lettersGuessed,correctGuesses):
        print("\nThe word is " + word)
        print(playerName + " has guessed the word! " + playerName + " wins!\n")
        return True
    else:
        return False


def start():
    displayWelcome()
    displayMenuOptions()
    done = False
    playerNames = []
    while not done:
        option = validateInput("Please enter an option: ",['1','2'])
        if option == '1':
            numOfPlayers = validatePlayerCount("Enter the number of players: ")
            for i in range(numOfPlayers):
                playerName = input("Player " + str(i+1) + "'s name: ")
                playerNames.append(playerName)
            hangman(playerNames)
            displayMenuOptions()
        if option == '2':
            done = True
            print("Quitting...")


def validateInput(question,optionsArray):
    while True:
        inpt = input(question)
        if inpt in optionsArray:
            return inpt
        print("Error! Please enter a valid option")

        
def validatePlayerCount(question):
    while True:
        inpt = input(question)
        if inpt.isdigit():
            if not int(inpt) < 2:
                return int(inpt)
            else:
                print("Please enter a number greater than 1!")
        else:
            print("Please enter a numerical value!")


start()
        
        
