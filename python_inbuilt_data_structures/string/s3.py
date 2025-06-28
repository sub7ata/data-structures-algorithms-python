"""WAP to reverse internal content of each word"""
"""Ex: input: 'data structure and algorithm' output: 'atad erutcurts dna mhtirogla'"""

class StringReverser:
    @staticmethod
    def reverse(cont):
        empt_lst = []
        sp_s = cont.split()
        for each in sp_s:
            empt_lst.append(each[::-1])
        r = ' '.join(empt_lst)
        return r


if __name__ == "__main__":
    input_cont = input("Enter content: ")
    print(f"Result: {StringReverser.reverse(input_cont)}")