# effects are simple functions to compose abilities from
# They are targets->side effects
# Different kinds of effects will have different kinds of targets so we have to be mindful

# ------- Effects targeting delvers

def mod_stat(amount, stat_key):
    def effect(target_delvers):
        for delver in target_delvers:
            delver.mod_stat(amount, stat_key)
    return effect

def mod_pm(physical, mental):
    def effect(target_delvers):
        for delver in target_delvers:
            delver.mod_stat(physical, 'physical')
            delver.mod_stat(mental, 'mental')
    return effect

def mod_base_pm(base_physical, base_mental):
    def effect(target_delvers):
        for delver in target_delvers:
            delver.mod_stat(base_physical, 'base_physical')
            delver.mod_stat(base_mental, 'base_mental')
    return effect

def set_stat(value, stat_key):
    def effect(target_delvers):
        for delver in target_delvers:
            delver.mod_stat(value, stat_key)
    return effect

def exhaust(target_delvers):
    for delver in target_delvers:
        delver.exhaust()

def recover(target_delvers):
    for delver in target_delvers:
        delver.exhaust(exhausted=False)

# ------- Effects targeting parties

def mod_resource(amount, resource_key):
    def effect(target_party):
        target_party.mod_resource(amount, resource_key)
    return effect

# -------- Effects targeting challenges

def reveal(target_challenges):
    for challenge in target_challenges:
        challenge.revealed = True

def mod_challenge_pm(physical, mental):
    def effect(target_challenges):
        for challenge in target_challenges:
            challenge.required_physical += physical
            challenge.required_mental += mental
    return effect

def mod_challenge_base_pm(physical, mental):
    def effect(target_challenges):
        for challenge in target_challenges:
            challenge.base_required_physical += physical
            challenge.base_required_mental += mental
    return effect

