# checks input is a number more than a given value
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

while True:
    print()
    # ask user for an integer (must be between 1 and 200)
    var_to_factor = num_check("Enter an integer: ")

