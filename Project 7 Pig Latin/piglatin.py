
#generate your sentence
sentence = "will you go with me to the ball to eat curry?"
#put the word into a list
pigTestList = sentence.split()
vowelList = ("a","e","i","o","u","y")
#check if anywords start with aeiouy

for word in range(len(pigTestList)):
    if pigTestList[word].startswith(vowelList[0:]):
        vowelsFound = pigTestList[word] + "yay"
    elif pigTestList[word] != pigTestList[word].startswith(vowelList[0:]):
        consonantsFound = pigTestList[word]
        #print(type(consonantsFound))
        print(consonantsFound[0])
        print(consonantsFound[1])
        '''
        if len(consonantsFound) > 3:
            #print(consonantsFound,",greater than three letters")
            for i in range(len(consonantsFound)):
                print(consonantsFound[0], ", the first char of the word")
                print(consonantsFound[1], ", the second char of the word")
        '''
        #elif len(consonantsFound) < 3:
            #print(consonantsFound, ", less than three characters")



        #get the index of the words that return true
        #list.index()
        #print(pigTestList.index(word))
        #word = word + "yay"
        #print(word)
