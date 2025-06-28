"""WAP to print the characters present at even and odd indexes separately for the given string."""
"""
Enter string: python
Result:
Characters in even indexs: pto
Characters in odd indexs: yhn
Result:
Characters in even indexs: pto
Characters in odd indexs: yhn
"""

class StringSeparater:
    @staticmethod
    def even_odd_separater(strng):
        even_str = ''
        odd_str = ''
        for idx, itm in enumerate(strng):
            if idx%2 == 0:
                even_str += itm
            else:
                odd_str += itm
        return f"Characters in even indexs: {even_str}\nCharacters in odd indexs: {odd_str}"

    @staticmethod
    def even_odd_separater1(strng):
        return f"Characters in even indexs: {strng[::2]}\nCharacters in odd indexs: {strng[1::2]}"

if __name__ == '__main__':
    input_data = input("Enter string: ")
    print(f"Result1:\n{StringSeparater.even_odd_separater(input_data)}")
    print(f"Result2:\n{StringSeparater.even_odd_separater1(input_data)}")