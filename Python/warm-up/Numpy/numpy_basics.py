import numpy as np

def divisor():
    print("="*30)
    print()

#crear un array
arr = np.array([1, 2, 3, 4,5])
#un elemento float transforma el resto
arr2 = np.array([1, 2, 3, 4.3,5])
print(arr)
print(type(arr))
divisor()
print(arr2)
divisor()
#recibe tuplas
arr3 = np.array((1, 2, 3, 4))
print(arr3)
divisor()

#strings
arr4 = np.array([1,2,3,"one"])
print(arr4)

divisor()
arr5 = np.array([[23,3,4,5,], [1,2,3,4]])
print(arr5)

divisor()
#slicing the array
print(arr[0:3])
print(arr5[0:2, 0:2])
print(arr5[0, 0:2])

divisor()
#atributes
print(np.shape(arr))
print(np.shape(arr5))
print(np.size(arr5))
print(np.ndim(arr5))
print(arr5.dtype)


