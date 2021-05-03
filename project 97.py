import random

gusses = 0

print("Number gussing game")
print("Guess a number between (0 to 9):- ")


number = random.randint(0,9)


while gusses < 5:
    guess = int(input("Enter your guess:- "))
    
    if(guess == number):
        print(" CONGRATULATIONS You Won!!!  ")
        break
    elif(guess < number):
        print("Your guess was too low:  Please guess a number greater than ",guess)
        gusses = gusses - 1

    elif(guess > number):
        print("Your guess was too high.  Please guess number smaller than ",guess)
        gusses = gusses - 1

    else:
        print("Sorry not able to get it!")

