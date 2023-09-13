from pokemon import Charmander, Bulbasaur, Squirtle, MissingNo
from queue_adt import CircularQueue
from referential_array import ArrayR
from stack_adt import ArrayStack

"""
This file has a PokeTeam class that contains the methods to set the team trainer, sets by which method the Pokemons
will battle i.e set, rotating or optimized which sorts team by selected criterion.

The class also has a method choose_team which allows user to select battle mode and takes input from the user for number
of pokemon in their team. This method also calls another method assign_team which populates the ADT based on the 
battle mode chosen. There is also __str__ method to print out the team.
"""


class PokeTeam():
    TEAM_LIMIT = 6
    ACCEPTED_BATTLE_MODE = [0, 1, 2]
    ACCEPTED_CRITERION = ["hp", "lvl", "def", "spd", "atk"]

    def __init__(self, trainer: str):
        """
        constructor for PokeTeam object
        best case = worst case = O(1)
        """
        self.set_trainer(trainer)
        self.set_battle_mode(0)

    def set_trainer(self, trainer: str):
        """
        method to assign value to caller PokeTeam
        best case = worst case = O(1)
        """
        if not (isinstance(trainer, str)):
            raise TypeError("Trainer name must be a string datatype")
        self.trainer = trainer

    def set_battle_mode(self, battle_mode: int):
        """
        method to assign battle mode to caller PokeTeam
        best case = worst case = O(1)
        """
        if not (isinstance(battle_mode, int)):
            raise TypeError("Battle mode must be an integer datatype")
        if battle_mode not in self.ACCEPTED_BATTLE_MODE:
            raise ValueError("Battle mode can only be 0, 1 or 2")
        self.battle_mode = battle_mode

    def set_criterion(self, criterion: str):
        """
        method that assigns criterion for caller PokeTeam
        best case = worst case = O(1)
        """
        if not (isinstance(criterion, str)):
            raise TypeError("Criterion must be a string")
        if criterion not in self.ACCEPTED_CRITERION:
            raise ValueError("Criterion must be one of hp, int, atk, def or spd")
        self.criterion = criterion

    def get_battle_mode(self) -> int:
        """
        method that returns battle mode of caller PokeTeam
        best case = worst case = O(1)
        """
        return self.battle_mode

    def get_criterion(self) -> str:
        """
        method that returns criterion of caller PokeTeam
        best case = worst case = O(1)
        """
        return self.criterion

    def get_trainer(self) -> str:
        """
        method that returns trainer of caller PokeTeam
        best case = worst case = O(1)
        """
        return self.trainer

    def choose_team(self, battle_mode: int, criterion: str = None):
        """
        method to ask input from user to populate team and assign value for battle mode and criterion if there is one
        best case = worst case = O(n)
        """
        self.set_battle_mode(battle_mode)
        if criterion is not None:
            self.set_criterion(criterion)

        valid = False
        output = ""
        while not valid:
            print(
                "Howdy Trainer! Choose your team as C B S" + "\n" + "where C is the number of Charmanders" + "\n" + "      B is the "
                + "number of Bulbasaurs\n      C is the number of Squirtles")
            output = input()
            if (len(output) == 5):
                if (output[1] == " " and output[3] == " " and int(output[0]) + int(output[2]) + int(
                        output[4]) <= self.TEAM_LIMIT):
                    valid = True

            elif (len(output) == 7):
                if (output[1] == " " and output[3] == " " and output[5] == " " and int(output[0]) + int(
                        output[2]) + int(output[4]) + int(output[6]) <= self.TEAM_LIMIT and int(output[6]) <= 1):
                    valid = True

        if (len(output) == 5):
            self.assign_team(int(output[0]), int(output[2]), int(output[4]))

        elif (len(output) == 7):
            self.assign_team(int(output[0]), int(output[2]), int(output[4]), int(output[6]))

    def assign_team(self, charm: int, bulb: int, squir: int, missingNo: int = 0):
        """
        method to populate the team based on the ADT that is chosen for the battle_mode entered by the user.
        best case = worst case = O(n), where n is the sum of charm, bulb, squir
        """

        if self.battle_mode == 0:
            self.team = ArrayStack(6)
            for _ in range(missingNo):
                self.team.push(MissingNo())
            for _ in range(squir):
                self.team.push(Squirtle())
            for _ in range(bulb):
                self.team.push(Bulbasaur())
            for _ in range(charm):
                self.team.push(Charmander())


        elif self.battle_mode == 1:
            self.team = CircularQueue(6)
            for _ in range(charm):
                self.team.append(Charmander())
            for _ in range(bulb):
                self.team.append(Bulbasaur())
            for _ in range(squir):
                self.team.append(Squirtle())
            for _ in range(missingNo):
                self.team.append(MissingNo())


        elif self.battle_mode == 2:
            temp = ArrayR(6)
            self.team = CircularQueue(6)

            for i in range(charm):
                temp[i] = Charmander()
            for j in range(charm, charm + bulb):
                temp[j] = Bulbasaur()
            for k in range(charm + bulb, charm + bulb + squir):
                temp[k] = Squirtle()
            for l in range(charm + bulb + squir, charm + bulb + squir + missingNo):
                temp[l] = MissingNo()

            temp.bubble_sort(self.get_criterion())

            for i in range(len(temp)):
                if temp[i] == None:
                    break
                self.team.append(temp[i])

    def __str__(self) -> str:
        """
        method that returns a String that contains the name, HP and level of the all pokemon from the caller PokeTeam
        best case = worst case = O(n), where n is the number of pokemons in PokeTeam
        """

        if self.get_battle_mode() == 0:
            out = ""
            temp = [None] * len(self.team)
            for i in range(len(self.team)):
                temp[i] = self.team.pop()
                if i == 0:
                    out += str(temp[i])
                else:
                    out += ", " + str(temp[i])

            for i in range(len(temp) - 1, -1, -1):
                self.team.push(temp[i])

        elif self.get_battle_mode() == 1 or self.get_battle_mode() == 2:
            out = ""
            temp = [None] * len(self.team)
            for i in range(len(self.team)):
                temp[i] = self.team.serve()
                if i == 0:
                    out += str(temp[i])
                else:
                    out += ", " + str(temp[i])

            for i in range(len(temp)):
                self.team.append(temp[i])

        return out
