# checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter a number between 1 and 200".format()

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if 1>=response>=200:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

keep_going = ""
while keep_going == "":
    print()
    # ask user for an integer (must be between 1 and 200)
    var_to_factor = num_check("Enter an integer: ")
    print()

