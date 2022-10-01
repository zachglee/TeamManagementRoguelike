from model.Delver import Delver
from model.Delver import DelverStats
from model.Ability import Ability
from model.Ability import AbilityComponent as AC
import content.targeters as target
from content.conditions import available, assigned, challenge_overcome, coin_flip, exhausted, damaged, leader, chance_
from content.effects import mod_stat, recover, exhaust, mod_resource, set_stat, mod_pm, mod_base_pm, reveal
import content.bonds as bonds

import random

# Lestes
# Bonding theme - many weak assigned
# low-stat fighters with quick recovery

def low_stat_assigned(game_state, source=None):
    if random.random() > 0.5:
        return [delver for delver in game_state.party.assigned()
                if delver.stats.base_physical + delver.stats.base_mental <= 6]
    else:
        return []

fellow_assigned = target.if_([assigned, coin_flip, challenge_overcome], target.random_other_assigned)

# Delvers

tedonae_the_archer = Delver(
    "Tedonae the Archer",
    DelverStats(5, 1, 0, 0, 1, 2),
    follower_ability=Ability([AC(target.all_assigned, [mod_stat(2, 'physical')])], conditions=[available]),
    leader_ability=Ability([AC(target.all_assigned, [mod_stat(3, 'physical')])]),
    bonding_targeter=low_stat_assigned,
    flavor="'Don't worry. I'll cover you.'"
)

hadrian_the_strategist = Delver(
    "Hadrian the Strategist",
    DelverStats(0, 6, 0, 0, 1, 2),
    Ability([AC(target.all_assigned, [mod_stat(2, 'mental')])], conditions=[available]),
    Ability([AC(target.all_assigned, [mod_stat(3, 'mental')])]),
    low_stat_assigned,
    flavor="'Listen up comrades, here's the plan...'"
)

helen_the_skirmisher = Delver(
    "Helen the Skirmisher",
    DelverStats(4, 1, 0, 0, 2, 1),
    follower_ability=Ability([AC(target.self, [mod_stat(2, 'morale')])], conditions=[assigned]),
    leader_ability=Ability([AC(target.all_assigned, [mod_stat(1, 'morale')])]),
    bonding_targeter=fellow_assigned,
    flavor="'Everyone ready? Let's make this a fight to remember.'"
)

caed_the_tactician = Delver(
    "Caed the Tactician",
    DelverStats(2, 3, 0, 0, 2, 1),
    follower_ability=Ability([AC(target.self, [mod_stat(2, 'morale')])], conditions=[assigned]),
    leader_ability=Ability([AC(target.all_assigned, [mod_pm(1, 1)])]),
    bonding_targeter=fellow_assigned,
    flavor="'Fight hard. Fight smart. Fight as one.'"
)

bacchus_the_cook = Delver(
    "Bacchus the Cook",
    DelverStats(0, 5, 0, 0, 2, 1),
    follower_ability=Ability([AC(target.all_exhausted, [mod_stat(1, 'morale')])], conditions=[available]),
    leader_ability=Ability([
        AC(target.all_exhausted, [mod_stat(1, 'morale')]),
        AC(target.all_available, [mod_stat(1, 'morale')])
    ]),
    bonding_targeter=low_stat_assigned,
    flavor="'They can't fight if they can't eat.'"
)

eve_the_firebrand = Delver(
    "Eve the Firebrand",
    DelverStats(3, 2, 0, 0, 2, 1),
    follower_ability=Ability([AC(target.all_exhausted, [mod_stat(1, 'morale')])], conditions=[assigned]),
    leader_ability=Ability([
        AC(target.random_exhausted, [mod_stat(2, 'morale')]),
    ]),
    bonding_targeter=fellow_assigned,
    flavor="'Pick yourself up! I'm not going to let them do all the fighting, are you?!"
)

delvers = [
    tedonae_the_archer,
    hadrian_the_strategist,
    helen_the_skirmisher,
    caed_the_tactician,
    bacchus_the_cook,
    eve_the_firebrand,
]