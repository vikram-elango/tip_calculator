print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
tip = float(input("What percentage of the tip would you like to give? 10, 12, or 15 \n"))/100*bill

total=bill+tip
people = int(input("How many people to split the bill?\n"))
each=round(total/people,2)
print(f"Each person should pay: ${each}")
