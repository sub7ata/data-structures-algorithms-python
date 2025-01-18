import unittest


def iterative_fibonacci(number):
    """ITERATIVE FIBONACCI"""
    first_number = 0
    second_number = 1
    if number < 0:
        return f"{number} is a invalid number for the fibonacci number."
    elif number == 0:
        return 0
    elif number == 1:
        return second_number
    else:
        for _ in range(1, number):
            third_number = first_number + second_number
            first_number = second_number
            second_number = third_number
        return third_number

def recursive_fibonacci(number):
    """RECURSIVE FIBONACCI"""
    if number < 0:
        return f"{number} is a invalid number for the fibonacci number."
    elif number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)

def dynamically_fibonacci(number):
    n = number
    cache = [None] * (n + 1)

    if n == 0 or n == 1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = dynamically_fibonacci(n-1) + dynamically_fibonacci(n-2)
    return cache[n]


if __name__ == "__main__":
    number = int(input("Enter the number for the fibonacci: "))
    print("Fibonacci number using iterative:\t", iterative_fibonacci(number))
    print("Fibonacci number using recursive:\t", recursive_fibonacci(number))
    print("Fibonacci number using dynamically:\t", dynamically_fibonacci(number))


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(iterative_fibonacci(10), 55)
        self.assertEqual(iterative_fibonacci(1), 1)
        self.assertEqual(iterative_fibonacci(23), 28657)

        self.assertEqual(recursive_fibonacci(10), 55)
        self.assertEqual(recursive_fibonacci(1), 1)
        self.assertEqual(recursive_fibonacci(23), 28657)
        
        self.assertEqual(dynamically_fibonacci(10), 55)
        self.assertEqual(dynamically_fibonacci(1), 1)
        self.assertEqual(dynamically_fibonacci(23), 28657)

        print('All test cases passed.')

if __name__ == '__main__':
    unittest.main()