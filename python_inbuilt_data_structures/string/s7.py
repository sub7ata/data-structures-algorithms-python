"""WAP to sort characters of the string, first alphabet symbols followed by digits?"""
"""Input: B4A1D3C2 Output: ABCD1234"""

class StringSorter:
    @staticmethod
    def sort_string(s):
        letters = []
        digits = []
        for idx, itm in enumerate(s):
            if itm.isalpha():
                letters.append(itm)
            elif itm.isdigit():
                digits.append(itm)
        return ''.join(sorted(letters)) + ''.join(sorted(digits))

    @staticmethod
    def sort_string1(s):
        letters = ''
        digits = ''
        for idx, itm in enumerate(s):
            if itm.isalpha():
                letters += itm
            elif itm.isdigit():
                digits += itm
        return ''.join(sorted(letters)) + ''.join(sorted(digits))

if __name__ == '__main__':
    input = input("Enter the string: ")
    output1 = StringSorter.sort_string(input)
    print(f"Result1: {output1}")
    output2 = StringSorter.sort_string1(input)
    print(f"Result2: {output2}")