def number_of_copies(n,m):
    if n < 0 or m < 0:
        return 0
    else:
        return n*m

def number_of_copies2(n,m):
    if n < 0 or m < 0:
        return 0
    return n*m
    
test = number_of_copies(5,5)
print(test)