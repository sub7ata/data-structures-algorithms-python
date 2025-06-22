"""WAP to reverse the content of the given string"""
"""Ex: input: abcde | output: edcba"""

class StringReverser:
    """using the slice operator"""
    @staticmethod
    def reverse(text):
        return text[::-1]
    
    """using the reversed() function"""
    @staticmethod
    def reverse1(text):
        return "".join(reversed(text))
    
    """using the while loop"""
    @staticmethod
    def reverse2(text):
        new_text = ''
        l = len(text) - 1
        while l >= 0:
            new_text = new_text + text[l]
            l -= 1
        return new_text


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print("Reversed string:", StringReverser.reverse(input_string))
    print("Reversed string:", StringReverser.reverse1(input_string))
    print("Reversed string:", StringReverser.reverse2(input_string))

