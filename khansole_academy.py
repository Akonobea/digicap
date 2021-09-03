#Author: Josephine Akonobea Bekoe
#Date: 03.09.2021
#------------------
#import random module for use
import random
#continue asking for answers as long as they are wrong
while True:
    #generate first and second random numbers
 firstRandom = random.randint(10, 99)
 secondRandom = random.randint(10,99)
 #sum up numbers for an answer
 answer = firstRandom + secondRandom
#prompt player for answer to question
 print("What is: " + str(firstRandom) + " + " + str(secondRandom) +"?")
 #read input from command
 userInput = int(input(">> "))
 #approve answer if it matches answer and exit; otherwise continue until correct answer has been reached.
 if userInput == answer:
    print("You are correct!")
    break
 else:
    print("You are wrong!" + "---Correct Answer: " + str(answer))    
