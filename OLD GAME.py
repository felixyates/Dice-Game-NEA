while rounds < 5:
  player = 0
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