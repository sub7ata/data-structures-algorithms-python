"""WAP to reverse order of words present in the given string"""
"""Ex: input: 'data structure and algorithm' output: 'algorithm and structure data'"""

class StringReverser:
    @staticmethod
    def reverse(cont):
        s = cont.split()
        r = s[::-1]
        print(' '.join(r))


if __name__ == "__main__":
    input = input("Enter content: ")
    StringReverser.reverse(input)