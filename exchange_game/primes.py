def largest_prime(k: int) -> int:
    """
    Approach Taken :
    Firstly, we find the floored square root of k to later cancel out the prime multiples. Next, we create a list where
    all values are true initially where true means they are prime. Then, we iterate through range 2 (first prime number)
    to sqrt_val + 1 (exclusive). Next, if number is prime it goes through another for loop which iterates from i squared
    upto k with a step of i (where i is the current number) What this essentially does is  starting from i**2 it makes
    all multiples of i upto x false i.e. not prime. The inner loop terminates as number goes over k and the outer loop
    terminates when we reach sqrt val. We only take upto sqrt because after that point at least one of the factors
    must be smaller than square root of k.

    Next, we iterate through our list in reverse order and return the first number which is true i.e. prime because
    according to our method all multiples of non prime numbers have been set to False i.e. not prime.

    Worst-case Time Complexity :
    = (O(n) * O(log n)) + O(n)
    = O(n log n) + O(n)
    = O(n log n) since it is more dominating

    Where n is the range of numbers given in the parameters
    """

    if k <= 2 or k > 100000:
        raise ValueError("k must be larger than 2 and at most 100000")

    sqrt_val = int(k ** 0.5)
    lst = [True for i in range(k)]
    for i in range(2, sqrt_val + 1):  # O(n)
        if lst[i] is True:
            for j in range(i * i, k, i):  # O(log n)
                lst[j] = False

    for i in range(k - 1, 1, -1):  # O(n)
        if lst[i] is True:
            return i
