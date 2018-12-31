
#generate your sentence
sentence = "will you go with me to the ball to eat curry?"
#put the word into a list
pigTestList = sentence.split()
vowelList = ("a","e","i","o","u","y")
#check if anywords start with aeiouy

for word in range(len(pigTestList)):
    if pigTestList[word].startswith(vowelList[0:]):
        pigTestList[word] = pigTestList[word] + "yay"

    elif pigTestList[word] != pigTestList[word].startswith(vowelList[0:]):
        if len(pigTestList[word]) > 3:
            #need to take the first two letters and move them to the end of the word
            #the strings within this for loop art strings
            deals = pigTestList[word].lstrip(pigTestList[word][0:2])
            doneDeal = pigTestList[word][0:2]#taken out the first two letters from each word
            finalProduct = deals + doneDeal + "yay"
            pigTestList[word] = finalProduct
