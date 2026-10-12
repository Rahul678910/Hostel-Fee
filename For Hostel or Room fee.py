# For Hostel 
# rent = int(input("Enter your hostel/flat rent = "))
# food = int(input("Enter the amount of food ordered = "))

# electricity_spend = int(input("Enter the total amount  of electricity spend = "))
# charge_per_unit = int(input("Enter the charge per unit = "))
# persons = int(input("Enter the number of persons living in room / flat = "))

# total_bill = electricity_spend * charge_per_unit

# output = (food + rent + total_bill) // persons

# print("Each persons should pay the amount of ", output)



accommodation_fee = int(input("Enter the monthly room/flat charge = "))
meal_cost = int(input("Enter the total food expenses = "))
units_used = int(input("Enter the electricity units consumed = "))
unit_rate = int(input("Enter cost per electricity unit = "))
total_residents = int(input("How many people are sharing the space? = "))

electricity_bill = units_used * unit_rate

combined_expense = accommodation_fee + meal_cost + electricity_bill

individual_share = combined_expense // total_residents

print("Each roommate needs to contribute ₹", individual_share)