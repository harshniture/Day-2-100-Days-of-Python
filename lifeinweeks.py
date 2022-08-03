#Task 3 Life in weeks

age = int(input("What is your current age?"))

remaining_years = 90 - age
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365
remaining_months = remaining_years * 12

print("You have " + str(remaining_days) + " days, " + str(remaining_weeks) + " weeks, and " + str(remaining_months) + " months left.")