import random

wordDataBase = ["downtown", "wound", "queen", "rice", "street", "grip", "flower", "marble", "invention", "branch", "attraction", "metal", "thread", "fowl", "tank", "need", "snakes", "letters", "price", "education", "rabbit", "wilderness", "respect", "doctor", "teeth", "gate", "apparatus", "ear", "desire", "knee", "tramp", "crowd", "arithmetic", "yarn", "loss", "babies", "memory", "thunder", "amusement", "debt", "foot", "pail", "linen", "powder", "drop", "zephyr", "distribution", "measure", "sun", "fall", "anger", "coach", "icicle", "group", "bite", "van", "hate", "chess", "air", "toe", "cellar", "alarm", "earthquake", "match", "sound", "story", "fly", "legs", "baseball","hat", "front", "fear", "condition", "circle", "thought", "top", "dad", "veil", "limit", "pocket", "calculator", "winter", "playground", "basketball", "self", "station", "actor", "dogs", "skin", "acoustics", "talk", "flight", "water", "maid", "wall", "nut", "steam", "advice", "property", "riddle"]

answer = 0
randWord = ""
print("Welcome to Jumbler")
print("The scrambled word is")


def scrambler():
    scrambled = ""
    randWord = wordDataBase[random.randint(0,99)]
    wordLength = len(randWord)
    i = wordLength
    modWord = randWord
    while(i > 0):
        wordLength = len(modWord)
        randPick = random.randint(0,wordLength)
        if(randPick == wordLength):
            randPick -= 1
        if(randPick == wordLength):
            randLetter = modWord[randPick - 1:]
        elif(randPick == 0):
            randLetter = modWord[:randPick + 1]
        else:
            randLetter = modWord[randPick:randPick + 1]
        scrambled += randLetter

        if(randPick == wordLength):
            modWord = modWord[:randPick]
        elif(randPick == 0):
            modWord = modWord[1:]
        else:
            modWord = modWord[:randPick] + modWord[randPick + 1:]
        
        
        i -= 1

    if(scrambled == randWord):
        scrambled()
    print(scrambled)
    
    while(1):
        answer = input("What is the word:")
        if(answer == randWord):
            print("That is correct!")
            replay = input("Would you like to play again (y/n):")
            if(replay == "y"):
                scrambler()
            else:
                print("Thanks for playing!")
                break
        else:
            print("That's incorrect")
        break
scrambler()

        
    

    
