from model.Challenge import Challenge
from model.Ability import Ability
from model.Ability import AbilityComponent as AC
from content.effects import mod_stat, mod_resource, exhaust, set_stat
import content.targeters as target

# -------- C O M M O N   A B I L I T I E S -------- #
exhaust_overcome = Ability([AC(target.all_assigned, [exhaust])])

# -------- N O N   C H A L L E N G E S -------- #
inactive_area = Challenge(
    "Inactive Area",
    "Chilling.",
    Ability([]),
    0, 0,
    Ability([]),
    active=False,
    revealed=True,
)

# --------

marrow_bruiser = Challenge(
    "Marrow Bruiser",
    "Deals damage to leader. Overcome 7/0",
    Ability([
        AC(target.leader, [mod_stat(3, "damage")]),
    ]),
    7, 0,
    exhaust_overcome,
)

marrow_horror = Challenge(
    "Marrow Horror",
    "Deals morale to leader. Overcome 2/5",
    Ability([
        AC(target.leader, [mod_stat(-4, "morale")]),
    ]),
    2, 5,
    exhaust_overcome,
)

marrow_hunter = Challenge(
    "Marrow Hunter",
    "Deals morale and damage to an available.",
    Ability([
        AC(target.random_available, [mod_stat(-2, "morale"), mod_stat(2, "damage")]),
    ]),
    4, 3,
    exhaust_overcome
)

marrow_goliath = Challenge(
    "Marrow Goliath",
    "Deals 1 damage to 2 random delvers, hard to overcome",
    Ability([
        AC(target.random_member, [mod_stat(1, "damage")]),
        AC(target.random_member, [mod_stat(1, "damage")]),
        AC(target.random_member, [mod_stat(1, "damage")]),
    ]),
    5, 5,
    Ability([
        AC(target.all_assigned, [exhaust]),
        AC(target.random_assigned, [mod_stat(2, "base_physical")])
    ])
)

abja_thief = Challenge(
    "Abja Thief",
    "Steals supplies!",
    Ability([
        AC(target.party, [mod_resource(-1, "supplies")]),
    ]),
    4, 2,
    exhaust_overcome
)

abja_trapmaster = Challenge(
    "Abja Trapmaster",
    "Exhausts 1 + 1 morale damage to random available. Overcome exhausts random assigned.",
    Ability([
        AC(target.random_available, [exhaust, mod_stat(-2, 'morale')]),
    ]),
    1, 5,
    exhaust_overcome,
)

abja_assassin = Challenge(
    "Abja Assassin",
    "Deals 2 damage to random exhausted",
    Ability([
        AC(target.random_exhausted, [mod_stat(3, 'damage')])
    ]),
    3, 3,
    exhaust_overcome
)

abja_horde = Challenge(
    "Abja Horde",
    "3 random lose morale. Hard to overcome but gives supplies.",
    Ability([
        AC(target.random_member, [mod_stat(-2, 'morale')]),
        AC(target.random_member, [mod_stat(-2, 'morale')]),
        AC(target.random_member, [mod_stat(-2, 'morale')]),
    ]),
    6, 4,
    Ability([
        AC(target.all_assigned, [exhaust]),
        AC(target.party, [mod_resource(1, 'supplies')]),
    ])
)

watcher_crippler = Challenge(
    "Watcher Crippler",
    "Leader gets -2/-2.",
    Ability([
        AC(target.leader, [mod_stat(-2, 'base_physical'), mod_stat(-2, 'base_mental')])
    ]),
    0, 7,
    exhaust_overcome,
)

watcher_deathblade = Challenge(
    "Watcher Deathblade",
    "Leader gets -2 durability",
    Ability([
        AC(target.leader, [mod_stat(-2, 'durability')])
    ]),
    3, 4,
    exhaust_overcome
)

watcher_hexmage = Challenge(
    "Watcher Hexmage",
    "Everyone loses 1 morale. leader loses more",
    Ability([
        AC(target.leader, [mod_stat(-2, 'morale')]),
        AC(target.all_available, [mod_stat(-1, 'morale')]),
        AC(target.all_exhausted, [mod_stat(-1, 'morale')]),
    ]),
    2, 5,
    exhaust_overcome
)

challenges = [
    marrow_bruiser,
    marrow_horror,
    marrow_hunter,
    marrow_goliath,
    abja_horde,
    abja_thief,
    abja_trapmaster,
    abja_assassin,
    watcher_crippler,
    watcher_deathblade,
    watcher_hexmage,
]