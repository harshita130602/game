# RIVER CROSSING GAME

## Run the game in your system

Make sure that your system has the version of python>=3. Now, run the following commands in your terminal in order to run the game in your system:
* `git clone https://github.com/harshita130602/river-crossing-game`
* `cd river-crossing-game`
* `python3 game.py`

Now, play the game!

## Breif overview 
The RIVER CROSSING GAME is a simple multi-player game built by using pygame in python. The playing arena of game consists of a river with some partitions in it. There are 2 players in the game, one at Top and another at Bottom (2 sides of the river bank). A player is safe when it is standing on a partition/slab. There are two kinds of obstacles, moving and fixed. The player starts from the ‘START’ partition and must reach the ‘END’ position for player 1 and the ‘END’ becomes ‘START’, ‘START’ becomes ‘END’ for Player 2. The moving obstacles move from left to right. The player can move up, down, left and right using the up, down, left and right keys respectively. Player dies once he/she touches any obstacle. As player crosses moving obstacle successfully, accrues 10 points and for crossing fixed obstacles 5 points. Only one player is playing at a given point of time. 

**Your aim is to make players reach the other end of the river. The player wins the game based on**
* **Time taken to cross**
* **Points accrued while crossing obstacles**

At the end of the game (after both the players either die or reach other ‘END’), the players are respawned to their starting position. If the player wins a round, the speed of moving objects increases in the next round for that player. Score for the game is displayed on the screen.

**NOTE - This project is licensed under MIT License 2020. If you find any bugs in the game, please visit [issues column](https://github.com/harshita130602/river-crossing-game/issues) to report the issue.** 

## Enjoy the game!
