import random
import time
from replit import audio

# These are global sleep timings. Change these to 0 when testing.
# Default values can also be found below to change back to.

global ssSleep  # supershort sleep, default - 1.5 seconds
global sSleep  # short sleep, default - 2 seconds
global mSleep  # medium sleep, default - 5 seconds
global lSleep  # long sleep, default - 8 seconds
ssSleep = 1.5
sSleep = 2
mSleep = 5
lSleep = 8

# This is the amount of rounds you want to play
# The default (and project requirement) is 5, but you can lower it to speed up the game.
## WARNING: IT WILL PROBABLY BREAK STUFF!

global totalrounds
totalrounds = 5

# Audio functions

def drumRoll():
    try:
        audio.play_file("drumRoll.mp3")
    except TimeoutError:
        pass


def cheer():
    try:
        audio.play_file("cheer.mp3")
    except TimeoutError:
        pass


def music():
    try:
        global source
        source = audio.play_file("wiiParty.mp3")
        audio.play_file("cheer.mp3")
        source.volume = 0.25
        source.set_loop(-1)
    except TimeoutError:
        pass

# Game functions

def leaderboardDisplay(): # Reads, sorts, and then displays the leaderboard
    with open("leaderboard.txt", "r") as ldbFile:
        ldbFile = ldbFile.readlines()
        print("-" * 10 + "\n")

        print("MOST RECENT SCORES:\n")
        recentScores = []
        for i in range((len(ldbFile) - 6), len(ldbFile)):
            recentScores.append(str(ldbFile[i]))
        for i in range(5, 0, -1):
            y = (i - 6) * -1
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
        leaderboard.sort(key=lambda tup: tup[1], reverse=True)
        for i in range(5):
            score = int(str(leaderboard[i][1]).strip())
            print(f"#{i+1} {leaderboard[i][0]}: {str(score)}\n")

        print("-" * 10 + "\n")


def auth(playerNumber): # Player authentication
    valid = False
    exists = False
    print(f"Enter your username, Player {playerNumber}.")
    usernameInput = input("If you do not have an account, pick a username instead: ")
    players = getPlayers()
    exists = doesExist(usernameInput)
    if exists == False:
        while exists == False:
            createAccount = input(
                f"\nThat account ({usernameInput}) does not exist.\nWould you like to create a new account? (Y/N) "
            ).lower()
            createAccount = isValid(createAccount)
            if createAccount == True:
                exists = True
                print("\n")
                accountCreator(playerNumber)
            elif createAccount == False:
                exists = True
                print("\n")
                auth(playerNumber)

    players = getPlayers()

    for i in range(len(players)):
        if str(players[i][0]) == usernameInput:
            username = usernameInput
            password = str(players[i][1])

    if playerNumber == 1:
        global p1Username
        p1Username = username
    elif playerNumber == 2:
        global p2Username
        p2Username = username

    passwordInput = input("Now enter the password: ")
    while valid != True:
        if (usernameInput == username) and (passwordInput == password):
            valid = True
            break
        else:
            if usernameInput != username:
                usernameInput = input("Username incorrect. Please try again: ")
            if passwordInput != password:
                passwordInput = input("Password incorrect. Please try again: ")


def getPlayers(): # Grabs playerlist from 'players.txt', appends to 'players' list
    players = []
    with open('players.txt', 'r') as existingPlayers:
        existingPlayers = existingPlayers.readlines()
        for i in range(len(existingPlayers)):
            players.append(str(existingPlayers[i]).split(","))
            players[i][1] = players[i][1].strip()
    return players


def doesExist(usernameInput): # Checks whether a player exists within the 'players' list
    exists = False
    players = getPlayers()
    for i in range(len(players)):
        if str(players[i][0]) == usernameInput:
            exists = True
            return True

    if exists == False:
        return False


def accountCreator(playerNumber): # Creates an account for the player
    loop = True
    valid = False
    print("I'll get one set up for you right away.")
    time.sleep(sSleep)
    newUsername = input(
        "\nFirst, pick a username.\nRemember, this will appear on the leaderboard, so keep it clean! "
    )

    while loop != False:
        exists = doesExist(newUsername)
        if exists == True:
            newUsername = input(
                f"Uh oh, that username ({newUsername}) already exists. Try another one: "
            )
        elif exists == False:
            loop = False

    newPassword = input("\nNow pick a password. Make sure you remember it! ")
    while valid == False:
        if newPassword == "":
            newPassword = input("Password cannot be blank. Try again: ")
        else:
            valid = True

    with open('players.txt', 'a') as playersFile:
        playersFile.write(newUsername + "," + newPassword + "\n")
        print("Your account was successfully set up.\n")

def isValid(inVar):
    # Checks if an input equals 'y', 'yes', 'n' or 'no', keeps in loop otherwise
    # If input is 'y' or 'yes', returns True
    # If input is 'n' or 'no', returns False
    inVar = inVar.lower()
    if inVar == "y" or inVar == "yes" or inVar == "n" or inVar == "no":
        valid = True
    else:
        valid = False

    while valid == False:
        inVar = input("Please enter either 'Y' or 'N': ").lower()
        if inVar == "y" or inVar == "yes" or inVar == "n" or inVar == "no":
            valid = True
        else:
            valid = False

    if inVar == 'y' or inVar == 'yes':
        return True
    elif inVar == 'n' or inVar == 'no':
        return False


def tutorialQuestion(): # Checks if player wants to go through the tutorial
    music()
    time.sleep(sSleep)
    print("\nWelcome to un-named dice rolling game!")
    time.sleep(sSleep)
    print(
        "Here's a quick look at the leaderboard. I hope you'll be beating these scores!\n"
    )
    time.sleep(sSleep)
    leaderboardDisplay()
    time.sleep(mSleep)
    answer = input(
        "Final thing - would you like to go through the tutorial? (Y/N) "
    ).lower()

    answer = isValid(answer)

    if answer == True:
        tutorial()
    elif answer == False:
        print("Alright then, let's get this show on the road!")


def tutorial(): # Displays the tutorial as written in 'tutorial.txt'
    with open("tutorial.txt", 'r') as file:
        print("\n")
        tutorial = file.readlines()
        for i in range(len(tutorial)):
            tutorial[i] = str(tutorial[i])
            print(str(tutorial[i]), end="")
            time.sleep(mSleep)
            i += 1
    print("\n")


def startGame(): # All the starting code of the game
    for i in range(2):
        auth(i + 1)
        print("\n")
    print("Correct! On with the game :)")
    tutorialQuestion()
    game()


def game(): # The main game code (total scores, round management)
    rounds = 0
    p1Score = 0
    p2Score = 0

    while rounds < totalrounds:
        p1Score = roll(1, p1Score)
        p2Score = roll(2, p2Score)
        rounds = rounds + 1
        if rounds < 5:
            time.sleep(sSleep)
            print("\nThat's the end of round",
                  str(rounds) + "!" + "\nSo far, Player 1 has", str(p1Score),
                  "and Player 2 has",
                  str(p2Score) + "!")
            time.sleep(sSleep)
            print("Now, on with round", str(rounds + 1) + ".")
            time.sleep(ssSleep)

    time.sleep(ssSleep)
    print("\nThat's the game! Let's take a look at those scores, shall we?\n")
    gameEnd(p1Score, p2Score)


def roll(currentPlayer, score): # Rolls dice and returns score
    i = currentPlayer
    print("\nPlayer", str(i) + ", you're up! Press ENTER to roll.", end=" ")
    input()
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("\nYou rolled", str(dice1), "and",
          str(dice2) + ", meaning that", str(dice1 + dice2),
          "was added to your score!")
    score = score + dice1 + dice2
    time.sleep(sSleep)

    if ((dice1 + dice2) / 2) == ((dice1 + dice2) // 2):
        print("The total was even! Score increased by 10.")
        score = score + 10
        time.sleep(sSleep)
    else:
        if score >= 5:
            score = score - 5
            print("But wait, the total was odd! Score decreased by 5.")
            time.sleep(sSleep)
        elif score < 5:
            score = 0
            print(
                "The total was odd, but as your score was below 5 you were only reset to 0."
            )
            time.sleep(sSleep)

    if dice1 == dice2:
        dice1 = random.randint(1, 6)
        score = score + dice1
        print("You rolled double, and rolled again - adding", str(dice1),
              "to your score!")
        time.sleep(sSleep)
    return score


def gameEnd(p1Score, p2Score): # Endgame sequence (displays winner, new leaderboard)
    time.sleep(sSleep)
    if p1Score != p2Score:
        print(f"{p1Username} got...  ", end="")
        source.set_paused(True)
        drumRoll()
        time.sleep(mSleep)
        print(str(p1Score) + ".\n")
        print(f"{p2Username} got...  ", end="")
        drumRoll()
        time.sleep(mSleep)
        print(str(p2Score) + ".\n")
        time.sleep(ssSleep)
        tieChk(p1Score, p2Score)
        if p1Score > p2Score:
            winner = p1Username
        else:
            winner = p2Username
        print(f"Congratulations {winner}, you won!\n")
        cheer()

    leaderboard(winner, p1Score, p2Score)

    time.sleep(lSleep)
    input("\nThanks for playing, I hope you had fun!\nPress ENTER to exit. ")
    time.sleep(sSleep)


def tieChk(p1Score, p2Score): # Checks if scores are a tie, keeps rolling until tie broken.
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
    with open("leaderboard.txt", "a") as ldbFile:
        ldbFile.write(p1Username + "," + str(p1Score) + "\n")
        ldbFile.write(p2Username + "," + str(p2Score) + "\n")
        print(
            "I've added your scores to the leaderboard! Are you in the top 5?")
    leaderboardDisplay()


## MAIN CODE

startGame()