import random

# targeters are simple functions that return a list of 1 or more objects from a GameState

# -------- T A R G E T E R   H E L P E R S -------- #

# def _target_random(choices):
#     if len(choices) == 0: return []
#     return [random.choice(choices)]

def _target_choice(choices, choice_name="choices"):
    if len(choices) == 0: return []
    while True:
        print(f"The current {choice_name} are:")
        [print(f"{i+1}:{choice}") for i, choice in zip(range(0, len(choices)), choices)]
        user_choice = input("\n Choose one by index: ")
        if not user_choice.isnumeric():
            print(f"Input must be a valid number.")
            continue
        i = int(user_choice) - 1
        if i in range(0, len(choices)):
            return [choices[i]]

# -------- T A R G E T E R   F A C T O R I E S -------- #

# factories denoted by trailing underscore

def if_(conditions, targeter):
    def t(game_state, source=None):
        if all([condition(game_state, source=source) for condition in conditions]):
            return targeter(game_state, source=source)
        else:
            return []
    return t

def random_(get_delvers, other=False):
    def t(game_state, source=None):
        choices = [delver for delver in get_delvers(game_state)
                   if not other or delver.name != source.name]
        if len(choices) == 0: return []
        return [random.choice(choices)]
    return t

def all_(get_delvers, other=False):
    def t(game_state, source=None):
        delvers = [delver for delver in get_delvers(game_state)
                   if not other or delver.name != source.name]
        return delvers
    return t

def not_(targeter):
    def t(game_state, source=None):
        original_delvers = targeter(game_state, source=source)
        return [d for d in game_state.party.members if d not in original_delvers]
    return t



# -------- D E L V E R   T A R G E T E R S -------- #

# TODO make targets for 'exclude self'

def self(game_state, source=None):
    return [source]

def leader(game_state, source=None):
    return [game_state.party.leader()]

random_exhausted = random_(lambda g: g.party.exhausted())
random_assigned = random_(lambda g: g.party.assigned())
random_available = random_(lambda g: g.party.available())
random_damaged = random_(lambda g: [member for member in g.party.members if member.damaged()])
random_nonleader = random_(lambda g: [member for member in g.party.members if not member.leader])
random_member = random_(lambda g: g.party.members)

random_other_exhausted = random_(lambda g: g.party.exhausted(), other=True)
random_other_assigned = random_(lambda g: g.party.assigned(), other=True)
random_other_available = random_(lambda g: g.party.available(), other=True)
random_other_damaged = random_(lambda g: [member for member in g.party.members if member.damaged()], other=True)
random_member = random_(lambda g: g.party.members, other=True)

all_exhausted = all_(lambda g: g.party.exhausted())
all_assigned = all_(lambda g: g.party.assigned())
all_available = all_(lambda g: g.party.available())
all_damaged = all_(lambda g: [member for member in g.party.members if member.damaged()])
all_member = all_(lambda g: g.party.members)

all_other_exhausted = all_(lambda g: g.party.exhausted(), other=True)
all_other_assigned = all_(lambda g: g.party.assigned(), other=True)
all_other_available = all_(lambda g: g.party.available(), other=True)
all_other_damaged = all_(lambda g: [member for member in g.party.members if member.damaged()], other=True)
all_other_member = all_(lambda g: g.party.members, other=True)



def choose_exhausted(game_state, source=None):
    choices = game_state.party.exhausted()
    return _target_choice(choices, choice_name="exhausted")

def choose_assigned(game_state, source=None):
    choices = game_state.party.assigned()
    return _target_choice(choices, choice_name="assigned")

def choose_available(game_state, source=None):
    choices = game_state.party.available()
    return _target_choice(choices, choice_name="available")

# ------- L O C A T I O N   T A R G E T E R S -------- #

def choose_accessible_location(game_state, source=None):
    x, y = game_state.party.location
    width = len(game_state.layout)
    height = len(game_state.layout[0])

    def in_bounds(x, y):
        return 0 <= x < width and y >= 0 and y < height

    adjacents = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    real_adjacents = [l for l in adjacents if in_bounds(l[0], l[1])]
    accessible_adjacents = [l for l in real_adjacents if not game_state.layout[l[0]][l[1]].impassible]
    return _target_choice(accessible_adjacents, choice_name="accesssible locations")

# -------- P A R T Y   T A R G E T E R S -------- #

def party(game_state, source=None):
    return game_state.party

# -------- C H A L L E N G E   T A R G E T E R S -------- #

random_adjacent_hidden = random_(lambda g: [c for c in g.adjacent_challenges if not c.revealed])

all_adjacent_hidden = all_(lambda g: [c for c in g.adjacent_challenges if not c.revealed])