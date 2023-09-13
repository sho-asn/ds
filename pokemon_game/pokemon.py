from pokemon_base import PokemonBase
from random import random
from abc import ABC

"""
Contains 5 Inherited Classes

This class has 3 inherited Pokemon class from the PokemonBase class for defining different types of pokemon
which has different implementation of the abstract methods defined in Base Class. 
E.g level_up for Charmander and Squirtle increases base stats differently. 

There is another inherited class that is GlitchMon is another inherited PokemonBase class which defines an irregular
pokemon with different stats and way of handling said stats. There is another Class missingNo which is child class of
GlitchMon which creates a GlitchMon object and acts as a constructor.
"""


class Charmander(PokemonBase):
    name = "Charmander"

    def __init__(self) -> None:
        """
        constructor for Charmander object
        best case = worst case = O(1)
        """
        PokemonBase.__init__(self, 7, "Fire")
        self.set_attack(7)
        self.set_defence(4)
        self.set_speed(8)

    def level_up(self) -> None:
        """
        method called by a Charmander object when it levels up, it increases level by 1, and adjust its attack and speed according to its level
        best case = worst case = O(1)
        """
        self.set_level(self.get_level() + 1)
        self.set_attack(6 + self.get_level())
        self.set_speed(7 + self.get_level())

    def damage_taken(self, Pokemon: 'PokemonBase') -> int:
        """
        method that calculates and returns the damage the caller Charmander object would receive by a Pokemon.
        Damage rating is the attack stat of Pokemon, doubled if Pokemon is Water type, halved if Pokemon is Grass type,
        Damage rating is divided by 2 if the damage rating is lower than or equals to the defence of caller Charmander.
        best case = worst case = O(1)
        """
        if not (isinstance(Pokemon, PokemonBase)):
            raise TypeError("Pokemon must be a pokemon")
        damage = Pokemon.get_attack()
        if Pokemon.get_poke_type() == "Grass":
            damage //= 2
        elif Pokemon.get_poke_type() == "Water":
            damage *= 2
        if damage <= self.get_defence():
            damage //= 2
        return damage


class Bulbasaur(PokemonBase):
    name = "Bulbasaur"

    def __init__(self) -> None:
        """
        Constructor for Bulbasaur object
        best case = worst case = O(1)
        """
        PokemonBase.__init__(self, 9, "Grass")
        self.set_attack(5)
        self.set_defence(5)
        self.set_speed(7)

    def level_up(self) -> None:
        """
        method called by a Bulbasaur object when it levels up, it increases level by 1, and adjust its speed according to its level
        best case = worst case = O(1)
        """
        self.set_level(self.get_level() + 1)
        self.set_speed(7 + self.get_level() // 2)

    def damage_taken(self, Pokemon: 'PokemonBase') -> int:
        """
        method that calculates and returns the damage the caller Bulbasaur object would receive by a Pokemon.
        Damage rating is the attack stat of Pokemon, doubled if Pokemon is Fire type, halved if Pokemon is Water type,
        Damage rating is divided by 2 if the damage rating is lower than or equals to the defence of caller Bulbasaur + 5.
        best case = worst case = O(1)
        """
        if not (isinstance(Pokemon, PokemonBase)):
            raise TypeError("Pokemon must be a pokemon")
        damage = Pokemon.get_attack()
        if Pokemon.get_poke_type() == "Water":
            damage //= 2
        elif Pokemon.get_poke_type() == "Fire":
            damage *= 2
        if damage <= self.get_defence() + 5:
            damage //= 2

        return damage


class Squirtle(PokemonBase):
    name = "Squirtle"

    def __init__(self) -> None:
        """
        constructor for Squirtle object
        best case = worst case = O(1)
        """
        PokemonBase.__init__(self, 8, "Water")
        self.set_attack(4)
        self.set_defence(7)
        self.set_speed(7)

    def level_up(self) -> None:
        """
        method called by a Squirtle object when it levels up, it increases level by 1, and adjust its attack and defence according to its level
        best case = worst case = O(1)
        """
        self.set_level(self.get_level() + 1)
        self.set_attack(4 + self.get_level() // 2)
        self.set_defence(6 + self.get_level())

    def damage_taken(self, Pokemon: 'PokemonBase') -> int:
        """
        method that calculates and returns the damage the caller Squirtle object would receive by a Pokemon.
        Damage rating is the attack stat of Pokemon, doubled if Pokemon is Grass type, halved if Pokemon is Fire type,
        Damage rating is divided by 2 if the damage rating is lower than or equals to the defence of caller Bulbasaur * 2.
        best case = worst case = O(1)
        """
        if not (isinstance(Pokemon, PokemonBase)):
            raise TypeError("Pokemon must be a pokemon")
        damage = Pokemon.get_attack()
        if Pokemon.get_poke_type() == "Fire":
            damage //= 2
        elif Pokemon.get_poke_type() == "Grass":
            damage *= 2
        if damage <= self.get_defence() * 2:
            damage //= 2

        return damage


class GlitchMon(PokemonBase, ABC):

    def increase_HP(self, HP: int = 1) -> None:
        """
        method to increase HP of caller MissingNo object, default value is 1
        best case = worst case = O(1)
        """
        if not (isinstance(HP, int)):
            raise TypeError("HP must be an integer")
        if HP <= 0:
            raise ValueError("HP must be greater than 0")
        self.set_HP(self.get_HP() + HP)

    def superpower(self) -> None:
        """
        method that has a 25% chance to be called by MissingNo object when attacked, it has a 1/3 chance to level up, increase its HP or level up and increase its HP
        best case = worst case = O(1)
        """
        rng = int(random() * 3)
        if rng == 0:
            self.level_up()
        elif rng == 1:
            self.increase_HP()
        elif rng == 2:
            self.level_up()
            self.increase_HP()

    def damage_taken(self, Pokemon: 'PokemonBase') -> int:
        """
        method that calculates and returns the damage the caller MissingNo object would receive from a Pokemon.
        It has a 1 in 3 chance to follow the defensive properties of a Charmander, Bulbasaur or Squirtle.
        best case = worst case = O(1)
        """
        if not (isinstance(Pokemon, PokemonBase)):
            raise TypeError("Pokemon must be a pokemon")
        damage = Pokemon.get_attack()
        rng = int(random() * 3)
        if rng == 0:
            if damage <= self.get_defence():
                damage //= 2


        elif rng == 1:
            if damage <= self.get_defence() + 5:
                damage //= 2

        elif rng == 2:
            if damage <= self.get_defence() * 2:
                damage //= 2

        return damage

    def level_up(self) -> None:
        """
        method called by a MissingNo object when it levels up, it increases level by 1, and increases all stats of MissingNo by 1
        best case = worst case = O(1)
        """
        self.set_level(self.get_level() + 1)
        self.increase_HP()
        self.set_attack(self.get_attack() + 1)
        self.set_speed(self.get_speed() + 1)
        self.set_defence(self.get_defence() + 1)

    def attacked_by(self, Pokemon: 'PokemonBase') -> None:
        """
        method that is called by MissingNo object when MissingNo object is attacked by a Pokemon.
        It has a 1 in 4 chance to call superpower, enhancing its abilities and ignore the attack of Pokemon.
        It has a 3 in 4 chance to take damage from Pokemon
        best case = worst case = O(1)
        """
        if not (isinstance(Pokemon, PokemonBase)):
            raise TypeError("Pokemon must be a pokemon")
        rng = int(random() * 4)
        if rng == 0:
            self.superpower()
        else:
            self.reduce_HP(self.damage_taken(Pokemon))


class MissingNo(GlitchMon):
    name = "MissingNo"

    def __init__(self) -> None:
        """
        constructor for MissingNo object
        best case = worst case = O(1)
        """
        PokemonBase.__init__(self, 8)
        self.set_attack(5)
        self.set_defence(5)
        self.set_speed(7)
