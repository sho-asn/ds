from abc import ABC, abstractmethod

"""
Abstract Class PokemonBase

This class defines an abstract pokemon base which has a constructor and general methods common across
all Pokemon's. The methods are related to the stats of the Pokemon such as HP, Attack, Defence, Speed, etc.
"""


class PokemonBase(ABC):

    def __init__(self, HP: int, poke_type: str = None) -> None:
        """
        constructor for abstract class PokemonBase
        best case = worst case = O(1)
        """
        self.set_HP(HP)
        self.set_poke_type(poke_type)
        self.set_level(1)

    def get_HP(self) -> int:
        """
        method that returns HP of the caller pokemon
        best case = worst case = O(1)
        """
        return self.HP

    def set_HP(self, HP: int) -> None:
        """
        method to assign HP for the caller pokemon
        best case = worst case = O(1)
        """
        if not (isinstance(HP, int)):
            raise TypeError("HP must be an integer")
        self.HP = HP

    def reduce_HP(self, taken_damage: int) -> None:
        """
        method to reduce HP of the caller pokemon
        best case = worst case = O(1)
        """
        if not (isinstance(taken_damage, int)):
            raise TypeError("damage taken must be an integer")
        if taken_damage < 0:
            raise ValueError("damage taken cannot be less than 0")
        self.set_HP(self.get_HP() - taken_damage)

    def get_level(self) -> int:
        """
        method that returns level of the caller pokemon
        best case = worst case = O(1)
        """
        return self.level

    def set_level(self, level: int) -> None:
        """
        method to assign level for the caller pokemon
        best case = worst case = O(1)
        """
        if not (isinstance(level, int)):
            raise TypeError("level must be an integer")
        if level <= 0:
            raise ValueError("value cannot be less than 0")
        self.level = level

    def set_poke_type(self, poke_type: str = None) -> None:
        """
        method to assign type for the caller pokemon
        best case = worst case = O(1)
        """
        if not (isinstance(poke_type, str)) and poke_type != None:
            raise TypeError("Type of pokemon must be a string or have no type")
        if poke_type != "Fire" and poke_type != "Grass" and poke_type != "Water" and poke_type != None:
            raise ValueError("Pokemon type must be Fire, Grass, Water or have no type only")
        self.poke_type = poke_type

    def get_poke_type(self) -> str:
        """
        method that returns type of the caller pokemon
        best case = worst case = O(1)
        """
        return self.poke_type

    def get_name(self) -> str:
        """
        method that returns name of the caller pokemon
        best case = worst case = O(1)
        """
        return self.name

    def get_speed(self) -> int:
        """
        method that returns speed of the caller pokemon
        best case = worst case = O(1)
        """
        return self.speed

    def set_speed(self, speed: int) -> None:
        """
        method to assign speed for the caller pokemon
        best case = worst case = O(1)
        """
        if not (isinstance(speed, int)):
            raise TypeError("speed must be an integer")
        if speed <= 0:
            raise ValueError("speed must be greater than 0")
        self.speed = speed

    def get_defence(self) -> int:
        """
        method that returns defence of the caller pokemon
        best case = worst case = O(1)
        """
        return self.defence

    def set_defence(self, defence: int) -> None:
        """
        method to assign defence for the caller pokemon
        best case = worst case = O(1)
        """
        if not (isinstance(defence, int)):
            raise TypeError("defence must be an integer")
        if defence <= 0:
            raise ValueError("defence must be greater than 0")
        self.defence = defence

    def get_attack(self) -> int:
        """
        method that returns attack for the caller pokemon
        best case = worst case = O(1)
        """
        return self.attack

    def set_attack(self, attack: int) -> None:
        """
        method to assign attack for the caller pokemon
        best case = worst case = O(1)
        """
        if not (isinstance(attack, int)):
            raise TypeError("attack must be an integer")
        if attack <= 0:
            raise ValueError("attack must be greater than 0")
        self.attack = attack

    def alive(self) -> bool:
        """
        method that returns True if the caller pokemon is alive, False otherwise
        """
        return self.get_HP() > 0

    def faint(self) -> bool:
        """
        method that returns False if the caller pokemon is alive, True otherwise
        """
        return self.get_HP() <= 0

    def __str__(self) -> str:
        """
        method that returns a String that contains the name, HP and level of the caller pokemon
        best case = worst case = O(1)
        """
        return (self.name + "'s HP = " + str(self.HP) + " and level = " + str(self.level))

    def faster_than(self, Pokemon: 'PokemonBase') -> bool:
        """
        method that returns True if the caller pokemon is faster(has greater speed) than Pokemon, False otherwise
        best case = worst case = O(1)
        """
        if not (isinstance(Pokemon, PokemonBase)):
            raise TypeError("Pokemon must be a pokemon")
        return (self.get_speed() > Pokemon.get_speed())

    def attacked_by(self, Pokemon: 'PokemonBase') -> None:
        """
        method that is called when a Pokemon object is attacked by Pokemon to reduce its HP
        best case = worst case = O(1)
        """
        if not (isinstance(Pokemon, PokemonBase)):
            raise TypeError("Pokemon must be a pokemon")
        self.reduce_HP(self.damage_taken(Pokemon))

    @abstractmethod
    def level_up(self) -> None:
        """
        abstract method called by pokemon when it levels up
        """
        pass

    @abstractmethod
    def damage_taken(self, Pokemon: 'PokemonBase') -> int:
        """
        method that calculates and returns the damage the caller pokemon would receive by Pokemon
        """
        pass
