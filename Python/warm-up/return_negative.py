def  return_negative_number(number):
    if number == 0:                    #revisar si hay codigo innecesario, ejm cuando number *0
        return 0
    elif number < 0:
        return number
    else:   
        return number*(-1)
    
a = return_negative_number(-3)
b = return_negative_number(0)
c = return_negative_number(8)

print(a)
print(b)
print(c)

def make_negative_number(number):
    if number < 0:
        return number
    return number*-1
