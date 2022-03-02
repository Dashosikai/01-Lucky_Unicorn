show_instructions = input("have you played this game"
    "before? ").lower()


if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

elif show_instructions == "y":
        print("display instructions")

elif show_instructions == "no" or  show_instructions == "n":
        print("display instructions")

elif show_instructions == "n":
        print("display instructions")

else:
        print("Please answer yes / no")
