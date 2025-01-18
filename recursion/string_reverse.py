import unittest


def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

if __name__ == '__main__':
    print(f"After reverse: {reverse('hello world')}")


class TestReverse(unittest.TestCase):

    def test_rev(self):
        self.assertEqual(reverse('hello'), 'olleh')
        self.assertEqual(reverse('hello world'), 'dlrow olleh')
        self.assertEqual(reverse('123456789'), '987654321')

        print('PASSED ALL TEST CASES!')


if __name__ == '__main__':
    unittest.main()
