import csv
from pathlib import Path

# base loan data to pull
loan_costs = [500, 600, 200, 1000, 450]

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
print(f"The future value of this loan is {Future_Value}, with a remaining time period of {Remaining_Months} months.")

#Present value calculation, with a determined Discount rate
Annual_Discount_Rate = 0.2
Present_Value = round(Future_Value / (1 + Annual_Discount_Rate/12) ** Remaining_Months, 2)
#printed these as checks for myself to confirm
print(f"The Present Value of this loans is {Present_Value}")
print(f"The Loan Price is {Loan_Price}")


if Present_Value>Loan_Price or Present_Value==Loan_Price:
    print("The Loan is worth at least the cost to buy it.")
else:
    print("The Loan is too expensive and not worth the price.")

#Part 3: Perform Financial Calculations.