print("Welcome to the tip calculator!")
bill = input("What is the bill total? in €: ")
people = input("how man people that bill need to be divided to? ")
tip = input("Enter the tip percentage: ")

splitted_bill = float(bill) / int(people)
pay_per_person = splitted_bill * (1 + float(tip) / 100)

# Round the result to 2 decimal places.
final_amount = "{:.2f}".format(pay_per_person)

print(f"Each person should pay: €{final_amount}")
