import random
import copy

from model.GameState import GameState
from model.Party import Party

from content.challenges.challenges import inactive_area

# functions for procedural generation

def generate_layout(challenges, width=3, height=3):
    # generate 2d array of width x height
    layout = [[None for _ in range(0, height)] for _ in range(width)]
    for x in range(0, width):
        for y in range(0, height):
            layout[x][y] = copy.deepcopy(random.choice(challenges))
    layout[1][1] = inactive_area
    layout[width-1][height-1] = inactive_area
    layout[0][height-1] = inactive_area
    layout[width-1][0] = inactive_area
    return layout

def generate_delver_pool(delvers, n=3):
    return delvers  # TODO change this

def generate_start_game_state(challenges, delvers, width=3, height=3, supplies=30):
    layout = generate_layout(challenges, width=width, height=height)
    game_state = GameState(layout, Party([], 0), delvers, supplies)
    return game_state