import random
n = random.randint(1,500)
print("You have 9 guesses")
n_guess=0
while(n_guess<9):
    user_guess = int(input("Enter your guess \n"))
    n_guess=n_guess+1
    print(n_guess,"The number of times you have played the game")
    if user_guess>n:
        print("TRY AGAIN!, your number is bigger than the umber you need to guess")
    elif user_guess<n:
        print("TRY AGAIN!,Your number is smaller than the number you need to guess")
    elif user_guess==n:
        print("Congratulations!You won the game!")
        break
print(n)