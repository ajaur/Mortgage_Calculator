# Mortgage Calculator

This Python file contains fuctions commonly used to calculate mortgage payments.

## Background
This project was created to practice coding using Python.

## Classes
This file contains 3 different Classes used for organizing the mortgage calculations.
  1. Terms
  2. Monthly_PI_Calculation
  3. Total_Interest_Paid_for_Life_of_Loan

### Terms
#### Description: 
This Class houses the variables to be used in our 2 main calculations. These variables are unique terms that are input by the User for our individual mortgage. 
#### Usage:
 ```javascript
    if calculation_selection == '1':
        interest_rate = float(input("Enter the interest rate (in percentage): "))
        term = int(input("Enter the term in years: "))
        loan_amount = float(input("Enter the loan amount: "))
        total_tax_amount = float(input("Enter the total yearly tax amount (optional, enter 0 if not applicable): "))
        insurance_premium = float(input("Enter the total yearly insurance premium (optional, enter 0 if not applicable): "))
        monthly_pmi_amount = float(input("Enter the monthly PMI (Private Mortgage Insurance) amount (optional, enter 0 if not applicable): "))

        user_terms = Terms(interest_rate, term, loan_amount, total_tax_amount, insurance_premium, monthly_pmi_amount)
```

#### Reponse:
user_terms valiable is created which will be used when calling the mortgage calculator funtions.
 ```javascript
     pi_calculation = Monthly_PI_Calculation()
        pi_calculation.calculation(user_terms)
```
