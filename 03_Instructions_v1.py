
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


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""




played_before = yes_no("have you played the "
                           "game before? ")

if played_before == "no":
   instructions()
 
print("Programs Continues")