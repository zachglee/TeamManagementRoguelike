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
    "Deals 3 damage to leader. Overcome 7/0",
    Ability([
        AC(target.leader, [mod_stat(3, "damage")]),
    ]),
    9, 0,
    exhaust_overcome,
)

marrow_horror = Challenge(
    "Marrow Horror",
    "-5 morale to leader. Overcome 2/5",
    Ability([
        AC(target.leader, [mod_stat(-5, "morale")]),
    ]),
    3, 6,
    exhaust_overcome,
)

marrow_hunter = Challenge(
    "Marrow Hunter",
    "Sets damage to 3 for random non-leader.",
    Ability([
        AC(target.random_nonleader, [set_stat(3, "damage")]),
    ]),
    5, 5,
    exhaust_overcome
)

marrow_goliath = Challenge(
    "Marrow Goliath",
    "1 damage and -1 morale to all, bonus if overcome",
    Ability([
        AC(target.all_assigned, [mod_stat(-1, "morale"), mod_stat(1, "damage")]),
        AC(target.all_available, [mod_stat(-1, "morale"), mod_stat(1, "damage")]),
        AC(target.leader, [mod_stat(-1, "morale"), mod_stat(1, "damage")]),
    ]),
    10, 2,
    Ability([
        AC(target.all_assigned, [exhaust]),
        AC(target.random_assigned, [mod_stat(2, "base_physical")])
    ])
)

abja_thief = Challenge(
    "Abja Thief",
    "Steals supplies!",
    Ability([
        AC(target.party, [mod_resource(-7, "supplies")]),
    ]),
    5, 2,
    exhaust_overcome
)

abja_trapmaster = Challenge(
    "Abja Trapmaster",
    "Exhausts 1 + 1 damage to random member.",
    Ability([
        AC(target.random_member, [exhaust, mod_stat(1, 'damage')]),
    ]),
    1, 6,
    exhaust_overcome,
)

abja_assassin = Challenge(
    "Abja Assassin",
    "Deals 4 damage to random exhausted",
    Ability([
        AC(target.random_exhausted, [mod_stat(4, 'damage')])
    ]),
    3, 4,
    exhaust_overcome
)

abja_horde = Challenge(
    "Abja Horde",
    "Exhaust the leader, -2 morale. Hard to overcome but gives supplies.",
    Ability([
        AC(target.leader, [exhaust, mod_stat(-2, 'morale')]),
    ]),
    6, 6,
    Ability([
        AC(target.all_assigned, [exhaust]),
        AC(target.party, [mod_resource(4, 'supplies')]),
    ])
)

watcher_crippler = Challenge(
    "Watcher Crippler",
    "Leader gets -2/-2.",
    Ability([
        AC(target.leader, [mod_stat(-2, 'base_physical'), mod_stat(-2, 'base_mental')])
    ]),
    0, 9,
    exhaust_overcome,
)

watcher_deathblade = Challenge(
    "Watcher Deathblade",
    "Leader gets -2 durability",
    Ability([
        AC(target.leader, [mod_stat(-2, 'durability')])
    ]),
    4, 5,
    exhaust_overcome
)

watcher_hexmage = Challenge(
    "Watcher Hexmage",
    "Everyone loses 2 morale.",
    Ability([
        AC(target.all_member, [mod_stat(-2, 'morale')]),
    ]),
    3, 6,
    exhaust_overcome
)

watcher_mindcrusher = Challenge(
    "Watcher Mindcrusher",
    "Random member set morale to -1 and increase recovery morale by 2",
    Ability([
        AC(target.random_member, [set_stat(-1, "morale"), mod_stat(2, "recovery_morale")])
    ]),
    2, 10,
    Ability([
        AC(target.all_assigned, [exhaust]),
        AC(target.random_assigned, [mod_stat(-1, 'recovery_morale')]),
    ])
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
    watcher_mindcrusher,
]