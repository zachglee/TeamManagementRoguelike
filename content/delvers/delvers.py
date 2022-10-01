from model.Delver import Delver
from model.Delver import DelverStats
from model.Ability import Ability
from model.Ability import AbilityComponent as AC
import content.targeters as target
from content.conditions import available, assigned, magic, no_magic, coin_flip, exhausted, damaged, leader, chance_
from content.effects import mod_stat, recover, exhaust, mod_resource, set_stat, mod_pm, mod_base_pm, reveal
import content.bonds as bonds

import random

# Dinae
import content.delvers.dinae as dinae

# Drael
import content.delvers.drael as drael

# Giza
import content.delvers.giza as giza

# Lestes
import content.delvers.lestes as lestes

# Vespern

# Enjek

# strong abilities from exhausted

# Mizzerat

# Lacraz

# Anzazi

# Ashka

# ashka_the_prince = Delver(
#     "Ashka the Prince",
#     DelverStats(1, 1, 1, 1, 1, 1, supplies=10),
#     Ability([AC(target.self, [])]),
#     Ability([AC(target.self, [mod_stat(1, 'morale')])])
# )
#
# ava_the_princess = Delver(
#     "Ava the Princess",
#     DelverStats(2, 2, 0, 0, 1, 2),
#     Ability([AC(target.self, [mod_stat(1, 'morale')])], conditions=[available]),
#     Ability([
#         AC(target.self, [mod_stat(-1, 'morale')]),
#         AC(target.all_assigned, [mod_stat(2, 'morale'), mod_stat(2, 'physical'), mod_stat(2, 'mental')]),
#     ])
# )
#
# ram_the_trainer = Delver(
#     "Ram the Trainer",
#     DelverStats(3, 2, 1, 0, 2, 2),
#     Ability([AC(target.leader, [mod_stat(1, 'base_physical')])], conditions=[available]),
#     Ability([AC(target.random_assigned, [mod_stat(1, 'durability')])])
# )
#
# esper_the_mentor = Delver(
#     "Esper the Mentor",
#     DelverStats(1, 4, 2, 0, 1, 1),
#     Ability([AC(target.leader, [mod_stat(1, 'base_mental')])], conditions=[available]),
#     Ability([AC(target.random_available, [mod_stat(-1, 'recovery_morale')])])
# )
#
# # kell_the_guardian = Delver(
# #     "Kell the Guardian",
# #     DelverStats(3, 3, 0, 1, 2, 2),
# #     Ability([])
# # )
#
# # shiva_the_bodyguard = Delver(
# #     "Shiva the Bodyguard",
# #     DelverStats(6, 1, 0, 0, 4, 2),
# #     Ability([AC(target.leader, [mod_stat(-2, 'damage'), mod_stat(1)])], conditions=[available]),
# #     Ability([
# #         AC(target.self, [mod_stat(1, 'damage')]),
# #         AC(target.all_available, [mod_stat(-1, 'damage')]),
# #     ])
# # )
#
#
#

# giri_the_blacksmith = Delver(
#     "Giri the Blacksmith",
#     DelverStats(3, 3, 0, 0, 2, 2),
#     Ability([
#         AC(target.random_available, [mod_base_pm(3, 0)])
#     ])
# )

# giradhin_the_seer = Delver(
#     "Giradhin the Seer",
#     DelverStats(0, 6, 1, 1, 1, 2),
#     Ability([AC(target.random_adjacent_hidden, [reveal])], conditions=[available, magic]),
#     Ability([AC(target.all_adjacent_hidden, [reveal])], conditions=[magic]),
#     bonds.leader_when_endure
# )

#
# pharah_the_dismantler = Delver(
#     "Pharah the Dismantler",
#     DelverStats()
# )

# misc

# voz_the_skirmisher = Delver(
#     "Voz the Skirmisher",
#     DelverStats(5, 4, 0, 0, 2, 3),
#     Ability([AC(target.self, [])], conditions=[available]),
#     Ability([AC(target.self, [mod_stat(2, 'morale')])])
# )

# -------- M A G I C

# selene_the_shapeshifter = Delver(
#     "Selene the Shapeshifter",
#     DelverStats(2, 2, 0, 1, 1, 2),
#     Ability([
#         AC(target.self, [set_stat(6, 'base_physical'), set_stat(6, 'base_mental')], conditions=[magic])]),
#         AC(target.self, [set_stat(2, 'base_physical'), set_stat(2, 'base_mental')], conditions=[no_magic]),
#     ]),
#     Ability([
#
#     ]),
# )

# Lacrata - big stats, reducing enemy stats?
# Bonding Theme: They respect magical power, and they respect martial power. Selfish. individualist

# tera_the_battlemage = Delver(
#     "Tera the Battlemage",
#     DelverStats(4, 3, 0, 1, 2, 2),
#     Ability([AC(target.self, [mod_stat(2, 'physical'), mod_stat(2, 'mental')])], conditions=[assigned, magic]),
#     Ability([
#         AC(target.self, [mod_stat(1, 'base_physical'), mod_stat(1, 'base_mental')]),
#         AC(target.party, [mod_resource(-1, 'magic')])
#     ], conditions=[magic])
# )
#
# fiona_the_arcane_archer = Delver(
#     "Fiona the Arcane Archer",
#     DelverStats(3, 4, 0, 1, 2, 2),
#     Ability([AC(target.)])
# )
#
# tywin_the_pyromancer = Delver(
#     "Tywin the Pyromancer",
#     DelverStats(1, 6, 0, 1, 1, 2),
#     Ability([AC(target, [])], conditions=[available])
# )
#
# # grima
#
# viren_the_vampiric = Delver(
#     "Viren the Vampiric",
#     DelverStats(3, 3, 0, 0, 1, 2),
#     Ability([
#         AC(target.self, [mod_pm(-1, 0)]),
#         AC(target.party, [mod_resource(1, 'magic')])
#     ], conditions=[available]),
#     Ability([AC(target.random_exhausted, [mod_pm(0, -1)])])
# )

# shinya_the_hexblade = Delver(
#     "Shinya the Hexblade",
#
# )
#
# ravi_the_sorceress = Delver(
#     "Ravi the Sorceress",
#     Ability([AC(target.)])
# )

# baric_the_cleric = Delver(
#     "Baric the Cleric",
#     DelverStats(2, 5, 1, 2, 2, 3),
#     Ability([AC(target.random_exhausted, [])])
# )

delvers = dinae.delvers + drael.delvers + giza.delvers + lestes.delvers

# delvers = [
#     # Ashka
#     ashka_the_prince,
#     ava_the_princess,
#     # alise_the_bodyguard,
#     ram_the_trainer,
#     esper_the_mentor,
#     #
#     voz_the_skirmisher,
#     maya_the_scavenger,
#     tera_the_battlemage,
# ] + dinae.delvers + drael.delvers