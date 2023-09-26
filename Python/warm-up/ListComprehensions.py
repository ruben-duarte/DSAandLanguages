"""
Let's learn about list comprehensions! You are given three integers x,y,z and  representing the dimensions of a cuboid along with an integer n . Print a list of all possible coordinates given by (i,j,k)  on a 3D grid where the sum of i+j+k is not equal to n . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.


links https://byjus.com/maths/permutation/
https://stackoverflow.com/questions/18551458/how-to-frame-two-for-loops-in-list-comprehension-python

https://www.geeksforgeeks.org/range-to-a-list-in-python/

"""
x,y,z = 1,1,2
n = 3
i = [*range(x+1)]
j = [*range(y+1)]
k = [*range(z+1)]

for x in i:
    for y in j:
        for z in k:
            print([x,y,z])

result = [[x,y,z] for x in i for y in j for z in k if sum([x,y,z]) != n]
print(result)

