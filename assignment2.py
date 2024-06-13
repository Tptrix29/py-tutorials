####### Assignment 2: Rewrite Triple Combo Game with class ########

import random


class TripleComboGame:
    def __init__(self, arr_len=5, pool_range=9):
        """Initialize the game with default values"""
        self.arr_len = arr_len
        self.pool_range = pool_range
        self.flag = True
        self.score = 0
        self.arr = []
        self.pool = random.choices([i + 1 for i in range(pool_range)], k=pool_range)

    def welcome(self):
        """Display the welcome message"""
        print("=============================================")
        print("Welcome to the Triple Combo Game!")
        print("=============================================")
        print("Rule:")
        print("Please select number from the pool and earn points by cancelling the 3 combo in the array.\n")

    def display_status(self):
        """Display the game status"""
        print(f"\nYour current score is: {self.score}")
        print("========================================")
        print(f"Your current array is: {' '.join(str(i) for i in self.arr)} {' '.join('_' for _ in range(self.arr_len - len(self.arr)))}")
        print(f"Please select a number from the pool: {self.pool}")
        print("========================================\n")

    def game_over(self):
        """Display the game over message"""
        print("\nYou have reached the maximum number of elements in the array!")
        print("====================================")
        print("Your final score is: ", self.score)
        print("====================================")
        print("\nGame Over! Thank you for playing!")

    def input_validation(self):
        """Get a valid input from the user"""
        # TODO: complete the input validation logic here
        ####### START OF YOUR CODE ########

        ######## END OF YOUR CODE #########

    def update_array(self, choice):
        """update the array and check for combo"""
        # TODO: complete the update array logic here
        ####### START OF YOUR CODE ########

        ######## END OF YOUR CODE #########

    def update_pool(self, choice):
        """remove the selected number from the pool and add a new number to the pool"""
        # TODO: complete the update pool logic here
        ####### START OF YOUR CODE ########

        ######## END OF YOUR CODE #########

    def check_game_over(self):
        """Check for game over condition"""
        # TODO: complete the game over logic here
        ####### START OF YOUR CODE ########

        ######## END OF YOUR CODE #########

    def start_game(self):
        """Start the game loop"""
        self.welcome()
        while self.flag:
            self.display_status()
            choice = self.input_validation()
            self.update_array(choice)
            self.update_pool(choice)
            self.check_game_over()


if __name__ == "__main__":
    # create an instance of the game
    game = TripleComboGame()
    # start the game loop
    game.start_game()
