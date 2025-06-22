"""WAP To reverse the internal content of every second word in the string"""
"""Ex: intput: 'one two three four five six' output: 'eno two eerht four evif six'"""

class StringReverser:
    @staticmethod
    def reverse_func(cont):
        lst = list()
        s = cont.split()
        for idx, item in enumerate(s):
            if idx % 2 == 0:
                lst.append(item[::-1])
            else:
                lst.append(item)
        return ' '.join(lst)


if __name__ == "__main__":
    input_data = input("Enter the content: ")
    print(f"Result: {StringReverser.reverse_func(input_data)}")