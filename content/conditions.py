#
import random

# -------- C O N D I T I O N   F A C T O R Y -------- #

def chance_(p):
    def c(game_state, source=None):
        r = random.random()
        return r < p
    return c

def not_(condition):
    def c(game_state, source=None):
        return not condition(game_state, source=source)
    return c

# -------- M I S C E L L A N E O U S -------- #

def always(game_state, source=None):
    return True

def coin_flip(game_state, source=None):
    return random.choice([True, False])

def challenge_overcome(game_state, source=None):
    return game_state.current_challenge.overcome

def challenge_impassible(game_state, source=None):
    return game_state.current_challenge.impassible

def solo_assigned(game_state, source=None):
    return len(game_state.party.assigned()) == 1

def none_assigned(game_state, source=None):
    return len(game_state.party.assigned()) == 0

# -------- P A R T Y   C O N D I T I O N S ------- #

def magic(game_state, source=None):
    return game_state.party.magic > 0

def no_magic(game_state, source=None):
    return game_state.party.magic <= 0

# -------- D E L V E R   C O N D I T I O N S -------- #

def available(game_state, source=None):
    return source.available

def assigned(game_state, source=None):
    return source.assigned

def exhausted(game_state, source=None):
    return source.exhausted

def dead(game_state, source=None):
    return source.dead

def damaged(game_state, source=None):
    return source.stats.damage > 0

def leader(game_state, source=None):
    return source.leader