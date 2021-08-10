# Dice Game NEA

This is my take on the OCR Dice Game NEA.

## Features
- [x] Authentication
- [x] Tutorial
- [x] Scoring system
- [x] Sound effects and music! Not strictly necessary but fun.

## To Do (?)
- Allow for the creation of new user accounts, the details of which will be stored in a file.
- Store highscores in a file and then display these in a leaderboard format.

## Rules
Each player will roll two dice at the start of each round, the total of which will be added to their score. If the total is even, they'll gain 10 points, but if it's odd, they'll lose 5 points (their score won't go below 0, though). If they score a double, they roll again, and the value of the dice will be added to their score. At the end of 5 rounds, if it's a tie, each player will roll one dice each until one of the players scores more.

## Dependencies
As of late, the only required dependency is replit, which provides the audio module for background music and sound effects, and can be installed using the command `pip3 install replit`. However, I have run into problems with the code outside out repl.it and as such recommend that it is run on the service exclusively.

## Notes: *interesting* things about the game
- The leaderboard must have an empty line at the end of the entries.
- Sometimes the audio (especially the drumroll) plays late or does not play at all.
  - *This is probably due to the audio being streamed from repl.it*

## License
© Felix Yates 2020 excluding the below audio files:
  * wiiParty.mp3 and wiiPartySHORT.mp3 - Nintendo Wii Party 'Spin-Off' music
  * drumRoll.mp3 - Epidemic Sound
  * diceRoll.mp3 - Epidemic Sound
  * cheer.mp3 - Epidemic Sound

Note: the Epidemic Sound sound effects are not included in the project for copyright reasons. You must find and use your own.
You can use bits of the code, but if you do please be respectful- give credit where it's due and don't just copy and paste it. 
