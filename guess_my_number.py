#Author: Josephine Akonobea Bekoe
#Date: 03.08.2021
#import random module
import random
#get random number between 10 and 90
random_number = random.randint(10,90)
#continue taking guesses until player guess matches random_number
while True:
    #prompt user for input
    print("Guess a number: ")
    #read and store user input 
    userGuessed = int(input(">> "))
    #congratulate player if their guess match random number 
    if userGuessed == random_number:
        print("Congrats!")
        break
    #otherwise the user has guessed higher or lower  number than random number 
    elif userGuessed > random_number:
        print("Too Big")
    elif userGuessed < random_number:
        print("Too small")
    
