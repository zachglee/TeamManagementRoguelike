from model.Delver import Delver
from model.Delver import DelverStats
from model.Ability import Ability
from model.Ability import AbilityComponent as AC
import content.targeters as target
from content.conditions import available, assigned, magic, no_magic, coin_flip, exhausted, damaged, leader, chance_
from content.effects import mod_stat, recover, exhaust, mod_resource, set_stat, mod_pm, mod_base_pm, reveal
import content.bonds as bonds

# # Giza - scrying, supplies, good stats
# Bonding Theme: they respect clever solutions to problems, weathering the storm
# - bond to leader that doesn't assign anyone (.25 chance)
# - bond to fellow availables .25 chance
#

yuri_the_unbreakable = Delver(
    "Yuri the Unbreakable",
    DelverStats(3, 2, 1, 0, 4, 2, supplies=1),
    Ability([AC(target.random_other_available, [mod_stat(1, 'morale')])]),
    Ability([AC(target.random_available, [mod_stat(1, 'morale')])]),
    bonds.leader_when_endure,
)

yara_the_unwavering = Delver(
    "Yara the Unwavering",
    DelverStats(2, 3, 6, 0, 2, 2, supplies=1),
    Ability([AC(target.random_other_available, [mod_stat(1, 'morale')])]),
    Ability([AC(target.random_available, [mod_stat(1, 'morale')])]),
    bonds.leader_when_endure,
)

samiya_the_healer = Delver(
    "Samiya the Healer",
    DelverStats(0, 6, 1, 0, 1, 2),
    Ability([AC(target.random_damaged, [mod_stat(-1, 'damage')])], conditions=[available]),
    Ability([AC(target.random_damaged, [set_stat(0, 'damage'), set_stat(2, 'morale')])]),
    bonds.leader_when_endure,
)

kanaan_the_survivalist = Delver(
    "Kanaan the Survivalist",
    DelverStats(4, 2, 1, 0, 3, 2),
    Ability([AC(target.random_damaged, [mod_stat(1, 'durability'), mod_base_pm(-1, 0)])], conditions=[available]),
    Ability([AC(target.random_damaged, [mod_stat(1, 'durability'), mod_base_pm(0, -1)])]),
    bonds.fellow_available,
)

rafi_the_conjuror = Delver(
    "Rafi the Conjuror",
    DelverStats(1, 5, 1, 0, 1, 2),
    Ability([AC(target.party, [mod_resource(1, 'magic')])], conditions=[available, chance_(0.5)]),
    Ability([AC(target.party, [mod_resource(-1, 'magic'), mod_resource(1, 'supplies')])], conditions=[magic]),
    bonds.fellow_available,
)

maya_the_scavenger = Delver(
    "Maya the Scavenger",
    DelverStats(3, 3, 1, 0, 1, 2),
    Ability([
        AC(target.self, [exhaust]),
        AC(target.party, [mod_resource(1, 'supplies')])
    ], conditions=[coin_flip, available]),
    Ability([
        AC(target.random_available, [exhaust]),
        AC(target.party, [mod_resource(1, 'supplies')])
    ], conditions=[coin_flip]),
    bonds.fellow_available
)

delvers = [
    yuri_the_unbreakable,
    yara_the_unwavering,
    samiya_the_healer,
    kanaan_the_survivalist,
    rafi_the_conjuror,
    maya_the_scavenger,
]