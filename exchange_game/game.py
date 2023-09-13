from __future__ import annotations
# ^ In case you aren't on Python 3.10
from random_gen import RandomGen
from array_list import ArrayList
from hash_table import LinearProbePotionTable
from potion import Potion
from avl import AVLTree


class Game:

    def __init__(self, seed=0) -> None:
        """
        Approach Taken :
        The __init__ method creates the Game Object with parameter seed which is set to default to 0. We set all
        the objects we will be needing to None initially here

        Worst Case Time Complexity :
        O(1) since equals is constant time operation
        """
        self.rand = RandomGen(seed=seed)
        self.hash_table = None
        self.original_pairs = None
        self.avl_tree = None
        self.inv_len = None

    def set_total_potion_data(self, potion_data: list) -> None:
        """
        Approach Taken :
        First, we create a ArrayList object to temporarily store potion objects before inserting into the hash table.
        Next, make the hash table where potion data will be stored initialized by length of potion data. Then we iterate
        through a loop in range of length of potion data. We will temporarily store the new potion object created from
        data given in potion data in the ArrayList. We will then insert the Potion objects into the hash table with the
        key as name of the object and the data as the Potion object itself.

        ADTS Used :
            First for temporary storage we use of data we use ArrayList since it is the most similar to list and can be
        easily accessed. We store our potion object created using potion empty in arraylist before inserting in hash table.
            Next we use LinearProbePotionTable which is the hash table for storing our Potion objects by hashing them by
        their names first. We use it since it's the most suitable for storing data and quick access using the key. We

        Worst Case Time Complexity :
        O(n) where n is the length of potion data
        """

        n = len(potion_data)
        arr = ArrayList(n)
        self.hash_table = LinearProbePotionTable(n)
        for i in range(n):  # O(n)
            arr[i] = Potion.create_empty(potion_data[i][0], potion_data[i][1], potion_data[i][2])
            self.hash_table.insert(arr[i].name, arr[i])

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        """
        Approach Taken :
        Firstly, we save the given potion name and amount pairs as a class variable since we will need to reinsert it
        later after deletion since we must not change the given data in any way. We also create the avl_tree as well as
        save the given data length for use later. Next we iterate through every pair in given list and first we check
        if the given pair name exists in our total potion data hash table and if it does, we get the Potion object from
        the hash table and use potion setter method to set the quantity of said object. Next, we again get the Potion
        object and then get the price and store it in a variable buy price after which we insert it into the avl tree
        with key as the buy price and the store data potion object too.

        ADTS Used :
        We use AVL Tree to hash using the buy price and store data which is the potion object. We choose to use this
        ADT because it has O (log n) complexity and also it is a self-balancing tree and it is sorted by the buy price
        so we can this later for the choose_potion_for_vendor and solve_game tasks.

        Worst Case Time Complexity :
        = O(C) * O(log n)
        = O(C log n)
        C is the number of length of potion_name_amount_pairs and N is number of number of potions
        provided in set_total_potion_data

        Note : All hash_table methods are assumed to be taking constant time complexity
        """

        self.original_pairs = potion_name_amount_pairs
        self.avl_tree = AVLTree()
        self.inv_len = len(potion_name_amount_pairs)
        for pair in potion_name_amount_pairs:  # O(C) where C is length of potion_name_amount_pairs
            if self.hash_table.__contains__(pair[0]):
                self.hash_table.__getitem__(pair[0]).set_quantity(pair[1])
                buy_price = self.hash_table.__getitem__(pair[0]).get_buy_price()
                self.avl_tree[buy_price] = self.hash_table.__getitem__(pair[0])  # O(log n)

    def choose_potions_for_vendors(self, num_vendors: int) -> list:
        """
        Approach Taken:
        First we initialize a variable random_num which is a RandomGen Object and also a selling potion list. Then we
        use a while loop to run for every vendor. Next we generate a random number in range of potion_name_amount_pairs
        length. Next from the random number generated for each vendor the vendor buys the number-th most expensive item.
        Example : If vendor one picks a random number from 1 to 7 and gets 5, he gets the 5th most expensive item in the
        inventory. This is done using kth largest which was in avl.py.

        Next we also get the name of c-th expensive item and get the object from the hash table. We then append it into
        the list of vendor selling where items sold by vendors are shown. After this is done we delete the key and item
        from the avl tree so that no other vendor will chose it again. We then decrease the inventory length by one so
        that c-th item isn't out of range. Once loop has finished iterations we add back all potions into inventory
        since we have been asked not to delete any.

        ADTS Used :
        We just use the previously defined AVL Tree which is storing the value of buy price. We reason we use AVL Tree
        is we already coded the k-th largest method and this task required us to implement c-th most expensive potion to
        buy we can easily use k-th largest function for that.

        Worst Case Time Complexity:
        = (O(C) * (O(log n) + O(log n))) + O(D log m)
        = (O(C) * O(log n)) + O(D log m)
        = O(C log n) + O(D log m)
        = O(C log n), since both functions are the same and only having different numbers they are bound by same
          tightest bound. e.g. f(n) is O(g(n)) if f(n) ≤ c * g(n) and n0 ≤ n for some constants c and n0

        C represents number of vendors
        N represents the number of potions provided in set_total_potion_data
        D is the number of length of potion_name_amount_pairs
        M is number of number of potions provided in set_total_potion_data

        Note : All hash_table methods are assumed to be taking constant time complexity

        """
        random_num = RandomGen()
        vendor_selling = []

        i = 0
        while i < num_vendors:  # O(C) where c is num vendors
            c_val = random_num.randint(self.inv_len)
            cth_expensive = self.avl_tree.kth_largest(c_val)  # O(log n)
            cth_expensive_potion_name = cth_expensive.item.get_name()  # O(1)
            selling_item = self.hash_table.__getitem__(cth_expensive_potion_name)  # O(1)
            vendor_selling.append((str(selling_item.get_name()), int(selling_item.get_quantity())))  # O(1)
            self.avl_tree.__delitem__(cth_expensive.key)  # O(log n)
            self.inv_len -= 1  # O(1)
            i += 1  # O(1)

        self.add_potions_to_inventory(self.original_pairs)  # O(D log m)
        return vendor_selling

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:
        """
        Approach Taken :
        First we reuse the self.avl_tree which has the buy_price as the key. We iterate through potion valuations and
        get the potion object and calculate profit by getting sell price from potion valuations parameter and also
        use get buy price method called by potion object to do sell - buy getting profit, we also add buy_price add
        to sort by buy price if we have similar profits. We will then use merge sort to sort the data by profit

        Worst Case Time Complexity :
        Could Not Complete

        ADTS Used :
        We use the self.avl tree from before because it contains buy_price as the key hence we can use it for getting
        lowest buy price item which will be the one we would want to sell to the adventurer if we have an item having
        the same profit.
        """
        buy_price = self.avl_tree
        profit_table = []
        for i in potion_valuations:  # range 4 for all self.vendor_selling items
            potion = self.hash_table.__getitem__(i[0])  # this is potion object
            buy_price = potion.get_buy_price()
            profit = float(i[1]) - potion.get_buy_price()
            profit_table.append([potion, profit, buy_price])
        self.mergeSort_profit(profit_table)
        self.mergeSort_buy_price(profit_table)

    def mergeSort_profit(self, myList) -> None:
        """
        Taken reference from online code and changed to use for own code for profit code.
        """
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            # Recursive call on each half
            self.mergeSort_profit(left)
            self.mergeSort_profit(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0

            # Iterator for the main list
            k = 0

            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    # The value from the left half has been used
                    myList[k] = left[i]
                    # Move the iterator forward
                    i += 1
                else:
                    myList[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1

    def mergeSort_buy_price(self, myList) -> None:
        """
        Taken reference from online code and changed to use for own code for buy price sort.
        """
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            # Recursive call on each half
            self.mergeSort_buy_price(left)
            self.mergeSort_buy_price(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0

            # Iterator for the main list
            k = 0

            while i < len(left) and j < len(right):
                if left[i][1] == right[j][1]:
                    if left[i][2] <= right[j][2]:
                        # The value from the left half has been used
                        myList[k] = left[i]
                        # Move the iterator forward
                        i += 1
                else:
                    myList[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1
