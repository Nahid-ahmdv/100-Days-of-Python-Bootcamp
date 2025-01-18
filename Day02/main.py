#the final project of Day 02: Tip calculator.
print("Welcome to the Tip Calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
ppl = int(input("How many people to split the bill? "))
each_person = (100 + tip) * total / (100 * ppl)
print(f"Each person should pay: ${round(each_person, 2)}")
print(f"Each person should pay: ${each_person:.2f}")

