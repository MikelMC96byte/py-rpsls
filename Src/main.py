from random import random
import os
import numpy

PICKS = [
    {
        "name": "ROCK",
        "wins": ["SCISSORS", "LIZZARD"]
    },
    {
        "name": "PAPER",
        "wins": ["ROCK", "SPOCK"]
    },
    {
        "name": "SCISSORS",
        "wins": ["PAPER", "SCISSORS"]
    },
    {
        "name": "LIZZARD",
        "wins": ["PAPER", "SPOCK"]
    },
    {
        "name": "SPOCK",
        "wins": ["SCISSORS", "ROCK"]
    }
]

def clear_console() -> None:
    clear = None
    if(os.name == 'nt'):
        clear = lambda: os.system('cls')
    else:
        clear = lambda: os.system('clear')
    clear()

def wrong_pick() -> int:
    clear_console()
    print("That's not a valid option! Please choose again...")
    return choose(False)

def choose(clear = True) -> int:
    if clear:
        clear_console()
    print("Options:")
    for i in range(0, len(PICKS)):
        print(str(i) + ": " + PICKS[i]["name"])
    pick = input("Please choose an option (number): ")
    try:
        pick = int(pick)
        if pick not in range(0, len(PICKS)):
            return wrong_pick()
        return pick
    except:
        return wrong_pick()

def initial_message() -> None:
    print("WELCOME TO ROCK PAPER SCIZZOR LIZZARD SPOCK...")
    print("MADE BY MikelMC(https://github.com/MikelMC96byte/py-rpsls) UNDER MIT LICENSE")
    print()
    print("LET'S START!!")
    print()

def win(player_pick) -> None:
    global win_counter, loose_counter, game_counter, even_counter
    machine_pick = int(numpy.floor(random() * (len(PICKS) - 1)))
    player_pick = PICKS[player_pick]
    machine_pick = PICKS[machine_pick]
    print("You chose " + player_pick["name"] + " and the machine... ")
    print(machine_pick["name"])
    print()
    if machine_pick["name"] == player_pick["name"]:
        print("...EVEN...")
        even_counter += 1
    elif machine_pick["name"] in player_pick["wins"]:
        print("CONGRATS!! YOW WON!!")
        win_counter += 1
    else:
        print("SORRY... YOUT LOST!!")
        loose_counter += 1
    print()
    print("Games: " + str(game_counter)\
        + " Wins: " + str(win_counter)\
        + " Losts: " + str(loose_counter)\
        + " Even: " + str(even_counter))

def play() -> None:
    global game_counter
    pick = -1
    if game_counter == 0:
        clear_console()
        initial_message()
        pick = choose(False)
    else:
        pick = choose()
    game_counter += 1
    win(pick)
    ask_keep_playing()

def ask_keep_playing() -> None:
    global keep_playing
    print()
    pick = input("Do you want to keep playing? (Y)es/(N)o...... ")
    keep_playing = pick.upper() == 'Y'

keep_playing = True
game_counter = 0
win_counter = 0
loose_counter = 0
even_counter = 0

def main() -> None:
    while keep_playing:
        play()

main()