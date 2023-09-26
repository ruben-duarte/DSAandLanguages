import random

class Array01:
    def __init__(self, capacity, fill_value=None):
        self.items = []
        self.index = 0
        for i in range(capacity):
            self.items.append(fill_value)
        
    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __fill__(self):
        for i in range(len(self.items)):
            self.items[i] = random.randint(0,9)

    def __add_items__(self):  #sin dunder muestra es el objeto en memoria
        sum = 0
        for i in range(len(self.items)):    
            sum += self.items[i]
        return sum
    
    def __sum__(self):
        return sum(self.items)

    def insert(self, item):     #index era una variable local se reiniciaba en cero, solucion variable con mayor scope self.index
        if self.index < len(self.items):
            self.items[self.index] = item
            self.index += 1
        else:
            print("Index out of range")

    def insert_at(self, value, ubication):
        pointer = 0
        #check if index is occupied
        if self.items[ubication] != None:
        #if true , move the consecutive items to the next position and insert the value            
            for item in range(len(self.items)):
                if self.items[item] is None:
                    pointer = item
                    break
            for item in range(pointer , ubication , -1):
                self.items[item] = self.items[item-1]
            self.items[ubication] = value
        # else insert in the position of index
        else:
           pass

# array_1 = Array01(3)
# print(array_1)
# array_1.__fill__()
# print(array_1)
# print("sum: ", array_1.__sum__())
# print("sum: ", array_1.__add_items__())

# array_test = Array01(4)
# print(array_test)
# array_test.insert(10)
# array_test.insert(20)
# print(array_test)
# array_test.insert(30)
# array_test.insert(40)
# print(array_test)
# array_test.insert(50)
# print(array_test)

insert_array = Array01(8)
print(insert_array)
insert_array.insert(34)
insert_array.insert(23)
insert_array.insert(12)
insert_array.insert(120)
insert_array.insert(-5)
print(insert_array)
print(insert_array.insert_at(23,1))
print(insert_array)
