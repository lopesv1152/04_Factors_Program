# checks input is a number between 1 and 200 (yet to edit)
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

# Main Routine goes here

keep_going = ""
while keep_going == "":
    print()
    # ask user for an integer (must be between 1 and 200)
    var_integer = num_check("Enter an integer: ",range(1,200))
    print()
