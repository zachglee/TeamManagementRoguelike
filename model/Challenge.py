class Challenge:
    def __init__(self,
                 name,
                 description,
                 endure_ability,
                 base_required_physical,
                 base_required_mental,
                 overcome_ability,
                 overcome=False,
                 active=True,
                 revealed=False):
        # status
        self.overcome = overcome
        self.active = active
        self.revealed = revealed
        # main
        self.name = name
        self.description = description
        self.endure_ability = endure_ability
        self.overcome_ability = overcome_ability  # Ability
        # TODO REMOVE? self.is_overcome_by = is_overcome_by # GameState -> Boolean
        # stats
        self.required_physical = base_required_physical
        self.required_mental = base_required_mental
        self.base_required_physical = base_required_physical
        self.base_required_mental = base_required_mental

    def __repr__(self):
        return self.name

    def is_overcome_by(self, game_state):
        assigned = game_state.party.assigned()
        assigned_physical = sum([delver.stats.physical for delver in assigned])
        assigned_mental = sum([delver.stats.mental for delver in assigned])
        return assigned_physical >= self.required_physical and assigned_mental >= self.required_mental

    # TODO find a better name
    def mark_overcome(self):
        print(f"--- {self.name} was overcome! ---")
        self.overcome = True

    def execute_overcome_ability(self, game_state):
        self.overcome_ability.execute(game_state, source=self)

    def execute_endure_ability(self, game_state):
        self.endure_ability.execute(game_state, source=self)



