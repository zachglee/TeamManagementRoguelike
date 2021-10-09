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
    DelverStats(4, 2, 0, 0, 3, 2),
    Ability([AC(target.self, [mod_pm(3, 3)])], conditions=[assigned, damaged]),
    Ability([AC(target.random_assigned, [mod_pm(3, 3), mod_stat(1, 'damage')])]),
    bonds.damaged
)

torv_the_blessed = Delver(
    "Torv the Blessed",
    DelverStats(5, 2, 0, 1, 2, 3),
    Ability([AC(target.self, [mod_stat(-1, 'damage')])], conditions=[available, magic]),
    Ability([
        AC(target.party, [mod_resource(1, 'magic')]),
        AC(target.self, [mod_stat(1, 'damage')])
    ], conditions=[no_magic]),
    bonds.damaged
)

kayle_the_warcleric = Delver(
    "Kayle the Warcleric",
    DelverStats(2, 5, 0, 1, 2, 3),
    Ability([AC(target.random_assigned, [mod_stat(-1, 'damage')])], conditions=[available]),
    Ability([
        AC(target.all_exhausted, [mod_stat(-1, 'damage')]),
        AC(target.all_available, [mod_stat(-1, 'damage')]),
        AC(target.all_assigned, [mod_stat(-1, 'damage')]),
        AC(target.party, [mod_resource(-1, 'magic')]),
    ], conditions=[magic]),
    bonds.damaged,
)

idra_the_warcaller = Delver(
    "Idra the Warcaller",
    DelverStats(1, 5, 0, 1, 1, 2),
    Ability([AC(target.random_exhausted, [mod_stat(2, 'morale')])], conditions=[available, magic]),
    Ability([
        AC(target.all_exhausted, [recover, mod_stat(1, 'morale')]),
        AC(target.party, mod_resource(-1, 'magic'))
    ], conditions=[magic]),
    bonds.solo_overcomer
)

brinn_the_ritualist = Delver(
    "Brinn the Ritualist",
    DelverStats(1, 6, 0, 0, 2, 2),
    Ability([AC(target.random_exhausted, [recover, mod_stat(1, 'damage')])], conditions=[available]),
    Ability([
        AC(target.random_exhausted, [recover]),
        AC(target.self, [mod_stat(1, 'damage')]),
    ]),
    bonds.solo_overcomer
)

hama_the_bladedancer = Delver(
    "Hama the Bladedancer",
    DelverStats(7, 3, 0, 0, 2, 3),
    Ability([AC(target.self, [recover])], conditions=[exhausted, damaged]),
    Ability([AC(target.self, [mod_stat(2, 'morale')])], conditions=[damaged]),
    bonds.solo_overcomer,
)

delvers = [
    bob_the_berserker,
    idra_the_warcaller,
    kayle_the_warcleric,
    brinn_the_ritualist,
    torv_the_blessed,
    hama_the_bladedancer,
]