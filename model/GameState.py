from model.ResourcePool import ResourcePool
import random

class GameState:
    def __init__(self, layout, party, delvers, supplies):
        # expedition
        self.layout = layout
        self.party = party

        # world
        self.starting_resources = ResourcePool([], supplies)
        self.surviving_resources = ResourcePool([], 0)

        # meta
        self.width = len(self.layout)
        self.height = len(self.layout[0])
        self.delver_pool = delvers
        self.timestep = 0
        self.embarked = False

        self.add_delvers_to_resource_pool(8)

    # -------- I D E M P O T E N T   H E L P E R S -------- #

    @property
    def challenges(self):
        challenges = []
        for i in range(0, len(self.layout)):
            for j in range(0, len(self.layout[0])):
                challenges.append(self.layout[i][j])
        return challenges

    @property
    def current_challenge(self):
        x, y = self.party.location
        return self.layout[x][y]

    @property
    def adjacent_locations(self):
        x, y = self.game_state.party.location
        width = len(self.game_state.layout)
        height = len(self.game_state.layout[0])

        def in_bounds(x, y):
            return 0 <= x < width and y >= 0 and y < height

        adjacents = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        real_adjacents = [l for l in adjacents if in_bounds(l[0], l[1])]
        return real_adjacents

    @property
    def adjacent_challenges(self):
        return [self.layout[x][y] for x, y in self.adjacent_locations]

    # --------

    def add_delvers_to_resource_pool(self, n):
        for _ in range(n):
            if len(self.delver_pool) > 0:
                i = random.choice(range(0, len(self.delver_pool)))
                self.starting_resources.delvers.append(self.delver_pool.pop(i))
