"""Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.
Did not solve it in time

 """
import time

def largestPalindrome(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 9
    start = time.time()
    range_of_dividers = list(reversed(range(10**(n-1), 10**(n))))
    # print(range_of_dividers)
    
    for base in range_of_dividers:
        string_number = str(base)
        number_to_test = int(string_number + string_number[::-1])
        for divider in range_of_dividers:
            if (number_to_test % divider == 0) and (number_to_test/divider <= range_of_dividers[0]):
                print(f"for n ={n}, time is {time.time() - start}")
                return number_to_test

for n in range(1, 9):
    print(largestPalindrome(n))


        
            