import random
from termcolor import colored

def try_me():

    #Enter the minimum and maximum limits of the dice rolls below

    min_val = 1

    max_val = 6

    player_1 = input(colored("Please type the name of the first player: ","yellow"))
    player_2 = input(colored("Please type the name of the second player: ","yellow"))

    #the variable that stores the user’s decision

    roll_again = "yes"

    #The dice roll loop if the user wants to continue

    while roll_again == "yes" or roll_again == "y":

        print(colored("Dices rolling...","blue"))

        print(colored("The values are :","blue"))

        #Printing the randomly generated variable of the first dice

        print(colored(f"{player_1}\'s number: {random.randint(min_val, max_val)}","red"))

        #Printing the randomly generated variable of the second dice

        print(colored(f"{player_2}\'s number: {random.randint(min_val, max_val)}","green"))

        #Here the user enters yes or y to continue and any other input ends the program

        roll_again = input(colored("Roll the Dices Again?","yellow"))

    else:
        print(colored("Game over! :D","blue"))
