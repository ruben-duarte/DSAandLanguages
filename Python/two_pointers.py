"""
two sum problem in a sorted list
"""
arr = [2,4,5,6]
target = 11

# [5,6]

#brute force 

def two_sum0(arr, target):
    addition = 0
    solution = []
    for num in range(len(arr)-1):
        for i in range(len(arr)):
            addition = arr[num]+arr[i] 
            print("addition: ",addition)
            print("arr[num] ", arr[num], "arr[i]", arr[i])
            if addition == target:
                solution.append(arr[num])
                solution.append(arr[i])
                break
    return solution

test = two_sum0(arr, target)
print(test)


# two pointers technique
def two_sum1(arr, target):
    pointer_1 = 0
    pointer_2 = len(arr) -1

    while pointer_1 < pointer_2:
            addition = arr[pointer_1] + arr[pointer_2]
            if addition < target:
                pointer_1 += 1
            elif addition > target:
                pointer_2 += 1
            else:
                return [arr[pointer_1], arr[pointer_2]]
    return False

test1 = two_sum1(arr, target)
print(test1)



