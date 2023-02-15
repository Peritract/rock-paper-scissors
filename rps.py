from random import choice

def get_computer_choice() -> str:
    """Returns a single-letter choice at random."""
    return choice(['R', 'P', 'S'])

def get_player_choice() -> str:
    """Prompts the player for a single letter;
    keeps prompting until they provide it."""

    # Start with an empty string
    text = ""

    # While the string isn't valid (R, P, S)
    while text not in ['R', 'P', 'S']:
        
        # Demand the user inputs something
        text = input("Choose [R]ock, [P]aper, or [S]cissors: ")

        # Capitalise it for safety
        text = text.upper()

    # Return the valid choice
    return text

def score_game(player, computer):
    """Calculates the winner."""
    score = player + computer
    if score == "RS" or score == "PR" or score == "SP":
        return "player_win"
    elif score == "SR" or score == "RP" or score == "PS":
        return "computer_win"
    else:
        return "draw"

def play():
    computer = get_computer_choice()
    player = get_player_choice()
    result = score_game(player, computer)
    print(f"{player} vs. {computer}")
    if result == "player_win":
        print("You win!")
    elif result == "draw":
        print("It's a draw!")
    else:
        print("You lose!")

if __name__ == "__main__":
    play()