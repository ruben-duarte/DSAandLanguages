class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def  __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

notes = Array(7, 5)
print(len(notes))
print(notes)

for i in range(len(notes)):
    notes[i] = i**2

print(notes)
print(notes[3])

for note in range(len(notes)):
    print(notes[note])

print(notes.__len__())
print(notes.__str__())
print(str(notes))
print(notes.__getitem__(3))
print(notes.__setitem__(3,10))

print(notes)