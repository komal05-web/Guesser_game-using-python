import getpass
def guessers_game():
    print("Welcome to the guesser's game!")
    print("Rules: One player(Chooser) selects a number and other players (Guessers) try to guess")
    print("Let's get started!\n")
    players=[]
    num_players=int(input("Enter the number of players:"))
    for i in range(num_players):
        player_name=input(f"Enter the name of player{i+1}:")
        players.append(player_name)
    print("\n Choose who will be the chooser.")
    chooser=input("Enter the name of the chooser:")
    if chooser not in players:
        print("Invalid player name!Restart the game.")
        return
    print(f"\n{chooser} you will now select a number for others to guess!")
    try:
        secret_number=int(getpass.getpass("Enter the secret number it will be hidden): "))
    except ValueError:
        print("invalid input!Please enter a valid number.Restart the game")
        return
    max_attempts=2
    attempts=0
    winners=[]
    print("\nGuessers,try to guess the number you have 5 attempts.\n")
    while attempts < max_attempts:
        guesses=[]
        print(f"---Rounds {attempts+1}---")    
        for player in players:
            if player!=chooser:   
                try:
                   guess=int(input(f"{player},enter your guess:"))
                except ValueError:
                   print("Invalid Input!Enter a valid number.")
                   guess=None
                guesses.append((player,guess))
        for player,guess in guesses:
            if guess == secret_number:
                winners.append(player)
        if winners:
            print(f"\nCongratulations!The following players guessed the number {secret_number} correctly: {','.join(winners)}")
            return
        print("\n No correct guesses in this round.Moving to the next round.")
        attempts+= 1
    #Step4=End game !No winner-Chooser wins
    if not winners:
        print(f"\nGame over.No one guessed the correct number.The secret number was{secret_number}.")
        print(f"The chooser, {chooser},wins!")
    else:
        print(f"Congratulations to the winner:{','.join(winners)}")        
    print("Thanks for playing!")
#Run the game
if __name__=="__main__":               
    guessers_game()
            

