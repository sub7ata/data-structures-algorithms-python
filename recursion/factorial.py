import unittest


def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def recursive_factorial(number):
    if number <= 1:
        return 1
    return number * recursive_factorial(number - 1)


if __name__ == '__main__':
    element = int(input("Enter the number for the factorial: "))
    print(f"Factorial number using iterative:\t{recursive_factorial(element)}")
    print(f"Factorial number using recursive:\t{recursive_factorial(element)}")


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(iterative_factorial(6), 720)
        self.assertEqual(iterative_factorial(1), 1)
        self.assertEqual(iterative_factorial(5), 120)

        self.assertEqual(recursive_factorial(6), 720)
        self.assertEqual(recursive_factorial(1), 1)
        self.assertEqual(recursive_factorial(5), 120)

        print('All test cases passed.')

if __name__ == '__main__':
    unittest.main()