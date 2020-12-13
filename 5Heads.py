# This program determines the probability of getting 5 heads in a row when flipping a coin
# five times per data set for n trials, n is determined by the user
import random

flag=0
count=0
FiveHcount=0
Normalcount=0
Totalcount=0

Trialnum=int(input("How many trials would you like to run? \n"))

while flag < Trialnum: # Runs the program for n (Trialnum) trials
	ht = []
	for i in range(0,5): # Creates the list of numbers (runs n times for n trials)
		ht.insert(i, (str(random.choice(['H', 'T']))) )

	print(ht) # Prints out the set of data
	print(" ")
	print("\n")

	if ht[0]=='H' and ht[1]=='H' and ht[2]=='H' and ht[3]=='H' and ht[4]=='H': # Checks if a set has all heads and records it
		FiveHcount = FiveHcount + 1
	else: # If a set of values does not contain all heads, then the set will be counted as not having 5 heads
		Normalcount = Normalcount + 1

	Totalcount=Totalcount+1 # Keeps track of the total amount of trials ran
	flag=flag+1 # The exit condition for the loop, when the desired trial number n is reached, the loop will break


print("")

print("Total number of times five H's occurred: " + str(FiveHcount))
print("Total number of times five H's did not occur: " + str(Normalcount))
print("Total number of trials ran: " + str(Totalcount))

print("")

prob=FiveHcount/Totalcount 
percent = prob*100

print("For " + str(Trialnum) + " trials")

print("The probability of you getting 5 heads in a row on a coin toss is approximately: \n" + str(FiveHcount) + "/" + str(Totalcount) + " or " + str(round(prob,4)) + " (" + str(round(percent,2)) +"%) \n")

input("(Press enter to exit the program) \n")