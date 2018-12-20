Email = input("please input your Email address: ")
userName = Email[:Email.index("@")]
domainName = Email[Email.index("@"):].strip("@")

def slicerLeftAndRight(Email,userName,domainName):
    finalOutput = "Hello, your username is {0} and your domain name is {1}".format(userName,domainName)
    print(finalOutput)
    return(finalOutput)

def main():
    slicerLeftAndRight(Email,userName,domainName)

if __name__ == "__main__":
    main()
