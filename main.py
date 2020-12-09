import random
import time
from replit import audio

## (C) Felix Yates 2020. More information available in README.md

def drumRoll():
    audio.play_file("drumRoll.mp3")


def cheer():
    audio.play_file("cheer.mp3")


def music():
    global source
    source = audio.play_file("wiiParty.mp3")
    source.volume = 0.25
    source.set_loop(-1)


def leaderboardDisplay():
    with open("leaderboard.txt", "r") as ldbFile:
        ldbFile = ldbFile.readlines()
        print("-" * 10 + "\n")

        print("MOST RECENT SCORES:\n")
        recentScores = []
        for i in range((len(ldbFile) - 6), len(ldbFile)):
            recentScores.append(str(ldbFile[i]))
        for i in range(5, 0, -1):
          y = (i-6)*-1
          entry = str(recentScores[i]).split(",")
          name = str(entry[0]).strip()
          score = str(entry[1]).strip()
          print(f"#{y} {name}: {score}\n")

        print("-" * 10 + "\n")

        print("TOP SCORES:\n")
        entries = []
        for x in range(len(ldbFile)):
          entries.append(str(ldbFile[x]))
          entries[x] = str(entries[x]).split(',')
          entries[x][1] = int(str(entries[x][i]).strip())
        leaderboard = [tuple(x) for x in entries]
        leaderboard.sort(key=lambda tup: tup[1],reverse=True)
        for i in range(5):
          score = int(str(leaderboard[i][1]).strip())
          print(f"#{i+1} {leaderboard[i][0]}: {str(score)}\n")

        print("-" * 10 + "\n")

def auth(playerNumber):
    valid = False
    with open("players.txt", "r") as playerfile:
        players = playerfile.readlines()
        player = str(players[playerNumber - 1]).split(',')
    for i in range(len(player)):
        player[i] = str(player[i]).strip()
    print(
        "Please enter the username for Player",
        str(playerNumber) + ": ",
        end="")
    usernameInput = input()
    passwordInput = input("And now the password: ")
    print("\n")
    username = str(player[0])
    password = str(player[1])
    while valid != True:
        if (usernameInput == username) and (passwordInput == password):
            valid = True
            break
        else:
            if usernameInput != username:
                usernameInput = input("Username incorrect. Please try again: ")
            if passwordInput != password:
                passwordInput = input("Password incorrect. Please try again: ")

"""def account(playerNumber):
  valid = False
  exists = True
  answer = input(f"Welcome, Player {playerNumber}! Do you have an account? (Y/N) ")
  """



def tutorialQuestion():
    music()
    time.sleep(2)
    print("\nWelcome to un-named dice rolling game!")
    time.sleep(2)
    print(
        "Here's a quick look at the leaderboard. I hope you'll be beating these scores!\n"
    )
    time.sleep(2)
    leaderboardDisplay()
    time.sleep(5)
    answer = input(
        "Final thing - would you like to go through the tutorial? (Y/N) "
    ).lower()

    if answer == "y" or answer == "yes":
        tutorial()
    elif answer == "n" or answer == "no":
        print("Alright then, let's get this show on the road!")
        time.sleep(1.5)
    else:
        valid = False
        while valid == False:
            answer = input(
                "Invalid - please enter either 'Y' or 'N': ").lower()
            if answer == "y" or answer == "yes":
                valid = True
                tutorial()
            elif answer == "n" or answer == "no":
                valid = True
                print("Alright, let's get this show on the road!")
                time.sleep(1.5)

def tutorial():
    with open("tutorial.txt", 'r') as file:
        print("\n")
        tutorial = file.readlines()
        for i in range(len(tutorial)):
            tutorial[i] = str(tutorial[i])
            print(str(tutorial[i]), end="")
            time.sleep(5)
            i += 1
    print("\n")

def game():
    rounds = 0
    p1Score = 0
    p2Score = 0

    while rounds < 5:
        p1Score = roll(1, p1Score)
        p2Score = roll(2, p2Score)
        rounds = rounds + 1
        if rounds < 5:
            time.sleep(2)
            print("\nThat's the end of round",
                  str(rounds) + "!" + "\nSo far, Player 1 has", str(p1Score),
                  "and Player 2 has",
                  str(p2Score) + "!")
            time.sleep(2.5)
            print("Now, on with round", str(rounds + 1) + ".")
            time.sleep(1)

    time.sleep(1)
    print("\nThat's the game! Let's take a look at those scores, shall we?\n")
    gameEnd(p1Score, p2Score)

def roll(currentPlayer, score):
    i = currentPlayer
    print("\nPlayer", str(i) + ", you're up! Press ENTER to roll.", end=" ")
    input()
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("\nYou rolled", str(dice1), "and",
          str(dice2) + ", meaning that", str(dice1 + dice2),
          "was added to your score!")
    score = score + dice1 + dice2
    time.sleep(2)

    if ((dice1 + dice2) / 2) == ((dice1 + dice2) // 2):
        print("The total was even! Score increased by 10.")
        score = score + 10
        time.sleep(2)
    else:
        if score >= 5:
            score = score - 5
            print("But wait, the total was odd! Score decreased by 5.")
            time.sleep(2)
        elif score < 5:
            score = 0
            print(
                "The total was odd, but as your score was below 5 you were only reset to 0."
            )
            time.sleep(2)

    if dice1 == dice2:
        dice1 = random.randint(1, 6)
        score = score + dice1
        print("You rolled double, and rolled again - adding", str(dice1),
              "to your score!")
        time.sleep(2)
    return score

def gameEnd(p1Score, p2Score):
    time.sleep(2.5)
    if p1Score != p2Score:
        print("Player 1 got...  ", end="")
        source.set_paused(True)
        drumRoll()
        time.sleep(5)
        print(str(p1Score) + ".\n")
        print("Player 2 got...  ", end="")
        drumRoll()
        time.sleep(5)
        print(str(p2Score) + ".\n")
        time.sleep(1)
        tieChk(p1Score, p2Score)
        if p1Score > p2Score:
            winner = 1
        else:
            winner = 2
        print("Congratulations Player " + str(winner) + ", you won!\n")
        cheer()

    leaderboard(winner, p1Score, p2Score)

    time.sleep(10)
    input("\nThanks for playing, I hope you had fun!\nPress ENTER to exit. ")
    time.sleep(3)

def tieChk(p1Score, p2Score):
    tie = False
    if p1Score == p2Score:
        print(
            "Will you look at that, it's a tie! You'll have to roll again until one of you gets the higher score."
        )
        tie = True

    while tie == True:
        p1Score = roll(1, p1Score)
        p2Score = roll(2, p2Score)

        if p1Score == p2Score:
            tie == True
            print("Another tie, another round!\n")
        else:
            tie == False
            print("Ok, the tie's been broken. Back to the scoreboard!")
            gameEnd(p1Score, p2Score)

def leaderboard(winner, p1Score, p2Score):
    print("Congrats Player", str(winner) + "!")
    print("To put your scores on the scoreboard, I need your names...")
    player1 = input("Player 1, what I am I putting your score under? ")
    player2 = input("What about you, Player 2? ")
    with open("leaderboard.txt", "a") as ldbFile:
        ldbFile.write(player1 + "," + str(p1Score) + "\n")
        ldbFile.write(player2 + "," + str(p2Score) + "\n")
        print("Thanks! They've been added to the leaderboard.")

## MAIN CODE

for i in range(2):
    auth((i + 1))
print("Correct! On with the game :)")
tutorialQuestion()
game()