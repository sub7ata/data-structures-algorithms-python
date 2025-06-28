"""WAP for the following requirement?"""
"""Input: aaaabbbccz  Output: 4a3b2c1z"""

class Test:
    @staticmethod
    def fun(s):
        prev_char = s[0]
        count = 1
        result = ''
        for char in s[1:]:
            if char == prev_char:
                count += 1
            else:
                result += f'{count}{prev_char}'
                prev_char = char
                count = 1
        result += f'{count}{prev_char}'
        return result

if __name__ == '__main__':
    input_data = input("Enter data: ")
    print(f"Result: {Test.fun(input_data)}")