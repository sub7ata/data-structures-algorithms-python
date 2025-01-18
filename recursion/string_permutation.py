import unittest


def permute(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):

            for perm in permute(s[:i] + s[i+1:]):
                out += [let + perm]
    return out


if __name__ == "__main__":
    print(f"After permutations: {permute("abc")}")


class TestPerm(unittest.TestCase):
    def test_permutations(self):
        self.assertEqual(sorted(permute('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        self.assertEqual(sorted(permute('dog')), sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))
        print('All test cases passed.')

if __name__ == '__main__':
    unittest.main()
