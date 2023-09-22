def sum_of_squares(nums):
    total = 0 #O(1)
    for number in nums: #O(n)
        total += number**2
    return total

a = sum_of_squares([1,2])
print(a)

def sum_of_squares_2(nums):
    return sum([number**2 for number in nums]) #O(n)

b = sum_of_squares_2([1,2])
print(b)

