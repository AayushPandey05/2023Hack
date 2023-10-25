message="Welcome to the tip calculator."
print (message)
bill=float(input("What was the total bill? ₹"))
people=int(input("How many people to split the bill? "))
#!.......Formula..........
bill_per_person = bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print (f"Each person should pay: ₹{final_amount}")
