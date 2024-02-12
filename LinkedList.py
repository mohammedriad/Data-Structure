class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = Node()

    def append(self, value):
        cur = self.head
        new_node = Node(value)
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        temp = []
        cur = self.head

        while cur.next != None:
            cur = cur.next
            temp.append(cur.data)
        return temp

    def length(self):
        count = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            count += 1
        return count

    def get(self, index):
        if index >= self.length() or index < 0:
            raise IndexError("Index Out Of Range : ")

        cur_idx = 0
        cur = self.head
        while True:
            cur = cur.next
            if index == cur_idx:
                return cur.data
            cur_idx += 1

    def delete(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return

        cur = self.head
        cur_idx = 0
        while True:
            last_node = cur
            cur = cur.next
            if cur_idx == index:
                last_node.next = cur.next
                return
            cur_idx += 1


def __getitem__(self, index):
    return self.get(index)


x = Linkedlist()
x.append(1)
x.append(2)
x.append(3)
print(x.display())
print(x.length())
x.delete(0)
print(x.get(1))
print(x.display())
