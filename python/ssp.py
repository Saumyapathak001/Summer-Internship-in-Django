guess = 1
trial = 3

print("You will get 3 trials to guess the number")

for i in range(1,trial+1):

    inp = int(input("Guess From 1 to 10 :"))

    if(inp == guess):
        print("Congrats You Guessed It Right")
        break
    elif(inp != guess and i != 3):
        print("Try Again!")

    elif(inp != guess and i == 3):
        print("You Loss!")