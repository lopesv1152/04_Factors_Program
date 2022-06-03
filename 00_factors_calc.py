# Functions go here

# Puts series of symbols at start and end of text (for empasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Enter an integer (a number which does not have a decimal part) between 1 and 200.")
    print()
    print("The calculator will list the factors of your integer in ascending order. The calculator will also specify if it is UNITY (has only one factor), a prime number (only divisible by one and itself), or a perfect square.")
    print()
    print("After completing your calculation, press <enter> to do more calculations or any key to quit the program.")
    print()
    return ""


# checks input is between 1 and 200
def num_check(question):
    try:
        # ask user to enter a number
        response = int(input(question))

        # checks number is more than zero
        if 1 <= response <= 200:
            return response
        
        # outputs error if input is invalid
        else:
            if response <= 0:
                print("Please enter an integer that is more than (or equal to) 1")
            else:
                print("Please enter an integer that is less than (or equal to) 200")
            print()

    except ValueError:
        print("Please enter an integer between 1 and 200")
    return ""

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


# Main Routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":
    # ask user for an integer (must be between 1 and 200)
    var_to_factor = num_check("Enter an integer: ")
    if var_to_factor != "":

        print()
        # find factors from integer
        comment = get_factors(var_to_factor)
        print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()