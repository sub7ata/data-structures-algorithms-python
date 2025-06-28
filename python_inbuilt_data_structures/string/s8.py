"""WAP for the following requirement?"""
"""Input: a4b3c2 Output: aaaabbbcc"""

class Test:
    @staticmethod
    def fun(data):
        txt = ""
        s = ""
        for i in data:
            if i.isalpha():
                s = i
            elif i.isdigit():
                txt += int(i) * s
        return txt

if __name__ == '__main__':
    input_data = input("Enter data: ")
    print(f"Result: {Test.fun(input_data)}")