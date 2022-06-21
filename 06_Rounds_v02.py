import random

# set balance for testing purpoese
balance = 5

rounds_played = 0 

play_again = input("Press <Enter> to play...") .lower()
while play_again == "":

    #increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    
    chosen_num = random.randint(1, 100)
    
    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (sub $1 from balance)
    elif 6 <= chosen_num  <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5
    
    
    
    if balance < 1:
     # I fbalance is to low, exit the game and 
     # output a suitable message
     play_again = "xxx"

    play_again = input("Press Enter to play again"
                       "or 'xxx' to quit")  

print()
print("Final balance", balance)