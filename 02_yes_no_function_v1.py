

def yes_no(question):
    valid = False
    while not valid:
        respones = input(question).lower()

        if respones == "yes" or respones  == "y":
            return "yes"


        elif respones == "no" or  respones == "n":
            return "no"


        else:
            print ("Please anwser yes / no ")


show_instructions = yes_no("have you played the "
                           "game before? ")
print ("You chose {} ". format(show_instructions))
print()
having_fun = yes_no ("Are you having fun ")
print("you said {} to having fun".format(having_fun))