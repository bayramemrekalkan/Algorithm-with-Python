
#! Randomly generate a 4-digit number with different digit values (number can start with zero).

#! Ask the user to guess a 4-digit number.

#! For every digit that the user guessed correctly in the correct place, they have a "cow".

#! For every digit the user guessed correctly in the wrong place is a "bull".

#! Every time the user makes a guess, tell them how many "cows" and "bulls" they have.

#! Once the user guesses the correct number, the game is over.

#! Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

#! Say the number generated by the computer is 1570. An example interaction could look like this 👇

# Welcome to the Cows and Bulls Game!

# Enter a number:

# >>> 1274

# 2 cow, 0 bull

# >>> 1256

# 1 cow, 1 bull

#? SOLUTION:

#* The enumerate() function 👉 takes a collection (e.g. a tuple) and returns it as an enumerate object.

#* The enumerate() function adds a counter as the key of the enumerate object.

#* Syntax >>> enumerate(iterable, start)

#iterable >	An iterable object
#start	  > A Number. Defining the start number of the enumerate object. Default 0

#* The sample() method 👉 returns a list with a randomly selection of a specified number of items from a sequnce.

#* Note: This method does not change the original sequence.

#* Syntax >>> random.sample(sequence, k)

# sequence  >	Required. A sequence. Can be any sequence: list, set, range etc.
# k         >	Required. The size of the returned list

import random

number = "".join(random.sample("0123456789",4))

cow, bull = 0,0

while cow < len(number):
    guess = input("Enter a 4 digit number: ")

    cow, bull = 0,0
    count = 0

    for ind, i in enumerate(guess):
        if i in number:
            if ind == number.index(i):
                cow += 1
            else:
                bull += 1
    count += 1
    print(f"{guess} has {cow} cow, {bull} bull.")

print(f"Congrats! Number of try: {count}")

