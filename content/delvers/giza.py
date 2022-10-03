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
    DelverStats(4, 3, 1, 0, 3, 4, supplies=5),
    follower_ability=Ability([AC(target.self, [mod_stat(2, 'morale')])]),
    leader_ability=Ability([AC(target.self, [mod_stat(2, 'durability')])]),
    bonding_targeter=bonds.fellow_assigned,
    flavor="'My body will not break.'"
)

yara_the_unwavering = Delver(
    "Yara the Unwavering",
    DelverStats(3, 4, 6, 0, 3, 5, supplies=5),
    follower_ability=Ability([AC(target.self, [mod_stat(2, 'morale')])]),
    leader_ability=Ability([AC(target.self, [mod_stat(-1, 'recovery_morale')])]),
    bonding_targeter=bonds.fellow_assigned,
    flavor="'My spirit will not falter.'"
)

samiya_the_healer = Delver(
    "Samiya the Healer",
    DelverStats(1, 6, 1, 0, 2, 4),
    follower_ability=Ability([AC(target.random_damaged, [mod_stat(-1, 'damage')])], conditions=[available]),
    leader_ability=Ability([AC(target.random_damaged, [set_stat(0, 'damage'), set_stat(2, 'morale')])]),
    bonding_targeter=bonds.fellow_assigned,
    flavor="'Rest now, my child. Let your wounds heal.'"
)

kanaan_the_survivalist = Delver(
    "Kanaan the Survivalist",
    DelverStats(5, 2, 1, 0, 4, 4),
    follower_ability=Ability([AC(target.random_damaged, [mod_stat(1, 'durability')])], conditions=[available]),
    leader_ability=Ability([AC(target.all_assigned, [mod_stat(1, 'durability')])]),
    bonding_targeter=bonds.fellow_assigned,
    flavor="'The body can go far if the spirit is strong.'"
)

rafi_the_conjuror = Delver(
    "Rafi the Conjuror",
    DelverStats(0, 7, 1, 0, 2, 4),
    follower_ability=Ability([AC(target.party, [mod_resource(1, 'magic')])], conditions=[available, chance_(0.5)]),
    leader_ability=Ability([AC(target.party, [mod_resource(-1, 'magic'), mod_resource(5, 'supplies')])], conditions=[magic]),
    bonding_targeter=bonds.fellow_assigned,
)

maya_the_scavenger = Delver(
    "Maya the Scavenger",
    DelverStats(3, 3, 1, 0, 2, 4),
    follower_ability=Ability([
        AC(target.party, [mod_resource(2, 'supplies')])
    ], conditions=[available]),
    leader_ability=Ability([
        AC(target.random_available, [exhaust]),
        AC(target.party, [mod_resource(6, 'supplies')])
    ]),
    bonding_targeter=bonds.fellow_assigned,
    flavor="'I found something!'"
)

delvers = [
    yuri_the_unbreakable,
    yara_the_unwavering,
    samiya_the_healer,
    kanaan_the_survivalist,
    rafi_the_conjuror,
    maya_the_scavenger,
]