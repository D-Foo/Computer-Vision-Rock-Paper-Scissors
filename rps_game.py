from pydoc import resolve
import random

class Rps:

    def __init__(self, choice_list) -> None:
        self.choice_list = choice_list
        self.computer_choice = ''
        self.player_choice = ''
        self.player_score = 0
        self.computer_score = 0
        pass
    
    def play_game(self):
        self.get_choices()
        self.resolve_choices()
        pass

    def play_with_camera_input(self, player_choice):
        self.player_choice = player_choice
        self.computer_choice = random.choice(self.choice_list)
        self.resolve_choices()
        pass
    
    def get_choices(self):
        #Get user input and choose computer choice randomly
        self.computer_choice = random.choice(self.choice_list)
        print("Computer chose " + self.computer_choice)
        player_input = False
        while player_input == False:
            self.player_choice = input("\nPlease enter \'rock\', \'paper\' or \'scissors\'")
            if(self.player_choice in self.choice_list):
                player_input = True
            else:
                print("Invalid Input")
        pass

    def resolve_choices(self):

        print("You chose " + self.player_choice + ". Computer chose " + self.computer_choice + ".")

        if(self.player_choice == self.computer_choice):
            print("Draw")
        elif(self.player_choice == "rock"):
            if(self.computer_choice == "scissors"):
                print("Player Wins")
                self.player_score += 1
            else:
                print("Computer Wins")
                self.computer_score += 1
        elif(self.player_choice == "paper"):
            if(self.computer_choice == "rock"):
                print("Player Wins")
                self.player_score += 1
            else:
                print("Computer Wins")
                self.computer_score += 1
        else:
            if(self.computer_choice == "paper"):
                print("Player Wins")
                self.player_score += 1
            else:
                print("Computer Wins")
                self.computer_score += 1
        pass

    def output_score(self):
        print("Results: ")
        print("Your Score -> " + str(self.player_score) + "  :  " + str(self.computer_score) + " <- Computer Score")
        if(self.player_score == self.computer_score):
            print("Draw")
        elif(self.player_score > self.computer_score):
            print("You Win!")
        else:
            print("Computer Wins!")

if __name__ == "__main__":
    choice_list = ["rock", "paper", "scissors"]
    rps_game = Rps(choice_list)
    rps_game.play_game()