"""WAP for the following requirement?"""
"""Input: a4k3b2 Output: aeknbd"""

class Test:
    def fun(data):
        vlu = ''
        for ch in data:
            if ch.isalpha():
                pre_ch = ch
                vlu += ch
            elif ch.isdigit():
                digit = ord(pre_ch)
                vlu += chr(digit+int(ch))
        return vlu

if __name__ == '__main__':
    input_data = input("Enter data: ")
    print(f"Result: {Test.fun(input_data)}")