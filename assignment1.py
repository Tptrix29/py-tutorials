####### Assignment 1: Triple Combo Game ########

import random

# configuration
flag = True
arr_len = 5
pool_range = 9

# welcome message
print("=============================================")
print("Welcome to the Triple Combo Game!")
print("=============================================")
print("Rule:")
print("Please select number from the pool and earn points by cancelling the 3 combo in the array.\n")

# initialize the game
pool = random.choices([i + 1 for i in range(pool_range)], k=pool_range)
score = 0
arr = []

# game loop
while flag:
    # display the game status
    print(f"\nYour current score is: {score}")
    print("========================================")
    print(f"Your current array is: {" ".join(str(i) for i in arr)} {" ".join("_" for _ in range(arr_len - len(arr)))}")
    print(f"Please select a number from the pool: {pool}")
    print("========================================\n")


    # TODO: complete the game logic here
    ######## START OF YOUR CODE ########


    ######## END OF YOUR CODE ##########

    # check for game over
    if len(arr) == arr_len:
        print("\nYou have reached the maximum number of elements in the array!")
        print("====================================")
        print("Your final score is: ", score)
        print("====================================")
        print("\nGame Over! Thank you for playing!")
        flag = False
        continue

