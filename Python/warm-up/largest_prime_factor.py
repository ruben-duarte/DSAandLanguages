prime_numbers_to_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#info https://www.cuemath.com/numbers/prime-factorization/
def prime_factor_list(number):
    factors = []
    divisor = prime_numbers_to_100[0]
    
    while number / divisor > 1:
        for item in range(1,100):
            if number % divisor == 0:
                factors.append(divisor)
                number = number / divisor
                break
            elif number % divisor > 0:
                divisor = prime_numbers_to_100[item]
    return factors

test = prime_factor_list(600)
print(test)

#600851475143
