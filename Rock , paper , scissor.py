"""
1- input from user(Rock paper , scissor)
2- computer chose
3- result print

cases
Rock
Rock - Rock = tie
Rock - paper = paper win
Rock - scissor = Rock win


Paper
Paper - Paper = tie
Paper - Rock = Rock win
Paper - scissor = scissor win 


scissor
scissor - scissor = tie
scissor - paper = scissor win
scissor - Rock = Rock win
"""


import random 
game_list = ["Rock" , "Paper" , "Scissor"]

user_choice = input("enter your move = Rock , Paper ,Scissor = ")

computer_choice = random.choice(game_list)

print(f"Userchoice = {user_choice} , computer choice = {computer_choice}") 

if user_choice == computer_choice:
    print(" Both choices are same , match tie")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("computer win")
    else:
        print("you win")

elif user_choice == "rock":
    if computer_choice == "scissor":
        print("you win")
    else:
        print("computer win")


elif user_choice == "Paper":
    if computer_choice == "Rock":
        print("you win")
    else:
        print("computer win")

elif user_choice == "Paper":
    if computer_choice == "scissor":
        print("computer win")
    else:
        print("you win")


elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("computer win")
    else:
        print("you win")

elif user_choice == "scissor":
    if computer_choice == "Paper":
        print("you win")
    else:
        print("computer win")
