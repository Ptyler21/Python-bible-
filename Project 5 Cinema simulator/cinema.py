movieDictionary = {
    "Xillia":{"age":18,"seats":0},
    "Xillia2":{"age":18,"seats":10},
    "Berseria":{"age":22,"seats":3},
    "Witcher3":{"age":18,"seats":4}
}

while True:

    userMovieChoice = input("please give me a movie: ")
    userAge = int(input("please give me a number: "))

    if userAge < movieDictionary[userMovieChoice]["age"]:
        print("sorry you cannot watch this movie, please pick another")

    elif userAge >= movieDictionary[userMovieChoice]["age"] and movieDictionary[userMovieChoice]["seats"] == 0:
        print ("sorry there are not enough seats, please pick another movie")

    else:
        print("Please enjoy the movie")
