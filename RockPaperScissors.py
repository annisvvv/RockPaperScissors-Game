import random

print("Welcome to the Rock, Paper, Scissors game")

x = input("click enter to begin to play or any other key to quit the game : ")

while x == "" :
    round = 1
    player_score = 0
    bot_score = 0

    while round < 4 :
        print("\n")
        print(f"********************Round {round}********************")
        round = round + 1

        choice = input("Choose between rock, paper or scissors : ").lower()
    
        items = ["rock", "paper", "scissors"]
        bot_choice = random.choice(items)

        if choice in items :
            
            print(f"Your oponemt choose {bot_choice}.\n")

            if choice == bot_choice :
                print(f"its a tie ... {player_score} - {bot_score}\n")
            elif (choice == "rock" and bot_choice == "scissors") or \
                 (choice == "paper" and bot_choice == "rock") or \
                 (choice == "scissors" and bot_choice == "paper"):
                player_score += 1
                print(f"You won this round! {player_score} - {bot_score}\n")
            else :
                bot_score += 1
                print(f"You lost this round! {player_score} - {bot_score}\n")
        else :
            print("Typo error, try again...")
            round = round - 1
    
    if player_score == bot_score:
         print("It's a tie\n")
    elif bot_score > player_score:
         print("You lose\n")
    else:
         print("Congratulations, you won this game!\n")

    y = input("Do you want to retry (y/n) : ").lower()
    x = "" if y == "y" else 0

print("\n")
input("press enter to exit the game : ")