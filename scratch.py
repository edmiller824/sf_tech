
f_list = []
curr = 0
new = 1
tot = 1

i = 0
n = 5

for i in range(5):
    f_list.append(tot)
    tot = curr + new 
    curr = new 
    new = tot 

print(f_list)



# h = "hello"
# print(h)

# print('hi')


# import pandas as pd

# mhd = pd.read_csv("sf_datasets/mental_health_dataset.csv")
# mhd.columns = mhd.columns.str.lower()

# # print(mhd.occupation.value_counts().idxmax)

# # # [1] get total number of records
# # print(mhd.describe())



# # # -- [2] determine number of occupations count of users in each
# occ_count = pd.DataFrame(mhd.occupation.value_counts().reset_index())
# # print(occ_count)
# # print(occ_count.idxmax())
# idmin = occ_count.idxmin()

# print(idmin)

# print(occ_count.loc[idmin,:])

# print((occ_count[idmin], index == "occupation"))

# -- [3] get occupations with greatest and least number of users

# mhd.occupations.idxmax



# /Users/emiller/Downloads/mental_health_dataset.csv

# # In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
# # This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. 
# # The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# # At the end of this exchange, your program should print out how many guesses it took to get your number.


# # user input a number

# import random

# user_num = int(input("pick an integer between 0 and 100: "))
# user_feedback = ""

# first_guess_min = random.randint(0, 99)
# first_guess_max = random.randint(first_guess_min, 100)
# last_guess = (first_guess_min + first_guess_max) // 2

# prog_num = (first_guess_min + first_guess_max) // 2

# guess_min = 0
# guess_max = 100

# if prog_num == user_num:
#     print(f"nailed it on the first try - your number was {user_num}!")

# while user_num != prog_num:
#     user_feedback = input(f"program guesses {prog_num}. too high or too low? ")
#     last_guess = prog_num
#     if user_feedback == "too high":
#         guess_max = prog_num
#         prog_num = (last_guess + guess_min) // 2
#     elif user_feedback == "too low":
#         guess_min = prog_num
#         prog_num = (last_guess + guess_max) // 2
#     else:
#         user_feedback = input("hmmm...what was that? too high or too low? ")
    
# print(f"got eeeem! your number was {user_num}!")




# # Create a program that will play the “cows and bulls” game with the user. The game works like this:

# # Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# # For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# # For every digit the user guessed correctly in the wrong place is a “bull.” 
# # Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# # Once the user guesses the correct number, the game is over.
# #  Keep track of the number of guesses the user makes throughout the game and tell the user at the end.


# # create 4 digit number as a list of 4 digits (while loop with append)
# import random
# rand_list = []
# user_list = []

# # generate a 4 digit number
# for num in range(4):
#     rand_list.append(str(random.randint(0, 9)))

# rand_num = "".join(rand_list)

# user_num = input("Enter a 4-digit number: ")

# for u in str(user_num):
#     user_list.append(u)


# while rand_list != user_list:
#     cow_count = 0
#     bull_count = 0
#     user_list = []
#     for u in str(user_num):
#         user_list.append(u)

#     for i in range(4):
#         if rand_list[i] == user_list[i]:
#             cow_count += 1

#         elif rand_list[i] != user_list[i]:
#             bull_count += 1
#     if cow_count == 4:
#         print(f"you got it, the number was {rand_num}")
#         break
#     if cow_count < 4:
#         user_num = input(f"{cow_count} cows and {bull_count} bulls. keep that same energy. Enter a 4-digit number: ")







# # Make a two-player Rock-Paper-Scissors game. 
# # (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
# # and ask if the players want to start a new game)

# # Remember the rules:

# # Rock beats scissors
# # Scissors beats paper
# # Paper beats rock

# choices = ["rock", "paper", "scissors"]

# player_1 = input("player one - shoot: ").lower()
# while player_1 not in choices:
#     player_1 = input("ONLY rock, paper, or scissors. player one - shoot: ")

# player_2 = input("player two - shoot: ").lower()
# while player_2 not in choices:
#     player_2 = input("ONLY rock, paper, or scissors. player two - shoot: ")

# while player_1 != "quit" or player_2 != "quit":
#     if player_1 == "quit" or player_2 == "quit":
#         break
#     elif player_1 == player_2:
#         player_1 = input("DRAW! let's play again. player 1 - shoot: ")
#         if player_1 == "quit":
#             break
#         player_2 = input("player 2 - shoot: ")
#         if player_2 == "quit":
#             break
# # the part above works!
#     elif (player_1 == "rock" and player_2 == "scissors") or (player_1 == "paper" and player_2 == "rock") or (player_1 == "scissors" and player_2 == "paper"):
#         player_1 = input("PLAYER 1 WINS! let's play again. player 1 - shoot: ")
#         if player_1 == "quit":
#             break
#         player_2 = input("player 2 - shoot: ")
#         if player_2 == "quit":
#             break

#     else:
#         player_1 = input("PLAYER 2 WINS! let's play again. player 1 - shoot: ")
#         if player_1 == "quit":
#             break
#         player_2 = input("player 2 - shoot: ")
#         if player_2 == "quit":
#             break

    




# # Write a program (using functions!) that asks the user for a long string containing multiple words. 
# # Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

# string_input = "They call me big Elly"

# string_list = string_input.split()

# rev = [word for word in reversed(string_list)]

# print(rev)
 



# # Generate a random number between 1 and 9 (including 1 and 9). 
# # Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

# # Extras:

# # Keep the game going until the user types “exit”
# # Keep track of how many guesses the user has taken, and when the game ends, print this out.

# import random
# rand_num = random.randint(1, 9)
# user_num = input("Enter a number between 1 and 9 (inclusive): ")
# counter = 0

# while (user_num != rand_num and user_num != "exit"):
#     if str(user_num) == "exit":
#         print("exiting program")
#         break
#     elif int(user_num) == rand_num:
#         if counter == 0:
#             print(f"that's it! the number was {rand_num}. nailed it on the first try")
#         elif counter == 1:
#             print(f"that's it! the number was {rand_num}. it took {counter} try")
#         else:
#             print(f"that's it! the number was {rand_num}. it took {counter} tries")
#         break
#     elif int(user_num) > 9 or int(user_num) < 1:
#         user_num = input("nah, BETWEEN 1 and 9. enter a number between 1 and 9, inclusive: ")
#     elif int(user_num) < rand_num:
#         counter += 1
#         if counter == 1:
#             user_num = input(f"too low, try again - that's {counter} try. enter a number between 1 and 9, inclusive: ")
#         else:
#             user_num = input(f"too low, try again - that's {counter} tries. enter a number between 1 and 9, inclusive: ")
#     elif int(user_num) > rand_num:
#         counter += 1
#         if counter == 1:
#             user_num = input(f"too high, try again - that's {counter} try. enter a number between 1 and 9, inclusive: ")
#         else:
#             user_num = input(f"too high, try again - that's {counter} tries. enter a number between 1 and 9, inclusive: ")


    




# # write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# # Make sure your program works on two lists of different sizes.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# common_list = []
# for num in a:
#     if (num in b) and (num not in common_list):
#         common_list.append(num)
#     else:
#         common_list = common_list

# print(common_list)


# # Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# # Hint: how does an even / odd number react differently when divided by 2?

# # Extras:

# # If the number is a multiple of 4, print out a different message.
# # Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# # If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
# user_num = []

# input_number = input("enter 2 integers, separated by spaces: ").split()

# for i in input_number:
#     i = int(i)
#     if (i % 2 == 0) and (i % 4 == 0):
#         print("even and divisible by 4")
#     elif i % 2 == 0:
#         print("even")
#     else:
#         print("odd")


# # get all numbers divisible by 3, 5, and both 3 and 5, between 24 and 50...
# # store in separate lists:
# div_3 = []
# div_5 = []
# div_3_5 = []

# for n in range(24,50):
#     if n % 3 == 0:
#         div_3.append(n)
#     if n % 5 == 0:
#         div_5.append(n)
#     if (n % 3 == 0) and (n % 5 == 0):
#         div_3_5.append(n)

# print(div_3)
# print(div_5)
# print(div_3_5)
# div_5
# store in dictionary, with indices being what they are divisible by:


# div_list = [3,5,7,9]
# div_dict = {}

# # # function that outputs a list of numbers between 24 and 50 that are divisible by div_list
# def some_output(div_list):
#     div = []
#     for n in range(24,51): 
#         if n % div_list == 0:
#             div.append(n)  
#         else:
#             div = div  
#     return div


# for dd in div_list:
#     output = some_output(dd)
#     div_dict[dd] = output

# print(div_dict)


# ===================================================

# total of hands 1 and 2
# numeric values are themselves
# values to face cards = 10
# value of aces...assign as 1

# if total values of cards <= 11, and there is at least 1 ace, add 10 to total

# compare hands


# =================== get value of 1 hand in blackjack =================================
# # hand_list = ["A","3"]

# # hand_list = [["A", "A", 3],["Q", 5, 7]]
# hand_list = [["J","A"], ["3"]]

# def bj_function(h):
#     total = []
#     hand_value = []
#     for c in h:
#         if c in ["J", "Q", "K"]:
#             hand_value.append(10)
#         elif c == "A":
#             hand_value.append(1)
#         else:
#             # c = map(int, c)
#             hand_value.append(int(c))
#     sub_total = sum(hand_value)

#     if sub_total <= 10 and ("A" in h):
#         total = sub_total + 10
#     else:
#         total = sub_total
#     return total

# # print(bj_function(hand_list))
# # get totals of hands, output in a list
# hand_nums = []
# for hds in hand_list:
#     nums = bj_function(hds)
#     hand_nums.append(nums)


# # remove hands that are over 21 - busted

# no_bust_hands = []
# for val in hand_nums:
#     if val <= 21:
#         no_bust_hands.append(val)
#     else:
#         no_bust_hands = no_bust_hands
    
# winning_score = max(no_bust_hands)

# print(hand_nums)
# print("winning score: " + str(winning_score))
# print(hand_nums[0] == winning_score)

# =================== get value of multiple hands, in separate lists =================================

# =================== get value of 1 hand in blackjack =================================

# hand_1 = ['10', '7']
# hand_2 = ['8', '3', 'A', '5']

# # hand_1.append(hand_2)
# hand_list = [hand_1, hand_2]

# def bj_function(h):
#     total = []
#     hand_value = []
#     for c in h:
#         if c in ["J", "Q", "K"]:
#             hand_value.append(10)
#         elif c == "A":
#             hand_value.append(1)
#         else:
#             # c = map(int, c)
#             hand_value.append(int(c))
#     sub_total = sum(hand_value)

#     if sub_total <= 11 and ("A" in h):
#         total = sub_total + 10
#     else:
#         total = sub_total
#     return total

# # print(bj_function(hand_list))
# # get totals of hands, output in a list
# hand_nums = []
# for hds in hand_list:
#     nums = bj_function(hds)
#     hand_nums.append(nums)


# # remove hands that are over 21 - busted

# no_bust_hands = []
# for val in hand_nums:
#     if val <= 21:
#         no_bust_hands.append(val)
#     else:
#         no_bust_hands = no_bust_hands
    
# no_bust_hands.append(0)    
# winning_score = max(no_bust_hands)

# print(hand_nums)
# print("winning score: " + str(winning_score))
# print((hand_nums[0] == winning_score) and (hand_nums[1] != winning_score))



# get prime numbers less than 20...

      

