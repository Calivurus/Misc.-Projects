Number = "50"
Guess = input("Guess the number! ")
if Guess < Number:
    print("Your guess is too low!")
elif Guess > Number:
    print("Your guess is too high!")
else:
    print("Correct!")