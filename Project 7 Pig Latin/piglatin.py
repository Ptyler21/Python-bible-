
sentence = input("give me a sentence: ").strip().lower()
pigTestList = sentence.split()
vowelList = ("a","e","i","o","u","y")
pigLatinList = list()
for word in pigTestList:
    if word[0] in "aeiou":
        newPigLatinWord = word + "yay"
        pigLatinList.append(newPigLatinWord)
    else:
        #start counting vowels in words
        vowelCounter = 0
        for letter in word:
            #look for letters that are consonants
            if letter not in "aeiou":
                vowelCounter += 1
            #but if you do find a vowel stop
            else:
                break
        consonants = word[:vowelCounter]
        restOfWord = word[vowelCounter:]
        newPigLatinWord = restOfWord + consonants + "ay"
        pigLatinList.append(newPigLatinWord)

finalSentence = ' '.join(letters for letters in pigLatinList)
print(finalSentence)


#finalSentence = ' '.join(letter for letter in pigTestList)

#print(finalSentence)
