"""WAP to remove duplicate characters from the given input String?"""
"""Input: AZZZBCDABBCDABBBBCCCCDDDDEEEEEF Output: AZBCDEF """

class Test:
    def __init__(self, input_data):
        self.input_str = input_data

    def fun1(self):
        output_str = ''
        for itm in self.input_str:
            if itm not in output_str:
                output_str += itm
        return output_str

    def fun2(self):
        lst = []
        for itm in self.input_str:
            if itm not in lst:
                lst.append(itm)
        return ''.join(lst)

    def fun3(self):
        return ''.join(set(self.input_str))

if __name__ == '__main__':
    input_string = input("Enter data: ")
    object = Test(input_string)
    print(f"Result1: {object.fun1()}")
    print(f"Result2: {object.fun2()}")
    print(f"Result3: {object.fun3()}")