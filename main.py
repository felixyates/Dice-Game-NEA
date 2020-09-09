import random
import time
import sys
from replit import audio

def drumRoll():
    audio.play_file("drumRoll.mp3")

def cheer():
  audio.play_file("cheer.mp3")

def music():
    audio.play_file("wiiParty.mp3",does_loop = True,volume=0.5)

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
              music()
              break
          else:
              if usernameInput != p2Username:
                  usernameInput = input("Username incorrect. Please try again: ")
              if passwordInput != p2Password:
                  passwordInput = input("Password incorrect. Please try again: ")

def tutorialQuestion():
  print("\nWelcome to un-named dice rolling game!")
  time.sleep(2)
  answer = input("Would you like to go through the tutorial? (Y/N) ").lower()
  
  if answer == ("y" or "yes"):
    tutorial()
  else:
    print("Alright, on with the game!")

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

# MAIN CODE

rounds = 0
tie = False
p1Score = 0
p2Score = 0

auth(1)
auth(2)
tutorialQuestion()

while rounds < 5:

## BEGINNING OF PLAYER 1 - MAKE INTO FUNCTION

    input("\nPlayer 1, you're up! Press ENTER to roll. ")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("\nYou rolled" ,str(dice1) ,"and" ,str(dice2) + ", meaning that" ,str(dice1+dice2) ,"was added to your score!")
    p1Score = p1Score + dice1 + dice2

    if ((dice1+dice2)/2) == ((dice1+dice2)//2):
        print("The total was even! Score increased by 10.")
        p1Score = p1Score + 10

    else:
        if p1Score >= 5:
            p1Score = p1Score - 5
        print("But wait, the total was odd! Score decreased by 5.")
    
    if dice1 == dice2:
        dice1 = random.randint(1,6)
        p1Score = p1Score + dice1
        print("You rolled double, and rolled again - adding" ,str(dice1) ,"to your score!")

## BEGINNING OF PLAYER 2 - another function

    input("\nYour turn, Player 2! Press ENTER to roll. ")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("\nYou rolled" ,str(dice1) ,"and" ,str(dice2) + ", meaning that" ,str(dice1+dice2) ,"was added to your score!")
    p2Score = p2Score + dice1 + dice2

    if ((dice1+dice2)/2) == ((dice1+dice2)//2):
        print("The total was even! Score increased by 10.")
        p2Score = p2Score + 10
    else:
        if p2Score >= 5:
            p2Score = p2Score - 5
        else:
            p2Score = 0
        print("But wait, the total was odd! Score decreased by 5.")
    
    if dice1 == dice2:
        dice1 = random.randint(1,6)
        p2Score = p2Score + dice1
        print("You rolled double, and rolled again - adding" ,str(dice1) ,"to your score!")
    
    rounds = rounds + 1

    if rounds < 5:
        print("\nThat's the end of round" ,str(rounds) + "!" + "\nSo far, Player 1 has" ,str(p1Score) ,"and Player 2 has" ,str(p2Score) + "!")
        time.sleep(2.5)
        print("Now, on with round" ,str(rounds + 1) + ".")
        time.sleep(1)

time.sleep(1)
print("\nThat's the game! Let's take a look at those scores, shall we?\n")
time.sleep(2.5)
if p1Score != p2Score:
    print("Player 1 got...  ",end="")
    drumRoll()
    print(str(p1Score) + ".\n")
    print("Player 2 got...  ",end="")
    drumRoll()
    print(str(p2Score) + ".\n")
    if p1Score > p2Score:
        print("Congratulations Player 1, you won!\n")
        cheer()
    else:
        print("Congratulations Player 2, you won!\n")
        cheer()

if p1Score == p2Score:
    print("Will you look at that, it's a tie! You'll have to roll again until one of you gets the higher score.")
    tie = True

while tie == True:
    input("Player 1, press ENTER to roll! ") #function here?
    dice1 = random.randint(1,6)
    p1Score = p1Score + dice1

    input("Back to you, Player 2. Press ENTER to roll! ")
    dice1 = random.randint(1,6)
    p2Score = p2Score + dice1

    if p1Score == p2Score:
        tie == True
        print("Another tie, another round!\n")
    else:
        tie == False
        print("Ok, the tie's been broken. Back to the scoreboard!")
        
        time.sleep(2.5)
        if p1Score != p2Score:
            print("Player 1 got" ,str(p1Score) ,"and Player 2 got" ,str(p2Score) + "!")
            if p1Score > p2Score:
                print("Congratulations Player 1, you won!\n")
            else:
                print("Congratulations Player 2, you won!\n")