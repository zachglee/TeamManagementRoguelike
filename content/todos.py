
# Coming back to this!
# - make enemy design more spiky so that enemies really ask certain things of you
# - make delver abilities change more between follower / leader so that choice matters more

# Playtest 2:
# - It needs to be more of an interesting choice who to assign to a challenge...
# - Right now you basically just assign whoever whoever is good at assigning and you just keep assigning them because everyone recovers so fast
# - The exhaust system is supposed to make it so that you have to wait a bit before you use someone again?
# - Maybe I should say the leader bonus is that you recover 1 morale while exhausted and you're bonded to leader.
# - Yeah lets see what that does to things?
# - It still doesn't resolve the imbalance of some folks just really wanting to be assigned or not assigned...
# - ...
# - Ok that was a little better -- there was more downtime though I still had a lot of uptime bc of my build. Helen is really strong. I also rested a bunch.
# - I should implement my branching paths idea instead of map
# - I did use everyone as a leader at some point, except for Helen? Used rafi for magic, used jon as placeholder, used Lina to buff... never used maya though...

# Playtest Notes
# - Ok so overall having leaders that that stat boost is really good
# - having morale engines is good. And there's only so many of those I can make
# - You should consider putting everyone in leader role eventually
# - I need more things to push leaders out then?
# - Using info from past runs and choosing route wasn't really a thing.
# - I should make it 50% chance that route becomes impassible?
# - Bonds should feel more significant -- they can give stat boosts maybe?
# - maybe more monsters should actually be harder to defeat?
# - maybe party size should be slightly bigger? Ok I just made it optional and it just takes different amounts of supply
# - I think I still need to lean more into 

# Content:
# TODO ability where your mental becomes your physical
# -----
# TODO also just implement more enemies and delvers
# TODO also another low-hanging fruit -- implement modification of challenge physical/mental
# TODO implement status effects? Status effects are updated / happen during cleanup
# - Delver has list of Status Effects
# - Delver has execute status effects method that runs during cleanup, which runs and removes any stale ones
# - A Status effect for now is just 2 effects separated by a timer. Initial effect then end effect.
# TODO implement temporary vs base for all stats (durability, recovery cost, etc)
# TODO implement passives + triggered abilities
# - how would I implement triggers?
# - Ultimately I think I would need to hardcode what kinds of triggers are valid
# - I could hardcode on rest / overcome?
# - So then the 'effect' of that ability would be to restTrigger(effect)
# - or maybe it needs to be like an event hook?
# - ehh maybe just for now explore the design space I do have...
# - ok no wait -- when the controller notices an event happens,
#   it calls execute_trigger_ability(trigger) on every delver in the party,
#   then that function just searches the abilities for ones that have the trigger,
#
# - hmm wait what would be more flexible is if i could encode all triggers as
#   predicates on the game state? Or like they operate on a transition from
#   one game state to another so they can see the change?
#   Hmm yeah having triggers is actually quite complex... I feel like it would
#   require a big re-design in the model? Like essentially you need to know the
#   history of what happened, so maintain a chain of game states,
#   and you need to know what's about to happen?
#   Ehh but that forces me into a functional design and i kind of like the imperative...
#   What if every state_change function, whether a method of a class, or something that
#   takes in a game_state, returns an 'event' object that describes what just happened?
#   That filters back up to the controller level where it gets emitted to every ability.
#   It's this description of a state change that occurred, and it can be rendered
#   and then other things can trigger off of it? So then triggers are simply take in
#   a game state and an event and return True or False.
# - There could be various Event classes that inherit from a parent Event class,
#   and they could each be rendered in a different way.
#   Oh and I guess they could also handle the mutation themselves?
#   I mean that's kind of the job of effects
# TODO implement abilities that trigger on rest / overcome?


# Gameplay:
# TODO implement the actual full game loop of assembling the party, going through, then doing it again

# Quality of Life:
# TODO implement automatic descriptions of abilities based on targeters
# TODO implement the option to get an in-depth description of objects
