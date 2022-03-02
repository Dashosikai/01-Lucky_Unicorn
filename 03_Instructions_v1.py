


def yes_no(question):...



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