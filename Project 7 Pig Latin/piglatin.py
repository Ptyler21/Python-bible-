
sentence = input("give me a sentence: ").strip().lower()
pigTestList = sentence.split()
vowelList = ("a","e","i","o","u","y")
for word in range(len(pigTestList)):
    if pigTestList[word].startswith(vowelList[0:]):
        pigTestList[word] = pigTestList[word] + "yay"

    elif pigTestList[word] != pigTestList[word].startswith(vowelList[0:]):
        if len(pigTestList[word]) >= 3:
            firstTwoLetterStrip = pigTestList[word].lstrip(pigTestList[word][0:2]).strip("?!.")
            firstTwoLetterStorage = pigTestList[word][0:2]
            largerThanThreeConcat = firstTwoLetterStrip + firstTwoLetterStorage.rstrip('?') + "yay"
            pigTestList[word] = largerThanThreeConcat
        elif len(pigTestList[word]) < 3:
            firstLetterStorage = pigTestList[word][0]
            secondLetterStorage = pigTestList[word][1]
            twoWordReverse = secondLetterStorage + firstLetterStorage + "yay"
            pigTestList[word] = twoWordReverse

finalSentence = ' '.join(letter for letter in pigTestList)

print(finalSentence)
