import content.targeters as target
import content.conditions as c

import random

# common bonding targeters

# dinae

leader_when_exhausted = target.if_([c.exhausted, c.coin_flip], target.leader)
# assigned_when_exhausted = target.if_([exhausted, coin_flip], target.random_assigned)

# assigned_when_damaged_leader = target.if_([leader, damaged, coin_flip], target.random_assigned)

fellow_assigned = target.if_([c.assigned, c.coin_flip, c.challenge_overcome], target.random_other_assigned)

# drael
damaged = target.if_([c.coin_flip], target.random_other_damaged)
solo_overcomer = target.if_([c.coin_flip, c.challenge_overcome, c.solo_assigned], target.random_other_assigned)

# giza
fellow_available = target.if_([c.available, c.chance_(0.25)], target.random_other_available)
leader_when_endure = target.if_([c.not_(c.leader), c.none_assigned, c.chance_(0.33)], target.leader)

# lacrata

def high_stat_assigned(game_state, source=None):
    if random.random() > 0.5:
        return [delver for delver in game_state.party.assigned()
                if delver.stats.physical + delver.stats.mental >= 10]
    else:
        return []

def magical_leader(game_state, source=None):
    if game_state.party.magic > 0:
        if random.random() > 0.5:
            leader = game_state.party.leader()
            return [leader] if leader else []
    return []

# Enjek

def low_stat_assigned(game_state, source=None):
    if random.random() > 0.5:
        return [delver for delver in game_state.party.assigned()
                if delver.stats.base_physical + delver.stats.base_mental <= 5]
    else:
        return []