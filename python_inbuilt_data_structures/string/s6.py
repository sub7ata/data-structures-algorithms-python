"""WAP to merge the characters of two strings into a single string by taking characters alternately."""
"""
Enter First String: SBAA
Enter Second String: URT
Updated String: SUBRATA
"""

class StringMerger:
    @staticmethod
    def merge_strings(str1, str2):
        l1 = len(str1)
        l2 = len(str2)
        i = 0
        j = 0
        new_str = ""
        while i < l1 or j < l2:
            if i < l1:
                new_str += str1[i]
                i += 1
            if j < l2:
                new_str += str2[j]
                j += 1
        return new_str

    def merge_strings1(a, b):
        from itertools import zip_longest
        lst = list(map(lambda d: (d[0] or '') + (d[1] or ''), zip_longest(a,b)))
        return "".join(lst)

if __name__ == "__main__":
    str1 = input("Enter First String: ")
    str2 = input("Enter Second String: ")
    output1 = StringMerger.merge_strings(str1, str2)
    output2 = StringMerger.merge_strings(str1, str2)
    print(f"Result1: {output1}")
    print(f"Result2: {output2}")
