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
    print("Write information on the factors calculator", "=")
    print()
    print("Write another line of instruction.")
    print()
    print("Write another line of instruction.")
    print()
    return ""


# checks input is a number between 1 and 200 (yet to edit)???
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter a number between 1 and 200".format(low)

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >=1 <=200:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# gets factors, returns a sorted list
def get_factors(to_factor):
    print("just filling this out to stop the angry-ness")

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

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number? ")

    if var_to_factor !=1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself :)"
    
    # comments for square / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)
    
    # output factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special..."
    
    else:
        heading = "Factors of {}".format(var_to_factor)
    
    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()