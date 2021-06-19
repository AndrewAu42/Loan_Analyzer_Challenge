import csv
from pathlib import Path

# base loan data to pull
loan_costs = [500, 600, 200, 1000, 450]

#spacing between sections for breaks
print(" ")
print("----------------------------------------------------")
print(" ")

#Part 1: Automating the Calculations
#Count the function with LEN() function
Number_Of_Loans = len(loan_costs)
print(f"The number of loans in is {Number_Of_Loans}")

#Adding everything in the dictionary for loans together
Total_Value_Loans = sum(loan_costs)
print(f"The total value of the loans is {Total_Value_Loans}")

#Average Calculation based on the previous definitions 
Average_Loan_amount = Total_Value_Loans / Number_Of_Loans
print(f"The average amount per loan is {Average_Loan_amount}")

#spacing between sections for breaks
print(" ")
print("----------------------------------------------------")
print(" ")

#Part 2: Analyze Loan Data

#provided loan data to reference
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#defining the terms based on the loan dictionary that is provided above
Loan_Price = loan.get('loan_price')
Future_Value = loan.get('future_value')
Repayment_Interval = loan.get('repayment_interval')
Remaining_Months = loan.get('remaining_months')
print(f"The future value of this loan is ${Future_Value}, with a remaining time period of {Remaining_Months} months.")

#Present value calculation, with a determined Discount rate, as well as added a round function to make it easier, however if it reiterates, round at result not calculation
Annual_Discount_Rate = 0.2
Present_Value = round(Future_Value / (1 + Annual_Discount_Rate/12) ** Remaining_Months, 2)

#printed these as checks for myself to confirm
print(f"The Present Value of this loans is {Present_Value}")
print(f"The Loan Price is {Loan_Price}")


if Present_Value>Loan_Price or Present_Value==Loan_Price:
    print("The Loan is worth at least the cost to buy it.")
else:
    print("The Loan is too expensive and not worth the price.")

#spacing between sections for breaks
print(" ")
print("----------------------------------------------------")
print(" ")

#Part 3: Perform Financial Calculations.

#dictionary reference for new loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#basic present value calculation, using the above formula as reference, however we're going to use this function for ease of use, same properties as above
def present_value(future_value,remaining_months,annual_discount_rate):
    present_value = round(future_value / (1 + annual_discount_rate/12) ** remaining_months, 2)
    return present_value

#added new naming convention to track updates from the dictionary above, and a quick reference from grabbing it
new_loan_Future_Value = new_loan.get('future_value')
new_loan_Remaining_Months = new_loan.get('remaining_months')
new_loan_Discount_Rate = 0.2

new_car_loan_Present_Value = present_value(new_loan_Future_Value,new_loan_Remaining_Months,new_loan_Discount_Rate)

print(f"The present value of the loan is: {new_car_loan_Present_Value}")

#spacing between sections for breaks
print(" ")
print("----------------------------------------------------")
print(" ")

#Part 4: Conditionally filter lists of loans.

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#list definition to iterate and pull, starts out blank
inexpensive_loans = []

# pulling the dictionary through loop, and trying to define whether it is <=500$ to add to list
for loan_value in loans:
    if loan_value["loan_price"] <=500:
        inexpensive_loans.append(loan_value)

# Printing out the results of the value in the loan price 
print(f"The list of inexpensive loans include: {inexpensive_loans}")

#spacing between sections for breaks
print(" ")
print("----------------------------------------------------")
print(" ")

# # Part 5: Save the results.

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

#Writing and puting the files out to the CSV file, and making sure its following the info from Part 4 loops/list

print(f"Updating File here:{output_path}")
with open(output_path,'w',newline=' ') as csvfile:
   writer = csv.writer(csvfile)
   writer.writerow(header)
   for row in inexpensive_loans:
       writer.writerow(row.values())
print('Completed! Double Check the File!')

#spacing between sections for breaks
print(" ")
print("----------------------------------------------------")
print(" ")
