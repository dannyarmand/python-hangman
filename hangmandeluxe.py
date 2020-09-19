#merge fara ascii
import random

capitals = ["kabul","buenos aires", "viena", "chisinau","monaco","amsterdam","minsk","sarajevo","oslo","beijing","lima","zagreb","bogota","lisbon","prague","bucharest","moscow","copenhagen","islamabad","paris","helsinki","caracas"]
citys =["kenya","jamaica","japan","kuwait","luxembourg","vietnam","zimbabwe","india","italy","israel","somalia","france","slovenia","germany","greece","syria","belgium","brazil","romania","argentina","austria","mexico","moldova"]
playGame = True
category = ""
userGuesstList = []
user_guesses = []
def display_hangman(lives):


    stages = [  """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]

    return stages[lives]

    #meniu
level = input(" Welcome! Choose difficulty level:(easy- E/medium - M/hard-H)")
while True:
    if level.upper() == "E":
        lives = 7
        print("Level Easy! You have 7 lives")
        break
    elif level.upper() == "M":
        lives = 6
        print("Level Medium! You have 6 lives")
        break
    elif level.upper() == "H":
        lives = 4
        print("Level hard! You have 4 lives")
        break
    else :
        print("Wrong Value!")
        level = input(" Welcome! Choose difficulty level:(easy- E/medium - M/hard-H)")
        break


     #Choosing the Secret word
while True:
        if category.upper() == "1":
          
            Word = random.choice(capitals)
            break
        elif category.upper() == "2":
          
            Word = random.choice(citys)
            break
        else:
            category = input("Please select a valid categary: 1 for Capitals /2 for city ; X to exit")

        if category.upper() == 'X':
            print("Bye. See you next time!")
            playGame = False
            break

if playGame:
    WordList = list(Word)

    def printG_Leters():
        print("".join(userGuesstList))
    for n in WordList:
        userGuesstList.append("_ ")
    printG_Leters()

    while True:    
        print("Guess a letter:")
        letter =input()

        if letter in user_guesses:
            print("you already guessed this, try again!")
        else:
                
                user_guesses.append(letter)
                if letter in WordList:
                    print("Nice!")
                    if lives > 0:
                        print("You have ", lives, 'lives left!')
                    for i in range(len(WordList)):
                        if letter == WordList[i]:
                            letterIndex = i
                            userGuesstList[letterIndex] = letter.upper()
                    printG_Leters()

                else:
                    lives -= 1
                    print("WRONG! Try again.")
                    print(display_hangman(lives))
                    if lives > 0:
                        print("You have ", lives, 'lives left!')
                    printG_Leters()
        joinedList = "".join(userGuesstList)
        if joinedList.upper() == Word.upper():
            print("WINER")
            break
        elif lives == 0:
            print("You LOSE!")
            print("Your word was: "+Word.upper())
            break
    continue_game = input("q to quit")
    if continue_game == "q":
        print("Bye Bye!!")
    else:
        print("enter valid input")
        continue_game = input("q to quit")
        print("Bye Bye!!")
        
    playGame = False

    
                      
       

                    
