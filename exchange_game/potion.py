class Potion:
    
    def __init__(self, potion_type: str, name: str, buy_price: float, quantity: float) -> None:
        """
        Approach Taken :
        __init__ method to initialize the Potion Object along with data potion_type, name, buy_price and quantity

        Worst Case Time Complexity :
        O(1) since equals is constant time complexity
        """

        self.potion_type = potion_type
        self.name = name
        self.buy_price = buy_price
        self.quantity = quantity

    @classmethod
    def create_empty(cls, potion_type: str, name: str, buy_price: float) -> 'Potion':
        """
        Approach Taken :
        Initialize a Potion object with quantity automatically set to 0

        Worst Case Time Complexity :
        O(1) since return Potion __init__ is also O(1) and return is also O(1) so it remains constant time.
        """
        return Potion(potion_type, name, buy_price, 0)

    @classmethod
    def good_hash(cls, potion_name: str, tablesize: int) -> int:
        """
        Approach Taken :
        For good hash we use pseudo random numbers and iterate through every character in potion name.
        Every iteration the values and pseudo random numbers keep changing to avoid any collisions. By keeping numbers
        random and iterating through every letter we are keeping collision low and making good hash function.

        Worst Case Time Complexity :
        O(n), where n is the number of characters in potion name
        """

        value = 0
        a = 31415
        b = 27183
        for char in potion_name:  # O(n)
            value = (ord(char) + a * value) % tablesize
            a = a * b % (tablesize - 1)
        return value

    @classmethod
    def bad_hash(cls, potion_name: str, tablesize: int) -> int:
        """
        Approach Taken : We just directly hash the name according to first letter ascii value without using any
        coefficients to multiply ord(char) to get randomness. This is done so that there are many collisions and
        this proves to be a bad hash function.

        Worst Case Time Complexity :
        O(1) since only return is constant time complexity
        """
        return ord(potion_name[0]) % tablesize

    def set_quantity(self, quantity) -> None:
        """
        Approach Taken :
        Method to set quantity when we use Potion.create_empty where the quantity is initially set to 0 to allow change
        later on.

        Worst Case Time Complexity :
        O(1) since equals is constant time complexity
        """

        self.quantity = quantity

    def get_potion_type(self) -> str:
        """
        Approach Taken:
        Method to return the potion type

        Worst Case Time Complexity :
        O(1) since only return is constant time complexity
        """

        return self.potion_type

    def get_name(self) -> str:
        """
        Approach Taken :
        Method to return the potion name

        Worst Case Time Complexity :
        O(1) since only return is constant time complexity
        """

        return self.name

    def get_buy_price(self) -> float:
        """
        Approach Taken :
        Method to return the potion buying price

        Worst Case Time Complexity :
        O(1) since only return is constant time complexity
        """

        return self.buy_price

    def get_quantity(self) -> float:
        """
        Approach Taken :
        Method to return the potion quantity

        Worst Case Time Complexity :
        O(1) since only return is constant time complexity
        """

        return self.quantity
