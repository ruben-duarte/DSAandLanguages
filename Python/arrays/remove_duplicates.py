from array_1 import Array01

original_array = Array01(8)
original_array.insert(1)
original_array.insert(2)
original_array.insert(2)
original_array.insert(3)
original_array.insert(3)
original_array.insert(4)
original_array.insert(4)
original_array.insert(5)
print(original_array)
#Remove duplicates from a sorted array

#using extra space
temp_array= Array01(len(original_array))
print(temp_array)

index_temp_array = 0
for number in range(len(original_array) - 1):  #para evitar index out of range el rango es len(list) - 1 porque inicia en 0
    if number <= len(original_array) -1:
        if original_array[number] != original_array[number + 1] :
            temp_array[index_temp_array] = original_array[number]
            index_temp_array += 1
temp_array[index_temp_array] = original_array[len(original_array)-1]  

print(temp_array)


