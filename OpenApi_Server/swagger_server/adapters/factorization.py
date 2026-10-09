def prime_factors(number):
    factors = []

    while number % 2 == 0:
        number = number // 2
        factors.append(2)

    currentFactor = 3
    while currentFactor * currentFactor <= number:
        if number % currentFactor == 0:
            number = number // currentFactor
            factors.append(currentFactor)
        else:
            currentFactor = currentFactor + 2

    if number > 2:
        factors.append(number)
        
    return factors