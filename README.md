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
 ```javascript
Terms:
    def __init__(self, input_interest_rate_percentage, input_term_in_years, input_loan_amount, input_total_tax_amount = 0, input_insurance_premium = 0, input_monthly_pmi_amount = 0):
        self.interest_rate = input_interest_rate_percentage
        self.term = input_term_in_years
        self.loan_amount = input_loan_amount
        self.taxes = input_total_tax_amount
        self.insurance = input_insurance_premium
        self.pmi = input_monthly_pmi_amount
```

#### Usage 1:
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

#### Reponse 1:
user_terms valiable is created which will be used when calling the Monyhly PI Calculation funtion.
 ```javascript
     pi_calculation = Monthly_PI_Calculation()
        pi_calculation.calculation(user_terms)
```
#### Usage 2:
 ```javascript
     elif calculation_selection == '2':
        interest_rate = float(input("Enter the interest rate (in percentage): "))
        term = int(input("Enter the term in years: "))
        loan_amount = float(input("Enter the loan amount: "))

        user_terms = Terms(interest_rate, term, loan_amount)
```
#### Reponse 2:
user_terms valiable is created which will be used when calling the Total Interest Paid for Life of Loan funtion.
 ```javascript
     total_interest = Total_Interest_Paid_for_Life_of_Loan()
        total_interest.calculation(user_terms)
```
### Monthly_PI_Calculation
#### Description: 
This Class holds the function to calculate the Monthly P&I, T&I and PITI.
```javascript
class Monthly_PI_Calculation:
    def __init__(self):
        pass

    def calculation(self, terms):
        monthly_pi = ((terms.interest_rate / 100 / 12) * terms.loan_amount) / (1 - ((1 + (terms.interest_rate / 100 / 12)) ** (-(terms.term) * 12)))
        rounded_monthly_pi = round(monthly_pi, 2)
        monthly_ti = terms.taxes / 12 + terms.insurance / 12 + terms.pmi
        rounded_monthly_ti = round(monthly_ti, 2)
        piti = round(rounded_monthly_pi + rounded_monthly_ti, 2)
        print("The monthly Principal and Interest Payment for this loan is", rounded_monthly_pi)
        if monthly_ti != 0:
            print("Your estimated monthly Tax and Insurance payment is", rounded_monthly_ti, "Your total estimated monthly PITI payment is", piti)
```
#### Usage:
```javascript
while True: 
    calculation_selection = input("Welcome to Mortgage Calculator. What would you like to calculate today? (Enter '1' for Monthly PI / Enter '2' for Total interest paid for life of loan): ") #user input is 1

    if calculation_selection == '1':
        interest_rate = float(input("Enter the interest rate (in percentage): ")) #user input is 2.5
        term = int(input("Enter the term in years: ")) #user input is 30
        loan_amount = float(input("Enter the loan amount: ")) #user input is 220000
        total_tax_amount = float(input("Enter the total yearly tax amount (optional, enter 0 if not applicable): ")) #user input is 4000
        insurance_premium = float(input("Enter the total yearly insurance premium (optional, enter 0 if not applicable): ")) #user input is 1000
        monthly_pmi_amount = float(input("Enter the monthly PMI (Private Mortgage Insurance) amount (optional, enter 0 if not applicable): ")) #user input is 0

        user_terms = Terms(interest_rate, term, loan_amount, total_tax_amount, insurance_premium, monthly_pmi_amount)

        pi_calculation = Monthly_PI_Calculation()
        pi_calculation.calculation(user_terms)
```
#### Response:
```javascript
The monthly Principal and Interest Payment for this loan is 869.27
Your estimated monthly Tax and Insurance payment is 416.67 Your total estimated monthly PITI payment is 1285.94
```
### Total_Interest_Paid_for_Life_of_Loan:
#### Description:
This Class holds the function to calculate the total interest that will be paid for the life of the loan.
```javascript
class Total_Interest_Paid_for_Life_of_Loan:
    def __init__(self):
        pass
    def calculation(self, terms):
        monthly_pi = ((terms.interest_rate / 100 / 12) * terms.loan_amount) / (1 - ((1 + (terms.interest_rate / 100 / 12)) ** (-(terms.term) * 12)))
        total_payments = monthly_pi * (terms.term * 12)
        total_interest_paid = total_payments - terms.loan_amount
        rounded_total_interest_paid = round(total_interest_paid, 2)
        
        print("The total interest paid for the life of the loan is:", rounded_total_interest_paid)
```
#### Usage:
```javascript
while True: 
    calculation_selection = input("Welcome to Mortgage Calculator. What would you like to calculate today? (Enter '1' for Monthly PI / Enter '2' for Total interest paid for life of loan): ")
    elif calculation_selection == '2':
            interest_rate = float(input("Enter the interest rate (in percentage): ")) #user input is 2.5
            term = int(input("Enter the term in years: ")) #user input is 30
            loan_amount = float(input("Enter the loan amount: ")) #user input is 220000
    
            user_terms = Terms(interest_rate, term, loan_amount)
    
            total_interest = Total_Interest_Paid_for_Life_of_Loan()
            total_interest.calculation(user_terms)
```
#### Response:
```javascript
The total interest paid for the life of the loan is: 92935.75
```
