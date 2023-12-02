favourite_fruits = ["pineapple", "apple", "watermelon", "grapes", "tangerine", "orange"]

if favourite_fruits != favourite_fruits:
    print("My hated fruits are", favourite_fruits)
else:
    print("My favourite fruits are", favourite_fruits)

sentence = input("Enter a sentence:")
words = sentence.split()
for word in words:
    print(f"{word}: len{word}")

numbers = [2, 4, 6, 8, 10, 12]
total = 0
for num in numbers:
    total += num

    print("Sum of numbers:", total)

import random

random_number = random.randint(1, 20)
guess = 0

while guess != random_number:
    guess = int(input("Guess the number (between 1 and 20): "))
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

password = "Emotions"

while True:
    user_input = input("Enter your password please:")
    if user_input == password:
        print("Correct. Welcome Ms Souza!")
        break
    else:
        print("No hackers! If you are one, hmmmmmm")
    
countdown_number = int(input("Enteer countdown munber please:"))

while countdown_number > 0:
    print(countdown_number)
    countdown_number -=1
print("Lets fly boys and girls!")