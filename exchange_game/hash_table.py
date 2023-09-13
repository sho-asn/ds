""" Hash Table ADT

Defines a Hash Table using Linear Probing for conflict resolution.
It currently rehashes the primary cluster to handle deletion.
"""
__author__ = 'Brendon Taylor, modified by Jackson Goerner'
__docformat__ = 'reStructuredText'
__modified__ = '21/05/2020'
__since__ = '14/05/2020'

from referential_array import ArrayR
from typing import TypeVar, Generic
from potion import Potion
from primes import largest_prime

T = TypeVar('T')


class LinearProbePotionTable(Generic[T]):
    """
    Linear Probe Potion Table

    This potion table does not support deletion.

    attributes:
        count: number of elements in the hash table
        table: used to represent our internal array
        table_size: current size of the hash table
    """

    def __init__(self, max_potions: int, good_hash: bool = True, tablesize_override: int = -1) -> None:
        """
        Approach Taken :
        LinearProbePotionTable Object Initializer with parameters; max potions number, good_ hash boolean value to
        determine whether we use good hash or not and tablesize_override to set table size either to max potion size
        or override value depending on the parameter given.

        Worst Case Time Complexity :
        O(1) since equals and if are both constant time operations
        """

        # Statistic setting
        self.conflict_count = 0
        self.probe_max = 0
        self.probe_total = 0
        self.count = 0
        if tablesize_override != -1:
            self.table = ArrayR(tablesize_override)
        else:
            self.table = ArrayR(max_potions * 3)
        self.good_hash = good_hash
        self.tablesize_override = tablesize_override

    def hash(self, potion_name: str) -> int:
        """
        Approach Taken :
        We need to implement a method which takes into consideration all cases possible for hashing. Firstly, we have
        the condition if good hash is true or false. Other condition is whether tablesize overridden or not. If good_hash
        is true we hash the name using good hash and tablesize will be largest prime number in range of length of
        self.table. Next if we have a overridden tablesize value we make that the tablesize instead. The next two cases
        follow the same implementation however we use bad hash instead of good hash, which happens when good_hash
        is set to False.

        Worst Case Time Complexity :
        O(m log m) in the worst case which is when we have self.good_hash == True and self.tablesize_override == -1.

        This is because, good_hash has a time complexity of O(n) where n is the number of characters in a name and
        largest_prime has a time complexity of O(m log m) where m is the range of numbers given in the parameters.
        Now, when we do O(n) + O(m log m), O(m log m) is more dominant hence it is the worst case time complexity

        """

        if self.good_hash == True and self.tablesize_override == -1:
            ret = Potion.good_hash(potion_name, largest_prime(len(self.table)))
        elif self.good_hash == True and self.tablesize_override != -1:
            ret = Potion.good_hash(potion_name, self.tablesize_override)
        elif self.good_hash == False and self.tablesize_override == -1:
            ret = Potion.bad_hash(potion_name, largest_prime(len(self.table)))
        else:  # self.good_hash = False and self.tablesize_override != -1:
            ret = Potion.bad_hash(potion_name, self.tablesize_override)
        return ret

    def statistics(self) -> tuple:
        """
        Approach Taken :
        Statistics is a method which simply returns the total number of conflict, total distance probed and length of
        longest probe done in a tuple form. Since probe total updates these values using self, we can just return it
        after probing is done.

        Worst Case Time Complexity :
        O(1) since return is constant time complexity
        """
        return self.conflict_count, self.probe_total, self.probe_max

    def __len__(self) -> int:
        """
        Returns number of elements in the hash table
        :complexity: O(1)
        """
        return self.count

    def __linear_probe(self, key: str, is_insert: bool) -> int:
        """
        Find the correct position for this key in the hash table using linear probing
        :complexity best: O(K) first position is empty
                          where K is the size of the key
        :complexity worst: O(K + N) when we've searched the entire table
                           where N is the table_size
        :raises KeyError: When a position can't be found

        Approach Taken :
        This method find the correct position for the key in the hash based on the returned value from hash() method.
        If the slot is empty and is_insert is True, it returns the position. Otherwise, it returns position if the
        table[position][0] equals to the key. If it's not applied for both cases, the position goes to next index
        position. In addition, it compares to pre_position (the returned value from hash()) and final_position, and
        conflict_count, probe_max and probe_total are updated.

        Worst Case Time Complexity :
        O(n) where n is the number that represents the length of self.table
        Worst case happens when we insert at for example 4th position and its next free location is 3rd position where
        the function runs through the full table size. The other if, =, + are constant time operations
        """

        pre_position = self.hash(key)
        position = self.hash(key)  # get the position using hash

        if is_insert and self.is_full():
            raise KeyError(key)

        for _ in range(len(self.table)):  # start traversing    # O(n)
            if self.table[position] is None:  # found empty slot
                if is_insert:
                    final_position = position
                    if pre_position == final_position:
                        probe = 0
                    elif pre_position < final_position:
                        probe = (final_position - pre_position)
                    else:
                        probe = (len(self.table) - pre_position + final_position + 1)
                    self.probe_total += probe
                    if pre_position != final_position:
                        conflict = 1
                    else:
                        conflict = 0
                    self.conflict_count += conflict
                    if probe > self.probe_max:
                        self.probe_max = probe
                    return final_position
                else:
                    raise KeyError(key)  # so the key is not in
            elif self.table[position][0] == key:  # found key
                return position
            else:  # there is something but not the key, try next
                position = (position + 1) % len(self.table)

        raise KeyError(key)

    def __contains__(self, key: str) -> bool:
        """
        Checks to see if the given key is in the Hash Table
        :see: #self.__getitem__(self, key: str)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> T:
        """
        Get the item at a certain key
        :see: #self.__linear_probe(key: str, is_insert: bool)
        :raises KeyError: when the item doesn't exist
        """
        position = self.__linear_probe(key, False)
        return self.table[position][1]

    def __setitem__(self, key: str, data: T) -> None:
        """
        Set an (key, data) pair in our hash table
        :see: #self.__linear_probe(key: str, is_insert: bool)
        :see: #self.__contains__(key: str)
        """
        if len(self) == len(self.table) and key not in self:
            raise ValueError("Cannot insert into a full table.")
        position = self.__linear_probe(key, True)

        if self.table[position] is None:
            self.count += 1
        self.table[position] = (key, data)

    def initalise_with_tablesize(self, tablesize: int) -> None:
        """
        Initialise a new array, with table size given by tablesize.
        Complexity: O(n), where n is len(tablesize)
        """
        self.count = 0
        self.table = ArrayR(tablesize)

    def is_empty(self):
        """
        Returns whether the hash table is empty
        :complexity: O(1)
        """
        return self.count == 0

    def is_full(self):
        """
        Returns whether the hash table is full
        :complexity: O(1)
        """
        return self.count == len(self.table)

    def insert(self, key: str, data: T) -> None:
        """
        Utility method to call our setitem method
        :see: #__setitem__(self, key: str, data: T)
        """
        self[key] = data

    def __str__(self) -> str:
        """
        Returns all they key/value pairs in our hash table (no particular order)
        :complexity: O(N) where N is the table size
        """
        result = ""
        for item in self.table:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + "," + str(value) + ")\n"
        return result
