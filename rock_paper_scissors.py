import random


computer_options = ['r','p','s']

play = 'y'
while(play == 'y'):
    user_input = input("press r for Rock, p for paper, s for scissors: ").lower()
    comp_input = computer_options[random.randint(0,2)]    
    print(f"Computer choose {comp_input}, You choose {user_input}")

    if (user_input == 'r' and comp_input == 's') or (user_input == 's' and comp_input == 'p') or (user_input == 'p' and comp_input == 'r'):
        print("You win, computer loose") 
    elif user_input == comp_input:
        print("Draw")
    else:
        print("computer wins, You loose")
    play = input("Do you like to play again? y/n: ")