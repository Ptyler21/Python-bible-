
nameList = ["jason","stephan","joseph","phillip"]
def mainList():
    while True:
        userName = input("Hello please give me a name: ")
        if nameList.count(userName) == 0:
            print("no entry in database")
            print(nameList)
            userNameAdd = input("would you like to add the name?(y/n): ")
            if "y" == userNameAdd:
                print("adding name...")
                nameList.append(userName)
                print("the name has been added!")
                print(nameList)
            elif "n" == userNameAdd:
                pass
        elif nameList.count(userName) >= 1:
            print("the name is in the database!")
            print(nameList)
            userInput = input("would you like to delete it?(y/n): ")
            if "y" == userInput:
                print("deleting name from list")
                nameList.remove(userName)
                print("name deleted....")
                print(nameList)
            elif "n" == userInput:
                pass
def main():
    mainList()


if __name__=="__main__":
    main()
