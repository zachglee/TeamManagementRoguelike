from content.delvers.delvers import delvers
from content.challenges.challenges import challenges
from controller.generation import generate_start_game_state
from controller.controller import Game
import random

gs = generate_start_game_state(challenges, delvers, width=7, height=7, supplies=200)
game = Game(gs)

game.play()
