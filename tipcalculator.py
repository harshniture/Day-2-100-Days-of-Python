# Tip Calculator

print("Welcome to Tip Calculator")
bill = input("What is the bill amount: ")
tip = input("What is the tip percentage 10, 12 or 15: ")
people = input("How many people to split the bill: ")
bill_with_tip = (float(bill) * float(tip) / 100) + float(bill)
your_pay = bill_with_tip / int(people)
print("Your total is: " + str(your_pay))