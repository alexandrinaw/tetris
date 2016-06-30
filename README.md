[![Build Status](https://travis-ci.org/alexandrinaw/tetris.svg?branch=master)](https://travis-ci.org/alexandrinaw/tetris)

# tetris
A command line tetris game you (or an AI!) can play in your terminal!

![AI Playing Tetris](demo.gif)

## To Play
```
git clone https://github.com/alexandrinaw/tetris.git
cd tetris
```

### Human Player
```
python tetris/game.py
```
#### Commands
* `up arrow`: rotates piece
* `down arrow`: makes currently falling piece fall faster
* `right arrow`: makes currently falling piece move right
* `left arrow`: makes currently falling piece move left
* `enter`: makes currently falling piece fall all the way to the bottom
* `p`: pauses the game
* `q`: quits the game and exits

### AI Player
```
python ai.py
```
