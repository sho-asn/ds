from typing import Generator


def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    """Complexity for lcg is O(n) since it keeps running until it is not break from"""

    while True:
        seed = (a * seed + c) % modulus
        yield seed


class RandomGen:

    def __init__(self, seed: int = 0) -> None:
        """
        Approach Taken :
        the __init__ method initializes the RandomGen object with the seed taken as a parameter

        Worst Case Time Complexity :
        O(1) since equals is constant time complexity
        """

        self.seed = seed
        self.generator = lcg(pow(2, 32), 134775813, 1, seed)

    def randint(self, k: int) -> int:
        """
        Approach Taken :
        We use the generator given and iterate through it directly and append the numbers to a list and break the loop
        once we have 5 numbers. Next we use another loop to go through the 5 numbers we generated and append them to a
        new list where we change them into binary using the in built binary function. Following since we only want the
        numbers, to remove "0b" we do list slicing of the string start from i = 2. Next we check if the length of
        binary number is greater than 16 we need to eliminate 16 least significant bits so we do list slicing from till
        range length of binary number - 16 to remove it. Following, we check that while length of sliced binary number
        isn't 16 we add a 0 to the left hand so value remains same but we have it in length = 16.

        Next, we iterate through a new loop 16 times (no of 0s and 1s) and we extract the ith bit from all 5 numbers
        and add it to a counter. If at least 3 of the bits are 1 then we add "1" to a new string else we add "0" We get
        a new binary string which is a result of previous counter method and we convert this binary number to denary
        using int method. Finally we mod the value we got by k and add 1 to it and return our random integer number

        Worst Case Time Complexity :
        = O(1) + (O(1) * O(1)) + O(1)
        = O(1) + O(1) + O(1)
        = O(1)
        """

        nums = []
        for x in self.generator:    # generator itself is O(n) however since we always take only 5 numbers as shown in
            nums.append(x)          # line 50 we can ignore O(n) and since it always does 5 steps we can round it to
            if len(nums) == 5:      # be O(1) operation which means constant time complexity
                break

        bin_nums = []
        for i in range(len(nums)):  # Due to constant 5 steps all the time so it's complexity is O(1)
            bin_nums.append(bin(nums[i]))
            bin_nums[i] = bin_nums[i][2:]
            if len(bin_nums[i]) > 16:
                bin_nums[i] = bin_nums[i][:len(bin_nums[i]) - 16]
            while len(bin_nums[i]) < 16:  # The steps taken will always be in the range of 16 and since the closet bound
                bin_nums[i] = "0" + bin_nums[i]  # of O(16) is O(1) so this is constant time complexity

        new_number = ""
        for i in range(16):  # Due to constant 16 steps all the time so it's complexity is O(1)
            one_counter = int(bin_nums[0][i]) + int(bin_nums[1][i]) + int(bin_nums[2][i]) + int(bin_nums[3][i]) + int(
                bin_nums[4][i])
            if one_counter >= 3:
                new_number += "1"
            else:
                new_number += "0"

        x = int(new_number, 2)
        ret = (x % k) + 1
        return ret


if __name__ == "__main__":
    Random_gen = lcg(pow(2, 32), 134775813, 1, 0)
