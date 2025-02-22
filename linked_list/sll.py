class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Test:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def display(self):
        temp = self.head
        if self.head == None:
            return
        print("[ ", end="")
        while temp != None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(" None ]")

    def insert_first(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def insert_any_position(self, position, data):
        temp = Node(data)
        if position == 0:
            self.insert_first(data)
        else:
            cur = self.head
            for i in range(position-2):
                cur = cur.next
                if cur == None:
                    return self.head
            temp.next = cur.next
            cur.next = temp

    def insert_last(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)

    def update_first(self, new_data):
        if self.head == None:
            return
        else:
            temp = self.head
            temp.data = new_data
            self.head = temp

    def update_any_position(self, position, new_data):
        if self.head.data is None:
            print("List is empty!")
            return None
        else:
            temp = self.head
            index = 0
            while temp != None:
                if index == position:
                    temp.data = new_data
                temp = temp.next
                index += 1

    def update_last(self, new_data):
        if self.head == None:
            return
        else:
            temp = self.head
            temp.data = new_data
            self.head = temp

    def delete(self):
        if not self.head:
            print("List is empty!")
            return None
        if not self.head.next:
            return None
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        return self.head

    def delete_any_position(self, position):
        if self.head is None:
            print("List is empty!")
            return None
        elif position < 0 or position > obj.count():
            print("Invalid Position!")
        else:
            temp = self.head
            index = 0
            prev = None
            if position == 0:
                self.head = temp.next
                temp=None
                return None
            
            while temp and index < position:
                prev = temp
                temp = temp.next
                index += 1

            if temp is None:
                print("Position out of range!")
                return
            
            prev.next = temp.next
            temp = None

    def delete_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        del temp
        return self.head

    def reverse(self):
        curr = self.head
        prev = None
        while curr!=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def printlist(self):
        temp = self.head
        if temp==None:
            print("List is empty")
            return
        while temp != None:
            print (temp.data,end=" => ")
            temp = temp.next
        print("None")
        print(f"COUNT: {obj.count()}")

    def count(self):
        temp = self.head
        c = 0
        while temp != None:
            c=c+1
            temp = temp.next
        return c


obj = Test()
while True:
    print("\n+++++++++++++++++:MENU:+++++++++++++++++")
    print("\
        1.Insert\n\
        2.Insert first\n\
        3.Insert any position\n\
        4.Delete\n\
        5.Delete first\n\
        6.Delete any position\n\
        7.Update\n\
        8.Update first\n\
        9.Update any position \n\
        10.Reverse\n\
        11.Display\n\
        0.Exit"
        )
    print("***********:Enter your choice:***********\n")
    i = int(input())
    
    match i:
        case 1:
            value = input(f"Enter the value to insert: ")
            obj.insert_last(value)
            print(obj)
            obj.printlist()

        case 2:
            value = input(f"Enter the value to insert: ")
            obj.insert_first(value)
            print(obj)

        case 3:
            position = int(input(f"Enter the position: "))
            value = input(f"Enter the value to insert: ")
            obj.insert_any_position(position, value)
            print(obj)

        case 4:
            obj.delete()
            print(obj)

        case 5:
            obj.delete_first()
            print(obj)

        case 6:
            position = int(input(f"Enter the position: "))
            obj.delete_any_position(position)
            print(obj)

        case 8:
            value = input(f"Enter the value to update: ")
            obj.update_first(value)
            print(obj)

        case 9:
            position = int(input(f"Enter the position: "))
            value = input(f"Enter the value to insert: ")
            obj.update_any_position(position, value)
            print(obj)

        case 10:
            obj.reverse()
            print(obj)

        case 11:
            obj.printlist()
        case 0:
            break

        case _:
            print("Unknow value")