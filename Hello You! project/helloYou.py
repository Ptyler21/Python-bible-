
askFirstName = input("Hello, what is your first name?: ")
askLastName = input("Hello, what is your last name?: ")
askAge = input("what is your age?: ")
askCity = input("what city are you from?: ")
askHobby = input("what is a hobby of yours?: ")

def personalQuestions(askFirstName,askLastName,askAge,askCity,askHobby):

    print('Hello there {0} {1}, you are {2} year old from {3} and you enjoy {4}'.format(askFirstName,askLastName,askAge,askCity,askHobby))

def main():
     personalQuestions(askFirstName,askLastName,askAge,askCity,askHobby)

if __name__ == "__main__":
    main()
