import random
import time
import sys
from replit import audio

def drumRoll():
  audio.play_file("drumRoll.mp3")

def cheer():
  audio.play_file("cheer.mp3")

def music():
  global source
  source = audio.play_file("wiiParty.mp3")
  source.volume = 0.25
  source.set_loop(-1)

def auth(playerNumber):
  p1Valid = False
  p2Valid = False
  p1Username = "player1"
  p1Password = "password"
  p2Username = "player2"
  p2Password = "password"
  print("Please enter the username for Player" ,str(playerNumber) + ": ",end="")
  usernameInput = input()
  passwordInput = input("And now the password: ")
  if playerNumber == 1:
      while p1Valid != True:
          if (usernameInput == p1Username) and (passwordInput == p2Password):
              p1Valid = True
              print("Correct. I'll just check Player 2's details, and then we can get started.\n")
              break
          else:
              if usernameInput != p1Username:
                  usernameInput = input("Username incorrect. Please try again: ")
              if passwordInput != p1Password:
                  passwordInput = input("Password incorrect. Please try again: ")
  elif playerNumber == 2:
      while p2Valid != True:
          if (usernameInput == p2Username) and (passwordInput == p2Password):
              p2Valid = True
              print("Correct! On with the game :)")
              break
          else:
              if usernameInput != p2Username:
                  usernameInput = input("Username incorrect. Please try again: ")
              if passwordInput != p2Password:
                  passwordInput = input("Password incorrect. Please try again: ")

def tutorialQuestion():
  music()
  time.sleep(2)
  print("\nWelcome to un-named dice rolling game!")
  time.sleep(2)
  answer = input("Would you like to go through the tutorial? (Y/N) ").lower()
  
  if answer == ("y" or "yes"):
    tutorial()
  else:
    print("Alright, on with the game!")
    time.sleep(1.5)

def tutorial():
  print("\nToday, you will compete for the title of dice rolling champion!")
  time.sleep(3)
  print("You will roll two dice at the start of each round, the total of which will be added to your score.")
  time.sleep(4)
  print("If the total is even, you'll gain 10 points, but if it's odd, you'll lose 5 points (you won't go below 0, though).")
  time.sleep(5)
  print("If you score a double, you can roll again, and the value of the dice will be added to your score.")
  time.sleep(4)
  print("At the end of 5 rounds, if it's a tie, you will roll one dice each until one of you scores more!")
  time.sleep(4)
  print("On with the game!")
  time.sleep(2)

def game():
  rounds = 0
  p1Score = 0
  p2Score = 0

  while rounds < 5:
    p1Score = roll(1,p1Score)
    p2Score = roll(2,p2Score)
    rounds = rounds + 1
    if rounds < 5:
      time.sleep(2)
      print("\nThat's the end of round" ,str(rounds) + "!" + "\nSo far, Player 1 has" ,str(p1Score) ,"and Player 2 has" ,str(p2Score) + "!")
      time.sleep(2.5)
      print("Now, on with round" ,str(rounds + 1) + ".")
      time.sleep(1)
  
  time.sleep(1)
  print("\nThat's the game! Let's take a look at those scores, shall we?\n")
  gameEnd(p1Score,p2Score)

def roll(currentPlayer,score):
  i = currentPlayer
  print("\nPlayer" ,str(i) + ", you're up! Press ENTER to roll." ,end=" ")
  input()
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  print("\nYou rolled" ,str(dice1) ,"and" ,str(dice2) + ", meaning that" ,str(dice1+dice2) ,"was added to your score!")
  score = score + dice1 + dice2
  time.sleep(2)

  if ((dice1+dice2)/2) == ((dice1+dice2)//2):
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
        print("The total was odd, but as your score was below 5 you were only reset to 0.")
        time.sleep(2)
    
  if dice1 == dice2:
    dice1 = random.randint(1,6)
    score = score + dice1
    print("You rolled double, and rolled again - adding" ,str(dice1) ,"to your score!")
    time.sleep(2)
  return score

def gameEnd(p1Score,p2Score):
  time.sleep(2.5)
  if p1Score != p2Score:
    print("Player 1 got...  ",end="")
    source.set_paused(True)
    drumRoll()
    time.sleep(5)
    print(str(p1Score) + ".\n")
    print("Player 2 got...  ",end="")
    drumRoll()
    time.sleep(5)
    print(str(p2Score) + ".\n")
    time.sleep(1)
    tieChk(p1Score,p2Score)
    if p1Score > p2Score:
      winner = 1
      winnerScore = p1Score
      print("Congratulations Player 1, you won!\n")
      cheer()
    else:
      winner = 2
      winnerScore = p2Score
      print("Congratulations Player 2, you won!\n")
      cheer()

    leaderboard(winner,winnerScore)
    
    time.sleep(10)
    input("\nThanks for playing, I hope you had fun!\nPress ENTER to exit. ")
    time.sleep(3)

def tieChk(p1Score,p2Score):
  tie = False
  if p1Score == p2Score:
    print("Will you look at that, it's a tie! You'll have to roll again until one of you gets the higher score.")
    tie = True

  while tie == True:
    p1Score = roll(1,p1Score)
    p2Score = roll(2,p2Score)

    if p1Score == p2Score:
        tie == True
        print("Another tie, another round!\n")
    else:
        tie == False
        print("Ok, the tie's been broken. Back to the scoreboard!")
        gameEnd(p1Score,p2Score)

def leaderboard(winner,winnerScore):
  print("Hey, Player" ,str(winner) +"!" ,"Would you like to add your score to the leaderboard? (Y/N) ",end=" ")
  ldb = input().lower()

  if ldb == "y" or "yes":
    winnerName = input("Alright, what name am I putting that under?")
    ldbFile = open("leaderboard.txt","a")
    ldbFile.write(winnerName + "," + str(winnerScore))
    print("Thanks! It's been added to the leaderboard.")
    ldbFile.close()
  else:
    print("Alright, no problem!")

  ldbFile = open("leaderboard.txt","r")
  ldbText = "LEADERBOARD"
  print("\n\n")
  print(ldbText.center(10,"-"))
  print("#1 -")


# MAIN CODE

#auth(1)
#auth(2)
#tutorialQuestion()
#game()

winner = 1
winnerScore = 56

print("Hey, Player" ,str(winner) +"!" ,"Would you like to add your score to the leaderboard? (Y/N) ",end="")
ldb = input().lower()

if ldb == "y" or "yes":
  winnerName = input("Alright, what name am I putting that under? ")
  ldbFile = open("leaderboard.txt","a")
  ldbFile.write(winnerName + "," + str(winnerScore)+"\n")
  print("Thanks! It's been added to the leaderboard.")
  ldbFile.close()
else:
  print("Alright, no problem!")

ldbFile = open("leaderboard.txt","r")
ldbText = "LEADERBOARD"
print("\n\n")
print(ldbText.center(10,"-"))
print(ldbArray)
ldbFile.close()