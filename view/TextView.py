from view.utils import print_side_by_side

# -------- H E L P E R S -------- #

def delver_to_string(delver):
    statuses = []
    if delver.leader: statuses.append("Leader")
    if delver.exhausted: statuses.append("Exhausted")
    if delver.assigned: statuses.append("Assigned")
    if delver.dead: statuses.append("DEAD")
    return (f"  ------ {delver.name} ({','.join(statuses)}) ------\n"
            f"    P/M: {delver.stats.physical}/{delver.stats.mental}, "
            f"Morale: {delver.stats.morale}/{delver.recovery_morale}, "
            f"Damage: {delver.stats.damage}/{delver.stats.durability}\n"
            f"    Bonds: {[b.name for b in delver.bonds]}\n"
            f"    {delver.flavor}")

def party_to_string(party):
    acc = f"******** Location: {party.location}, Supplies: {party.supplies}, Magic: {party.magic} ********"
    for member in party.members:
        acc += f"\n{delver_to_string(member)}"
    return acc

def challenge_to_string(challenge):
    return (f"!!!!!!!! {challenge.name} !!!!!!!!\n"
            f"  {challenge.description}\n"
            f"  P/M: {challenge.required_physical}/{challenge.required_mental}")

def layout_to_string(layout, party_location):
    def to_symbol(challenge):
        return 'X' if challenge.impassible else '?' if not challenge.revealed else '-' if not challenge.active else '+'
    x, y = party_location
    symbol_layout = [[to_symbol(challenge) for challenge in row] for row in layout]
    symbol_layout[x][y] = 'P'
    string_layout = "\n".join(["  ".join(row) for row in symbol_layout])
    return f"________ Zone ________\n{string_layout}"

# -------- M A I N -------- #

def render_game_state(game_state):
    if game_state.embarked:
        layout_string = layout_to_string(game_state.layout, game_state.party.location)
        challenge_string = challenge_to_string(game_state.current_challenge)
        world_string = f"{layout_string}\n{challenge_string}"
        party_string = party_to_string(game_state.party)
        print_side_by_side(party_string, world_string)
        print('')
    else:
        delvers = game_state.starting_resources.delvers
        pool = f"******** Supply Pool: {game_state.starting_resources.supplies} ********"
        for delver, i in zip(delvers, range(len(delvers))):
            pool += f"\n{i+1}: {delver_to_string(delver)}\n"

        party = party_to_string(game_state.party)
        print_side_by_side(party, pool)
        print('')

