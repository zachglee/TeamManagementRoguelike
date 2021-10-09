from content.conditions import always, available

# -------- H E L P E R S -------- #

# returns true if all given conditions return true when run on game_state and source
def all_conditions(game_state, source, conditions):
    return all([condition(game_state, source=source) for condition in conditions])

# An Ability is a collection of effects.

class AbilityComponent:
    def __init__(self, targeter, effects, conditions=[always]):
        self.targeter = targeter
        self.effects = effects
        self.conditions = conditions

class Ability:
    def __init__(self, ability_components, conditions=[always], trigger=None, name=''):
        self.ability_components = ability_components
        self.conditions = conditions
        self.trigger = trigger
        self.name = name

    def execute(self, game_state, source=None):
        if all_conditions(game_state, source, self.conditions):
            if source:
                print(f"!! {source} used ability {self.name} !!")
            for ac in self.ability_components:
                if all_conditions(game_state, source, ac.conditions):
                    targets = ac.targeter(game_state, source)
                    for effect in ac.effects:
                        effect(targets)

# --------