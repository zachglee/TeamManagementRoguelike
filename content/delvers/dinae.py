from model.Delver import Delver
from model.Delver import DelverStats
from model.Ability import Ability
from model.Ability import AbilityComponent as AC
import content.targeters as target
from content.conditions import available, assigned, chance_, challenge_overcome, coin_flip, exhausted
from content.effects import mod_stat, recover, exhaust, mod_resource, set_stat, mod_pm, mod_base_pm
import content.bonds as bonds

# Kingdom of Dinae
# Bond Theme: respecting others carrying the team when you're down and out

leader_when_exhausted = target.if_([exhausted, chance_(0.33)], target.leader)
fellow_assigned = target.if_([assigned, coin_flip, challenge_overcome], target.random_other_assigned)

ray_the_commander = Delver(
    "Ray the Commander",
    DelverStats(4, 2, 1, 0, 2, 2),
    follower_ability=Ability([AC(target.random_assigned, [mod_pm(1, 1)])], conditions=[available]),
    leader_ability=Ability([AC(target.random_assigned, [mod_pm(2, 2)])]),
    bonding_targeter=bonds.leader_when_exhausted,
    flavor="'They're on the retreat -- don't let up, soldier!'"
)

bella_the_captain = Delver(
    "Bella the Captain",
    DelverStats(2, 4, 2, 0, 1, 2),
    follower_ability=Ability([AC(target.random_available, [mod_stat(1, 'morale')])], conditions=[available]),
    leader_ability=Ability([AC(target.all_assigned, [mod_stat(2, 'morale')])]),
    bonding_targeter=bonds.leader_when_exhausted,
    flavor="'Keep your spirits up, friends. We'll make it through this.'"
)

jon_the_medic = Delver(
    "Jon the Medic",
    DelverStats(2, 4, 2, 0, 1, 2),
    follower_ability=Ability([AC(target.random_exhausted, [mod_stat(-1, 'damage'), mod_stat(1, 'morale')])], conditions=[available]),
    leader_ability=Ability([AC(target.all_exhausted, [mod_stat(-1, 'damage'), mod_stat(1, 'morale')])]),
    bonding_targeter=bonds.leader_when_exhausted,
    flavor="'You fought well. Now let's you patched up.'"
)

baric_the_soldier = Delver(
    "Baric the Soldier",
    DelverStats(5, 1, 2, 0, 3, 3),
    follower_ability=Ability([AC(target.self, [mod_stat(-1, 'morale'), mod_pm(2, 2)], conditions=[assigned])]),
    leader_ability=Ability([AC(target.self, [mod_stat(1, 'durability'), mod_stat(-1, 'morale')])]),
    bonding_targeter=bonds.fellow_assigned,
    flavor="'There's no stopping a man with something to believe in.'"
)

lina_the_trainee = Delver(
    "Lina the Trainee",
    DelverStats(1, 4, 1, 0, 1, 2),
    follower_ability=Ability([AC(target.self, [mod_stat(1, 'base_physical')])], conditions=[available]),
    leader_ability=Ability([AC(target.self, [mod_stat(1, 'base_mental')])]),
    bonding_targeter=bonds.fellow_assigned,
    flavor="'One day, I'll be like her... One day...'"
)

jayden_the_trooper = Delver(
    "Jayden the Trooper",
    DelverStats(3, 3, 2, 0, 2, 2),
    follower_ability=Ability([AC(target.self, [recover, mod_stat(-1, 'morale')], conditions=[exhausted])]),
    leader_ability=Ability([AC(target.random_exhausted, [recover, mod_stat(-2, 'morale')])]),
    bonding_targeter=bonds.fellow_assigned,
    flavor="'I can rest when I'm dead. They need my help now.'"
)

delvers = [
    jon_the_medic,
    ray_the_commander,
    jayden_the_trooper,
    baric_the_soldier,
    bella_the_captain,
    lina_the_trainee,
]