import time



start_time = time.time()

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

class Node: 
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_val(self):
        return self.value

    def get_next_node(self):
        return self.next_node 

    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def checkNodes(self, names_2):
        fl = self.head
        sl = names_2.head
        while (fl != None and sl != None):
            if (fl.value == sl.value):
                duplicates.append(fl.value)
            fl.next_node
            sl.next_node

f = open('names_1.txt', 'r')
names_1 = LinkedList()
names_1.add_to_head(f.read().split("\n"))  # List containing 10000 names
f.close()


f = open('names_2.txt', 'r')
names_2 = LinkedList()
names_2.add_to_head(f.read().split("\n"))  # List containing 10000 names
f.close()


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


