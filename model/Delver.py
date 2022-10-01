import random


class DelverStats:
    def __init__(self,
                 base_physical,
                 base_mental,
                 morale,
                 magic,
                 durability,
                 recovery_morale,
                 exhausted=False,
                 damage=0,
                 supplies=0,
                 num_bonds=2):
        self.base_physical = base_physical
        self.base_mental = base_mental
        self.physical = base_physical
        self.mental = base_mental
        self.morale = morale
        self.damage = damage
        self.magic = magic
        self.supplies = supplies
        self.durability = durability
        self.recovery_morale = recovery_morale
        self.exhausted = exhausted
        self.num_bonds = num_bonds


class Delver:
    def __init__( self, name, stats, follower_ability, leader_ability, bonding_targeter, flavor=""):
        self.leader = False
        self.assigned = False
        self.exhausted = False
        self.dead = False
        self.bonds = []
        #
        self.name = name
        self.stats = stats
        self.follower_ability = follower_ability
        self.leader_ability = leader_ability
        self.bonding_targeter = bonding_targeter
        self.flavor = flavor

    def __repr__(self):
        return self.name

    # -------- I D E M P O T E N T   H E L P E R S -------- #

    @property
    def recovery_morale(self):
        recovery_morale = self.stats.recovery_morale
        if any([delver.leader for delver in self.bonds]):
            recovery_morale -= 1
        return recovery_morale

    @property
    def primary_stat(self):
        if self.stats.base_physical > self.stats.base_mental:
            return "physical"
        elif self.stats.base_mental > self.stats.base_physical:
            return "mental"
        else:
            return random.choice(["physical", "mental"])

    @property
    def physical(self):
        physical = self.stats.physical
        if any([delver.leader for delver in self.bonds]):
            leader_primary_stat = [d for d in self.bonds if d.leader][0].primary_stat
            if leader_primary_stat == "physical":
                physical += 1
        return physical

    @property
    def mental(self):
        mental = self.stats.mental
        if any([delver.leader for delver in self.bonds]):
            leader_primary_stat = [d for d in self.bonds if d.leader][0].primary_stat
            if leader_primary_stat == "mental":
                mental += 1
        return mental

    def should_die(self):
        return (self.stats.damage > (2 * self.stats.durability)
                or self.stats.damage > self.stats.durability and self.exhausted)

    def should_exhaust(self):
        return not self.exhausted and self.stats.morale <= self.recovery_morale - 4

    def should_recover(self):
        return self.exhausted and not self.dead and self.stats.morale >= self.recovery_morale

    def should_inspire(self):
        return self.exhausted and not self.dead and self.stats.morale >= self.recovery_morale * 2

    def damaged(self, threshold=1):
        return self.stats.damage >= threshold

    @property
    def available(self):
        return not self.dead and not self.leader and not self.assigned and not self.exhausted

    # -------- S T A T E - C H A N G E   F U N C T I O N S -------- #

    def execute_follower_ability(self, game_state):
        self.follower_ability.execute(game_state, source=self)

    def execute_leader_ability(self, game_state):
        self.leader_ability.execute(game_state, source=self)

    def execute_bonding(self, game_state):
        bonding_targets = self.bonding_targeter(game_state, source=self)
        for delver in bonding_targets:
            self.bond(delver)

    # -------- L O C A L - C H A N G E   F U N C T I O N S ------- #

    def mod_stat(self, amount, stat_key):
        current_value = getattr(self.stats, stat_key)
        if stat_key == 'damage' and current_value + amount < 0:
            amount = current_value * -1
        setattr(self.stats, stat_key, current_value + amount)
        verb = 'gained' if amount >= 0 else 'lost'
        print(f"{self.name} {verb} {abs(amount)} {stat_key}! Now they have {getattr(self.stats, stat_key)}.")

    def set_stat(self, value, stat_key):
        setattr(self.stats, stat_key, value)
        print(f"{self.name}'s {stat_key} was set to {value}.")

    def bond(self, delver):
        if len(self.bonds) < self.stats.num_bonds and delver not in self.bonds:
            self.bonds.append(delver)
            print(f"{self.name} bonded to {delver.name}!")

    def exhaust(self, exhausted=True):
        self.exhausted = exhausted
        if self.exhausted:
            self.leader = False
        print(f"{self.name} is {'no longer ' if not exhausted else ''}exhausted!")

    def recover(self, morale_cost=0):
        self.exhaust(exhausted=False)
        self.mod_stat(morale_cost * -1, 'morale')

    def lead(self, leader=True):
        self.leader = leader
        print(f"{self.name} is {'no longer ' if not leader else ''}leading!")

    def assign(self, assigned=True):
        if self.leader or self.exhausted:
            print("ERROR: You cannot assign a delver that is exhausted, or the leader")
            return
        self.assigned = assigned
        print(f"{self.name} is {'no longer ' if not assigned else ''}leading!")

    def die(self, dead=True):
        self.exhausted = False
        self.leader = False
        self.assigned = False
        self.dead = dead
        print(f"{self.name} is {'no longer ' if not dead else ''}dead!")
