import random

#the baby will have a list of questions and one will be picked randomly
babyQuestions = ["why is the sky blue?","why do we breath?","why do you play video games all day?"]

#accessing one item from the list randomly
randQuestion=random.choice(babyQuestions)
print(randQuestion)

#you may input an answer if the answer isn't just because
#the baby will keep asking 
yourAnswer = input("well...: ").lower().strip()
while yourAnswer != "just because":
    yourAnswer = input("why: ").lower().strip()
