"""WAP for the following requirement? """
"""Input:a3z3b4 Output:aaabbbbzz (sorted String)"""

class Test:
    @staticmethod
    def fun(s):
        ch = ''
        chs = []
        for idx, itm in enumerate(s):
            if itm.isalpha():
                ch = itm
            else:
                chs.append(ch*int(itm))
        chs.sort()
        return ''.join(chs)


if __name__ == '__main__':
    input_data = input("Enter data: ")
    print(f"Result: {Test.fun(input_data)}")