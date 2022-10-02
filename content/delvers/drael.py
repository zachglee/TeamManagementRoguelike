from model.Delver import Delver
from model.Delver import DelverStats
from model.Ability import Ability
from model.Ability import AbilityComponent as AC
import content.targeters as target
from content.conditions import available, assigned, magic, no_magic, coin_flip, exhausted, damaged, leader
from content.effects import mod_stat, recover, exhaust, mod_resource, set_stat, mod_pm, mod_base_pm
import content.bonds as bonds

# Drael

# Bonding Theme: Respect taking a lot of damage, and respect assigned, glorious deeds

bob_the_berserker = Delver(
    "Bob the Berserker",
    DelverStats(5, 2, 0, 0, 4, 3),
    follower_ability=Ability([AC(target.self, [mod_pm(3, 3)])], conditions=[assigned, damaged]),
    leader_ability=Ability([AC(target.random_assigned, [mod_pm(3, 3), mod_stat(1, 'damage')])]),
    bonding_targeter=bonds.damaged,
    flavor="'Make that wound your strength, not your weakness.'"
)

torv_the_blessed = Delver(
    "Torv the Blessed",
    DelverStats(6, 2, 0, 1, 3, 4),
    follower_ability=Ability([AC(target.self, [set_stat(0, 'damage')])], conditions=[available, magic]),
    leader_ability=Ability([
        AC(target.party, [mod_resource(1, 'magic')]),
        AC(target.self, [mod_stat(1, 'damage')])
    ]),
    bonding_targeter=bonds.damaged,
    flavor="'Blood is magic, and magic is blood.'"
)

kayle_the_warcleric = Delver(
    "Kayle the Warcleric",
    DelverStats(3, 5, 0, 1, 3, 4),
    follower_ability=Ability([AC(target.random_assigned, [mod_stat(-1, 'damage')])], conditions=[available]),
    leader_ability=Ability([
        AC(target.all_assigned, [mod_stat(-1, 'damage')]),
        AC(target.all_assigned, [mod_stat(1, "base_physical")]),
        AC(target.party, [mod_resource(-1, 'magic')]),
    ], conditions=[magic]),
    bonding_targeter=bonds.damaged,
    flavor="'Your wounds are nothing beneath the Hand of Drael.'"
)

idra_the_warcaller = Delver(
    "Idra the Warcaller",
    DelverStats(2, 6, 0, 1, 2, 3),
    follower_ability=Ability([AC(target.random_exhausted, [mod_stat(2, 'morale')])], conditions=[available, magic]),
    leader_ability=Ability([
        AC(target.all_member, [recover, mod_stat(2, 'morale')]),
        AC(target.party, [mod_resource(-1, 'magic')])
    ], conditions=[magic]),
    bonding_targeter=bonds.solo_overcomer,
    flavor="'Glory in battle. Shame in retreat.'"
)

brinn_the_ritualist = Delver(
    "Brinn the Ritualist",
    DelverStats(1, 7, 0, 0, 3, 3),
    follower_ability=Ability([AC(target.random_exhausted, [recover, mod_stat(1, 'damage'), mod_stat(1, 'morale')])], conditions=[available]),
    leader_ability=Ability([
        AC(target.random_exhausted, [recover, mod_stat(1, 'morale')]),
        AC(target.self, [mod_stat(1, 'damage')]),
    ]),
    bonding_targeter=bonds.solo_overcomer,
    flavor="'To bleed is to be alive.'"
)

hama_the_bladedancer = Delver(
    "Hama the Bladedancer",
    DelverStats(7, 3, 0, 0, 3, 4),
    follower_ability=Ability([AC(target.self, [recover])], conditions=[exhausted, damaged]),
    leader_ability=Ability([AC(target.self, [mod_stat(2, 'morale')])], conditions=[damaged]),
    bonding_targeter=bonds.solo_overcomer,
    flavor="'Ha, can I still fight? I'm alive, aren't I?'"
)

delvers = [
    bob_the_berserker,
    idra_the_warcaller,
    kayle_the_warcleric,
    brinn_the_ritualist,
    torv_the_blessed,
    hama_the_bladedancer,
]