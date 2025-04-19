import random

print("------ GUESS THE NUMBER GAME ------\n")

first_number = input("First, enter a number:\n")
second_number = input("\nNext, enter a number that is greater\n than the number you just entered:\n")

random_number = random.randint(int(first_number), int(second_number))

print("\nA random number was generated within the range of the two numbers you entered.")
guess_number = input("Enter the number by guessing the generated random number:\n")

if random_number == int(guess_number):
    print("\nThat's right! The answer is " + str(random_number) + ".")

while random_number != int(guess_number):
    guess_number = input("\nThat's incorrect. Try again:\n")
    
    if random_number == int(guess_number):
        print("\nThat's right! The answer is " + str(random_number) + ".")
