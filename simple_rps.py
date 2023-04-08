from random import choice

# Get computer choice

secret = choice(["R", "P", "S"])

# Get player input

guess = ""

while guess not in ['R', 'P', 'S']:
    
    guess = input("Choose [R]ock, [P]aper, or [S]cissors: ")

    guess = guess.upper()

# Check the answer

score = guess + secret

if score == "RS" or score == "PR" or score == "SP":
    print("You win!")
elif score == "SR" or score == "RP" or score == "PS":
    print("You lose!")
else:
    print("It's a draw!")
