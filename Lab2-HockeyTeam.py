# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations
"""
Student Name:   Kyle Preston    
Program Title:  HockeyTeam in class exericse 2  
Description:   A code that prints a team name, win, loss, win percent with four decimal
"""

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Variables
    Wins= int(0) 
    Losses= int(0)
    Team = ""
    Totalgames= int(0)
    WinLossPct= float(0.0)


    #Inputs
    #Team name input
    Team=input("Please enter team name: " )

    #Win input
    Wins=input("Please enter the amount of wins: ")

    #Losses input
    Losses=input("PLease enter the amount of losses: ")

    #Calculations for the code
    #Total games is wins + losses
    # WinlossPct is wins divided by total games
    
    Totalgames= int(Wins) + int(Losses)
    WinLossPct = int(Wins) / Totalgames

    
    #Output
    # display team name with wins, losses and win percentage with four decimal places using .format
    Output= "The {0} has {1} wins and {2} losses with a win percentage of {3:.4f}.".format(Team, Wins, Losses, WinLossPct)
    print(Output)








    # YOUR CODE ENDS HERE

main()