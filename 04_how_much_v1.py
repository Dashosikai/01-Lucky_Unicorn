# Functions go here


# Main routine go here

error = "Please enter an whole number between 1 and 10"

valid = False
while not valid:
    # ask the question
    response = int(input("How much would you"
                         "like to play with?"))
    # if the amoun tis too low / too high give
    if 0 < response <= 10:
        print ("You have asked to play"
               "with ${}".format(response))

    # output an error
    else:
        print(error)
