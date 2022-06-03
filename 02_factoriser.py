# gets factors, returns a sorted list
def get_factors(to_factor):
    comment = ""
    factor_list = []

    # Check if the value is 1
    if to_factor == 1:
        return "1 is UNITY! It only has one factor, itself."  
    
    for number in range(1, to_factor+1):
        if to_factor%number == 0:
            factor_list.append(number)
    comment = "{}".format(factor_list)

    # comments for square / primes
    if len(factor_list) == 2:
        comment += " {} is a prime number.".format(to_factor)
    elif len(factor_list) % 2 == 1:
        comment += " {} is a perfect square".format(to_factor)

    return comment


while True:
    print()
    # find factors from integer
    factors = get_factors(int(input()))
    print(factors)
