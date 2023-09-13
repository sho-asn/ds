from poke_team import PokeTeam
from queue_adt import CircularQueue
from referential_array import ArrayR
from pokemon import MissingNo
from random import random

"""
Battle Class

The class contains three methods set_mode_battle, rotating_mode_battle and optimised_mode_battle which are different
ways of battling. After player chooses a battle team follows these concepts to fight the battle depending on the ADT 
that battle mode uses.
"""


class Battle():

    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        """
        Constructor for Battle object
        best case = worst case = O(1)
        """
        if not (isinstance(trainer_one_name, str)):
            raise TypeError("Name of trainer one must be of string type")
        if not (isinstance(trainer_two_name, str)):
            raise TypeError("Name of trainer two must be of string type")
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)
        self.team1.set_battle_mode(0)
        self.team2.set_battle_mode(0)

    def set_mode_battle(self) -> str:
        """
        When the battle mode is 0, pokemon fight until a team doesn't have pokemon in the team.
        Pokemon of two teams fight each other until one of them faints and the next pokemon from stack comes.
        It returns the trainer name that wins the battle, Draw otherwise.
        best case = O(n)
        worst case = O(n**2)
        """

        print("CHOOSE POKEMON FOR TEAM 1")
        self.team1.choose_team(0)
        print("CHOOSE POKEMON FOR TEAM 2")
        self.team2.choose_team(0)
        round_num = 1

        while self.team1.team.is_empty() == False and self.team2.team.is_empty() == False:

            poke1 = self.team1.team.pop()
            poke2 = self.team2.team.pop()

            if poke1.faster_than(poke2):
                poke2.attacked_by(poke1)
                if poke2.alive():
                    poke1.attacked_by(poke2)

            elif poke2.faster_than(poke1):
                poke1.attacked_by(poke2)
                if poke1.alive():
                    poke2.attacked_by(poke1)

            else:
                if isinstance(poke1, MissingNo) and not (isinstance(poke2, MissingNo)):
                    poke2.attacked_by(poke1)
                    poke1.attacked_by(poke2)
                elif isinstance(poke2, MissingNo) and not (isinstance(poke1, MissingNo)):
                    poke1.attacked_by(poke2)
                    poke2.attacked_by(poke1)
                elif isinstance(poke1, MissingNo) and isinstance(poke2, MissingNo):
                    rng1 = int(random() * 4)
                    rng2 = int(random() * 4)
                    if rng1 == 0 and rng2 == 0:
                        poke1.superpower()
                        poke2.superpower()
                    elif rng1 == 0 and rng2 != 0:
                        poke2.reduce_HP(poke2.damage_taken(poke1))
                        poke1.superpower()
                    elif rng1 != 0 and rng2 == 0:
                        poke1.reduce_HP(poke1.damage_taken(poke2))
                        poke2.superpower()
                    else:
                        poke1.reduce_HP(poke1.damage_taken(poke2))
                        poke2.reduce_HP(poke2.damage_taken(poke1))
                else:
                    poke2.attacked_by(poke1)
                    poke1.attacked_by(poke2)

            if poke1.alive() and poke2.faint():
                poke1.level_up()
                print("Round " + str(
                    round_num) + ": Team 1's " + poke1.get_name() + " faints Teams 2's " + poke2.get_name())

            elif poke1.faint() and poke2.alive():
                poke2.level_up()
                print("Round " + str(
                    round_num) + ": Team 1's " + poke1.get_name() + " is fainted by Teams 2's " + poke2.get_name())

            elif poke1.alive() and poke2.alive():
                poke1.reduce_HP(1)
                poke2.reduce_HP(1)
                if poke1.alive() and poke2.faint():
                    poke1.level_up()
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " faints Teams 2's " + poke2.get_name())
                elif poke1.faint() and poke2.alive():
                    poke2.level_up()
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " is fainted by Teams 2's " + poke2.get_name())
                elif poke1.alive() and poke2.alive():
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " fights Teams 2's " + poke2.get_name() + ", BOTH ALIVE`")
                elif poke1.faint() and poke2.faint():
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " fights Teams 2's " + poke2.get_name() + ", BOTH FAINT`")

            elif poke1.faint() and poke2.faint():
                print("Round " + str(
                    round_num) + ": Team 1's " + poke1.get_name() + " fights Teams 2's " + poke2.get_name() + ", BOTH FAINT`")

            if poke1.alive():
                self.team1.team.push(poke1)
            if poke2.alive():
                self.team2.team.push(poke2)
            round_num += 1

        if self.team1.team.is_empty() and not self.team2.team.is_empty():
            return self.team2.trainer

        elif not self.team1.team.is_empty() and self.team2.team.is_empty():
            return self.team1.trainer

        elif self.team1.team.is_empty() and self.team2.team.is_empty():
            return "Draw"

    def rotating_mode_battle(self) -> str:
        """
        When the battle mode is 1, trainers fight until a team doesn't have pokemon in the team.
        Each pokemon of teams can attack once per a round. If the pokemon is still alive,
        the Pokemon will be added as the last element of the list.
        It returns the trainer name that wins the battle, Draw otherwise.
        best case = O(n)
        worst case = O(n**2)
        """
        print("CHOOSE POKEMON FOR TEAM 1")
        self.team1.choose_team(1)
        print("CHOOSE POKEMON FOR TEAM 2")
        self.team2.choose_team(1)
        round_num = 1

        while self.team1.team.is_empty() == False and self.team2.team.is_empty() == False:

            poke1 = self.team1.team.serve()
            poke2 = self.team2.team.serve()

            if poke1.faster_than(poke2):
                poke2.attacked_by(poke1)
                if poke2.alive():
                    poke1.attacked_by(poke2)

            elif poke2.faster_than(poke1):
                poke1.attacked_by(poke2)
                if poke1.alive():
                    poke2.attacked_by(poke1)

            else:
                if isinstance(poke1, MissingNo) and not (isinstance(poke2, MissingNo)):
                    poke2.attacked_by(poke1)
                    poke1.attacked_by(poke2)
                elif isinstance(poke2, MissingNo) and not (isinstance(poke1, MissingNo)):
                    poke1.attacked_by(poke2)
                    poke2.attacked_by(poke1)
                elif isinstance(poke1, MissingNo) and isinstance(poke2, MissingNo):
                    rng1 = int(random() * 4)
                    rng2 = int(random() * 4)
                    if rng1 == 0 and rng2 == 0:
                        poke1.superpower()
                        poke2.superpower()
                    elif rng1 == 0 and rng2 != 0:
                        poke2.reduce_HP(poke2.damage_taken(poke1))
                        poke1.superpower()
                    elif rng1 != 0 and rng2 == 0:
                        poke1.reduce_HP(poke1.damage_taken(poke2))
                        poke2.superpower()
                    else:
                        poke1.reduce_HP(poke1.damage_taken(poke2))
                        poke2.reduce_HP(poke2.damage_taken(poke1))
                else:
                    poke2.attacked_by(poke1)
                    poke1.attacked_by(poke2)

            if poke1.alive() and poke2.faint():
                poke1.level_up()
                print("Round " + str(
                    round_num) + ": Team 1's " + poke1.get_name() + " faints Teams 2's " + poke2.get_name())

            elif poke1.faint() and poke2.alive():
                poke2.level_up()
                print("Round " + str(
                    round_num) + ": Team 1's " + poke1.get_name() + " is fainted by Teams 2's " + poke2.get_name())

            elif poke1.alive() and poke2.alive():
                poke1.reduce_HP(1)
                poke2.reduce_HP(1)
                if poke1.alive() and poke2.faint():
                    poke1.level_up()
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " faints Teams 2's " + poke2.get_name())
                elif poke1.faint() and poke2.alive():
                    poke2.level_up()
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " is fainted by Teams 2's " + poke2.get_name())
                elif poke1.alive() and poke2.alive():
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " fights Teams 2's " + poke2.get_name() + ", BOTH ALIVE`")
                elif poke1.faint() and poke2.faint():
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " fights Teams 2's " + poke2.get_name() + ", BOTH FAINT`")

            elif poke1.faint() and poke2.faint():
                print("Round " + str(
                    round_num) + ": Team 1's " + poke1.get_name() + " fights Teams 2's " + poke2.get_name() + ", BOTH FAINT`")

            if poke1.alive():
                self.team1.team.append(poke1)
            if poke2.alive():
                self.team2.team.append(poke2)
            round_num += 1

        if self.team1.team.is_empty() and not self.team2.team.is_empty():
            return self.team2.trainer

        elif not self.team1.team.is_empty() and self.team2.team.is_empty():
            return self.team1.trainer

        elif self.team1.team.is_empty() and self.team2.team.is_empty():
            return "Draw"

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """
        When the battle mode is 2, trainers fight until a team doesn't have pokemon in the team.
        In this method, the order of Pokemon is always sorted according to the value of criterion.
        Each pokemon of teams can attack once per a round. If the pokemon is still alive,
        the Pokemon will be added to the list according to the value of the criterion.
        It returns the trainer name that wins the battle, Draw otherwise.
        best case = O(n)
        worst case = O(n**2)
        """
        print("CHOOSE POKEMON FOR TEAM 1")
        self.team1.choose_team(2, criterion_team1)
        print("CHOOSE POKEMON FOR TEAM 2")
        self.team2.choose_team(2, criterion_team2)
        round_num = 1

        while self.team1.team.is_empty() == False and self.team2.team.is_empty() == False:

            poke1 = self.team1.team.serve()
            poke2 = self.team2.team.serve()

            if poke1.faster_than(poke2):
                poke2.attacked_by(poke1)
                if poke2.alive():
                    poke1.attacked_by(poke2)

            elif poke2.faster_than(poke1):
                poke1.attacked_by(poke2)
                if poke1.alive():
                    poke2.attacked_by(poke1)

            else:
                if isinstance(poke1, MissingNo) and not (isinstance(poke2, MissingNo)):
                    poke2.attacked_by(poke1)
                    poke1.attacked_by(poke2)
                elif isinstance(poke2, MissingNo) and not (isinstance(poke1, MissingNo)):
                    poke1.attacked_by(poke2)
                    poke2.attacked_by(poke1)
                elif isinstance(poke1, MissingNo) and isinstance(poke2, MissingNo):
                    rng1 = int(random() * 4)
                    rng2 = int(random() * 4)
                    if rng1 == 0 and rng2 == 0:
                        poke1.superpower()
                        poke2.superpower()
                    elif rng1 == 0 and rng2 != 0:
                        poke2.reduce_HP(poke2.damage_taken(poke1))
                        poke1.superpower()
                    elif rng1 != 0 and rng2 == 0:
                        poke1.reduce_HP(poke1.damage_taken(poke2))
                        poke2.superpower()
                    else:
                        poke1.reduce_HP(poke1.damage_taken(poke2))
                        poke2.reduce_HP(poke2.damage_taken(poke1))
                else:
                    poke2.attacked_by(poke1)
                    poke1.attacked_by(poke2)

            if poke1.alive() and poke2.faint():
                poke1.level_up()
                print("Round " + str(
                    round_num) + ": Team 1's " + poke1.get_name() + " faints Teams 2's " + poke2.get_name())

            elif poke1.faint() and poke2.alive():
                poke2.level_up()
                print("Round " + str(
                    round_num) + ": Team 1's " + poke1.get_name() + " is fainted by Teams 2's " + poke2.get_name())

            elif poke1.alive() and poke2.alive():
                poke1.reduce_HP(1)
                poke2.reduce_HP(1)
                if poke1.alive() and poke2.faint():
                    poke1.level_up()
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " faints Teams 2's " + poke2.get_name())
                elif poke1.faint() and poke2.alive():
                    poke2.level_up()
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " is fainted by Teams 2's " + poke2.get_name())
                elif poke1.alive() and poke2.alive():
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " fights Teams 2's " + poke2.get_name() + ", BOTH ALIVE`")
                elif poke1.faint() and poke2.faint():
                    print("Round " + str(
                        round_num) + ": Team 1's " + poke1.get_name() + " fights Teams 2's " + poke2.get_name() + ", BOTH FAINT`")

            elif poke1.faint() and poke2.faint():
                print("Round " + str(
                    round_num) + ": Team 1's " + poke1.get_name() + " fights Teams 2's " + poke2.get_name() + ", BOTH FAINT")

            temp1 = CircularQueue(6)
            if poke1.alive():
                temp1.append(poke1)
            while (not (self.team1.team.is_empty())):
                temp1.append(self.team1.team.serve())
            self.team1.team = temp1

            if self.team1.team.is_empty() == False:
                temp1 = ArrayR(len(self.team1.team))
                for i in range(len(self.team1.team)):
                    temp1[i] = self.team1.team.serve()
                temp1.bubble_sort(self.team1.get_criterion())
                for i in range(len(temp1)):
                    self.team1.team.append(temp1[i])

            temp2 = CircularQueue(6)
            if poke2.alive():
                temp2.append(poke2)
            while (not (self.team2.team.is_empty())):
                temp2.append(self.team2.team.serve())
            self.team2.team = temp2

            if self.team2.team.is_empty() == False:
                temp2 = ArrayR(len(self.team2.team))
                for i in range(len(self.team2.team)):
                    temp2[i] = self.team2.team.serve()
                temp2.bubble_sort(self.team2.get_criterion())
                for i in range(len(temp2)):
                    self.team2.team.append(temp2[i])

            round_num += 1

            if self.team1.team.is_empty() and not self.team2.team.is_empty():
                return self.team2.trainer

            elif not self.team1.team.is_empty() and self.team2.team.is_empty():
                return self.team1.trainer

            elif self.team1.team.is_empty() and self.team2.team.is_empty():
                return "Draw"
