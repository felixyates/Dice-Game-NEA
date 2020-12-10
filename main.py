import random
import time
from replit import audio

## (C) Felix Yates 2020. More information available in README.md

# These are global sleep timings. Change these to 0 when testing.
# Default values can also be found below to change back to.

global ssSleep # supershort sleep, default - 1.5 seconds
global sSleep # short sleep, default - 2 seconds
global mSleep # medium sleep, default - 5 seconds
global lSleep # long sleep, default - 8 seconds
ssSleep = 1.5
sSleep = 2
mSleep = 5
lSleep = 8


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


def auth(playerNumber):
    valid = False
    exists = False
    usernameInput = input(f"Enter your username, Player {playerNumber}: ")
    players = getPlayers()
    exists = doesExist(usernameInput)
    if exists == False:
      while exists == False:
        createAccount = input(f"That account ({usernameInput}) does not exist. Would you like to create a new account? (Y/N) ").lower()
        if createAccount == 'y' or 'yes':
          accountCreator(playerNumber)
        else:
          auth(playerNumber)
    
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

    passwordInput = input("Now the password: ")
    while valid != True:
        if (usernameInput == username) and (passwordInput == password):
            valid = True
            break
        else:
            if usernameInput != username:
                usernameInput = input("Username incorrect. Please try again: ")
            if passwordInput != password:
                passwordInput = input("Password incorrect. Please try again: ")

def getPlayers():
  players = []
  with open('players.txt', 'r') as existingPlayers:
    existingPlayers = existingPlayers.readlines()
    for i in range(len(existingPlayers)):
      players.append(str(existingPlayers[i]).split(","))
      players[i][1] = players[i][1].strip()
  return players

def doesExist(usernameInput):
  exists = False
  players = getPlayers()
  for i in range(len(players)):
    if str(players[i][0]) == usernameInput:
      exists = True
      return True
    
  if exists == False:
    return False
    

def accountChecker(playerNumber):
    valid = False
    if playerNumber == 1:
        hasAccount = input(
            f"Welcome, Player {playerNumber}! Do you have an account? (Y/N) "
        ).lower()
    elif playerNumber == 2:
        hasAccount = input(
            f"Excellent! And what about you, Player {playerNumber}? (Y/N) "
        ).lower()

    if hasAccount == "y" or hasAccount == "yes":
        if playerNumber == 1:
            accountChecker(2)
        elif playerNumber == 2:
            startGame()

    elif hasAccount == "n" or hasAccount == "no":
        accountCreator(playerNumber)
    else:
        valid = False
        while valid != True:
            hasAccount = input("Please enter either 'Y' or 'N': ").lower()
            if hasAccount == 'y' or hasAccount == 'yes':
                valid = True
                if playerNumber == 1:
                    accountChecker(2)
                elif playerNumber == 2:
                    print(
                        "\nPerfect! Now we'll just sign you in and get playing...\n"
                    )
                    for i in range(2):
                        auth(i + 1)
            elif hasAccount == 'n' or hasAccount == 'no':
                valid = True
                accountCreator(playerNumber)


def accountCreator(playerNumber):
    loop = True
    valid = False
    print("That's OK! I'll get one set up for you right away.")
    time.sleep(sSleep)
    newUsername = input(
        "\nFirst, pick a username.\nRemember, this will appear on the leaderboard, so keep it clean! "
    )

    while loop != False:
      exists = doesExist(newUsername)
      if exists == True:
        newUsername = input(f"Uh oh, that username ({newUsername}) already exists. Try another one: ")
      elif exists == False:
        loop = False

    newPassword = input("Now pick a password. Make sure you remember it! ")
    while valid == False:
        if newPassword == "":
            newPassword = input("Password cannot be blank. Try again: ")
        else:
            valid = True

    with open('players.txt', 'a') as playersFile:
      playersFile.write(newUsername+","+newPassword+"\n")
      print(f"Your account was successfully set up.\n")
    if playerNumber == 1:
      accountChecker(2)
    else:
      startGame()

def isValid(): # need to write
  ## Checks if an input equals 'y', 'yes', 'n' or 'no', keeps in loop otherwise
  print("Need to write this!!")


def tutorialQuestion():
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

    if answer == "y" or answer == "yes":
        tutorial()
    elif answer == "n" or answer == "no":
        print("Alright then, let's get this show on the road!")
        time.sleep(ssSleep)
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
                time.sleep(ssSleep)


def tutorial():
    with open("tutorial.txt", 'r') as file:
        print("\n")
        tutorial = file.readlines()
        for i in range(len(tutorial)):
            tutorial[i] = str(tutorial[i])
            print(str(tutorial[i]), end="")
            time.sleep(mSleep)
            i += 1
    print("\n")

def startGame():
  print("\nPerfect! Now we'll just sign you in and get playing...\n")
  for i in range(2):
    auth(i + 1)
  print("Correct! On with the game :)")
  tutorialQuestion()
  game()

def game():
    rounds = 0
    p1Score = 0
    p2Score = 0

    while rounds < 5:
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


def gameEnd(p1Score, p2Score):
    time.sleep(sSleep)
    if p1Score != p2Score:
        print("Player 1 got...  ", end="")
        source.set_paused(True)
        drumRoll()
        time.sleep(mSleep)
        print(str(p1Score) + ".\n")
        print("Player 2 got...  ", end="")
        drumRoll()
        time.sleep(mSleep)
        print(str(p2Score) + ".\n")
        time.sleep(ssSleep)
        tieChk(p1Score, p2Score)
        if p1Score > p2Score:
            winner = 1
        else:
            winner = 2
        print("Congratulations Player " + str(winner) + ", you won!\n")
        cheer()

    leaderboard(winner, p1Score, p2Score)

    time.sleep(lSleep)
    input("\nThanks for playing, I hope you had fun!\nPress ENTER to exit. ")
    time.sleep(sSleep)


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
    with open("leaderboard.txt", "a") as ldbFile:
        ldbFile.write(p1Username + "," + str(p1Score) + "\n")
        ldbFile.write(p2Username + "," + str(p2Score) + "\n")
        print("I've added your scores to the leaderboard! Are you in the top 5?")
    leaderboardDisplay()

## MAIN CODE

accountChecker(1)