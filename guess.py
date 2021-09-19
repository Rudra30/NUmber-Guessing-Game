import random
print("Number Guessing Game")
Number = random.randint(1,9)
chances = 0
print("Guess a Number between 1 and 9: ")
while chances < 5 :
    guess = int(input("Enter Your Guess: "))
    if guess == Number:
        print("COnGraTuLaTioNS! You Won")

        break

    elif guess < Number:
        print("Put some oil in your Brain, Guess a number higher than ", guess)

    else: 
        print("Sky isn't the limit, Guess a number lower than ", guess)
    chances += 1

if not chances < 5:
    print("There wasn't enough oil, You Lose!  The number was ", Number)




    
