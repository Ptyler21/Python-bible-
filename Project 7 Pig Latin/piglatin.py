
#generate your sentence
sentence = "will you go with me to the ball to eat curry?"
#put the word into a list
pigTestList = sentence.split()
vowelList = ("a","e","i","o","u","y")
#check if anywords start with aeiouy

for word in pigTestList:
    if word.startswith(vowelList[0:]):

        word = word + "yay"
        print(word)
        
