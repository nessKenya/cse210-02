Title: Hi-Lo Game

Description
-The player is prompted to enter the name
- The number/ stack of cards is displayed
-The player starts the game with 300 points.
-Individual cards are represented as a number from 1 to 13.
-The current card is displayed.
-The player guesses if the next one will be higher or lower.
-The the next card is displayed.
-The player earns 100 points if they guessed correctly.
-The player loses 75 points if they guessed incorrectly.
-If a player reaches 0 points the game is over.
-If a player has more than 0 points they decide if they want to keep playing.
-If a player decides not to play again the game is over.

Project Structure
Main.py - Calls hilo.start_game() from hilo.py file

hilo.py - initialize empty dictionary for cards that is imported from card.py. Stacks the cards adding them to the empty
          card dictionary. 
          The cards are then shuffled and displayed for the game.
          The top card is then shown for the player to guess the next card.
          The guess is gotten from player and based on response, appropriate action follows

card.py - displays the number

Required Software: Terminal, Any IDE 

Team member name            | Email address
Nelson Muchonji Bifwoli       bif20001@byui.edu 
Guillermo Quinteros           qui22003@byui.edu
Erika Ramirez                 ramirezerika328@gmail.com
Daniel                        das22001@byui.edu