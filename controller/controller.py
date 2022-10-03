import random
from view.TextView import delver_to_string, render_game_state, challenge_to_string
from content.targeters import choose_available, choose_assigned, choose_accessible_location
# from utils.generation import
from model.Party import Party

# a Game has a GameState, and a bunch of helpers to manipulate the GameState

class Game:
    def __init__(self, game_state):
        self.game_state = game_state

    # -------- A T O M I C   H E L P E R S -------- #

    def render(self):
        render_game_state(self.game_state)

    def prompt(self, message="Enter to continue."):
        input(message)

    # -------- R E S O L V E R   H E L P E R S -------- #
    # Resolvers execute steps that happen without explicit user input

    def _resolve_expedition_end(self):
        self.game_state.party = Party([], 0)
        self.game_state.embarked = False
        self.game_state.add_delvers_to_resource_pool(3)
        for challenge in self.game_state.challenges:
            if challenge.name != 'Inactive Area': challenge.active = True

    def _resolve_expedition_failure(self, description):
        print(description)
        self._resolve_expedition_end()

    def _resolve_expedition_success(self, description):
        print(description)
        living_party_members = [member for member in self.game_state.party.members if not member.dead]
        self.game_state.surviving_resources.delvers += living_party_members
        self.game_state.surviving_resources.supplies += self.game_state.party.supplies
        self._resolve_expedition_end()

    def _resolve_cleanup(self):
        # cleanup delvers
        for delver in self.game_state.party.members:
            delver.assigned = False
            delver.stats.physical = delver.stats.base_physical
            delver.stats.mental = delver.stats.base_mental
            delver.stats.recovery_morale = max(0, delver.stats.recovery_morale)
            if delver.exhausted and any(delver.leader for delver in delver.bonds):
                delver.stats.morale += 1
            if delver.should_exhaust():
                delver.exhaust()
            # NOTE: Trying ou moving away from inspire, since it dilutes the uniqueness of resting
            # as the time where you can get back exhausted delvers
            # if delver.should_inspire():
            #     delver.recover(morale_cost=delver.recovery_morale * 2)
            if delver.should_die():
                delver.die()

        # cleanup challenges
        for challenge in self.game_state.challenges:
            challenge.required_physical = challenge.base_required_physical
            challenge.required_mental = challenge.base_required_mental

        # check to see if the expedition ends
        if self.game_state.party.supplies < 0:
            description = 'You ran out of supply. You failed.'
            self._resolve_expedition_failure(description)
        elif all([m.dead for m in self.game_state.party.members]):
            description = 'All party members died. You failed.'
            self._resolve_expedition_failure(description)
        elif (self.game_state.party.location == (self.game_state.width - 1, self.game_state.height - 1)
              and not self.game_state.current_challenge.active):
            self._resolve_expedition_success("You reached the destination!")

        self.prompt()

    def _resolve_plan(self):
        # first all the abilities happen
        for delver in self.game_state.party.followers():
            delver.execute_follower_ability(self.game_state)
        self.game_state.party.leader().execute_leader_ability(self.game_state)

        # then check if you overcome the challenge
        challenge = self.game_state.current_challenge
        if challenge.is_overcome_by(self.game_state):
            challenge.mark_overcome() # TODO find a better name
            challenge.execute_overcome_ability(self.game_state)
        else:
            challenge.execute_endure_ability(self.game_state)

        # execute any bonding
        for delver in self.game_state.party.members:
            delver.execute_bonding(self.game_state)

        self.game_state.current_challenge.active = False
        self.prompt()

    def _resolve_rest(self):
        for member in self.game_state.party.members:
            member.mod_stat(1, 'morale')
            if member.should_recover():
                member.recover(morale_cost=member.recovery_morale)
        # TODO maybe some other stuff like relationship building
        self.prompt()


    # -------- P H A S E S   H E L P E R S -------- #
    # Phases do the work of prompting the user for input and then calling the proper resolvers

    def _embarking_phase(self):
        while True:
            self.render()
            command = input("recruit, supply, or done: ")
            command_tokens = command.split(' ')
            command_root = command_tokens[0]
            command_arguments = command_tokens[1:]
            if command_root == "recruit":
                available_delvers = []
                for _ in range(3):
                    i = random.choice(range(0, len(self.game_state.delver_pool)))
                    available_delvers.append(self.game_state.delver_pool.pop(i))
                self.draft_delver(available_delvers)
                # NOTE: Moving away from this
                # if command_arguments == []:
                #     print(f"Must provide the # of the Delver to recruit, like `recruit 3`")
                #     continue
                # i = int(command_arguments[0]) - 1
                # available_delvers = self.game_state.starting_resources.delvers
                # chosen_delver = available_delvers.pop(i)
                # self.game_state.add_delver_to_party(chosen_delver)
            if command_root == "supply":
                # TODO make sure they can't go negative on taking supply
                if command_arguments == []:
                    print(f"Must provide the amount of supply to bring, like `supply 3`")
                    continue
                amount = int(command_arguments[0])
                self.game_state.party.supplies += amount
                self.game_state.starting_resources.supplies -= amount
            if command_root == "done":
                print("Ok, embarking! Choose your starting leader.")
                new_leader = choose_available(self.game_state)[0]
                new_leader.lead()
                self.game_state.embarked = True
                return

    def _planning_phase(self):
        self.game_state.current_challenge.revealed = True
        while True:
            self.render()
            print("GAME: The Challenge is still active, you must deal with it!")
            command = input("assign, unassign, map, or done: ")
            if command == "assign":
                delver = choose_available(self.game_state)[0]
                delver.assign()
            if command == "unassign":
                delver = choose_assigned(self.game_state)[0]
                delver.assigned = False
            if command == "map":
                coordinates_raw = input("Enter coordinates separated by a comma like so: 1,2: ")
                coordinates = coordinates_raw.split(',')
                x, y = (int(coordinates[0]), int(coordinates[1]))
                challenge = self.game_state.layout[x][y]
                print(challenge_to_string(challenge) if challenge.revealed else "---- HIDDEN ----")
                self.prompt()
            if command == "done":
                self._resolve_plan()
                return

    def _travel_phase(self):
        while True:
            self.render()
            print("GAME: The challenge here has been dealt with for now.")
            command = input("travel, rest, or map: ")
            if command == "travel":
                if self.game_state.party.leader():
                    location = choose_accessible_location(self.game_state)[0]
                    self.game_state.party.location = location
                    break
                else:
                    input("You have no leader. You must rest and assign a new one.")
            if command == "rest":
                old_leader = self.game_state.party.leader()
                if old_leader:
                    old_leader.lead(leader=False)
                new_leader = choose_available(self.game_state)[0]
                new_leader.lead()
                self._resolve_rest()
                break
            if command == "map":
                coordinates_raw = input("Enter coordinates separated by a comma like so: 1,2: ")
                coordinates = coordinates_raw.split(',')
                x, y = (int(coordinates[0]), int(coordinates[1]))
                challenge = self.game_state.layout[x][y]
                print(challenge_to_string(challenge) if challenge.revealed else "---- HIDDEN ----")
                self.prompt()
        self.game_state.party.supplies -= len([m for m in self.game_state.party.members if not m.dead])

    def draft_delver(self, delver_choices):
        if len(delver_choices) == 0: return None
        chosen_delver = None
        while chosen_delver is None:
            print(f"Choose one to recruit:")
            for i, delver in enumerate(delver_choices):
                print(f"{i + 1}: {delver_to_string(delver)}")
            user_choice = input("\n Choose one by index: ")
            if not user_choice.isnumeric():
                print(f"Input must be a valid number.")
                continue
            i = int(user_choice) - 1
            if i in range(0, len(delver_choices)):
                chosen_delver = delver_choices[i]
        self.game_state.add_delver_to_party(chosen_delver)

    # -------- M A I N   L O O P -------- #

    def next(self):
        if self.game_state.embarked:
            if self.game_state.current_challenge.active:
                self._planning_phase()
            else:
                self._travel_phase()
            self._resolve_cleanup()
        else:
            self._embarking_phase()


    def play(self):
        while True:
            self.next()



