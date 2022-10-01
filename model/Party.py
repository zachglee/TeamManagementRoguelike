class Party:
    def __init__(self, members, supplies, location=(1, 1)):
        self.members = members
        self.supplies = supplies
        self.magic = sum([member.stats.magic for member in members])
        self.location = location

    # -------- I D E M P O T E N T   H E L P E R S -------- #

    def leader(self):
        leaders = [m for m in self.members if m.leader]
        return leaders[0] if len(leaders) == 1 else None

    def followers(self):
        return [m for m in self.members if not m.leader and not m.dead]

    def exhausted(self):
        return [m for m in self.members if m.exhausted]

    def assigned(self):
        return [m for m in self.members if m.assigned]

    def available(self):
        return [m for m in self.members if not m.leader and not m.exhausted and not m.assigned and not m.dead]
    
    def alive_members(self):
        return [m for m in self.members if not m.dead]

    # -------- M U T A T I N G    H E L P E R S -------- #

    def mod_resource(self, amount, resource_key):
        current_value = getattr(self, resource_key)
        setattr(self, resource_key, current_value + amount)
        verb = 'gained' if amount >= 0 else 'lost'
        print(f"You {verb} {abs(amount)} {resource_key}! Now you have {getattr(self, resource_key)}.")



