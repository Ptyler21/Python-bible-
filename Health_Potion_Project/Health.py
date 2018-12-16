#!/usr/bin/python3
import random

easyHealthAmount = random.randint(10,15)
mediumHealthAmount = random.randint(5,9)
hardHealthAmount = random.randint(1,4)
charHealth = int(input("give me a number for the health please: "))
gameDifficulty = str(input("what is the difficulty(easy, medium, hard): "))

finalHealth = int()
def character(charHealth,gameDifficulty):



    if "easy" == gameDifficulty:

        print(charHealth, "This is the current health value")
        return(charHealth + easyHealthAmount)
    elif "medium" == gameDifficulty:
        print(charHealth, "This is the current health value")
        return(charHealth + mediumHealthAmount)

    elif "hard" == gameDifficulty:
        print(charHealth, "This is the current health value")
        return(charHealth + hardHealthAmount)

    #determine variable type
    #print(type(charHealth))
def main():
    print (character(charHealth,gameDifficulty))

if __name__ == "__main__":
    main()
