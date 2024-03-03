class Terms:
    def __init__(self, input_interest_rate_percentage, input_term_in_years, input_loan_amount, input_total_tax_amount = 0, input_insurance_premium = 0, input_monthly_pmi_amount = 0):
        self.interest_rate = input_interest_rate_percentage
        self.term = input_term_in_years
        self.loan_amount = input_loan_amount
        self.taxes = input_total_tax_amount
        self.insurance = input_insurance_premium
        self.pmi = input_monthly_pmi_amount

        
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
        



class Total_Interest_Paid_for_Life_of_Loan:
    def __init__(self):
        pass
    def calculation(self, terms):
        monthly_pi = ((terms.interest_rate / 100 / 12) * terms.loan_amount) / (1 - ((1 + (terms.interest_rate / 100 / 12)) ** (-(terms.term) * 12)))
        total_payments = monthly_pi * (terms.term * 12)
        total_interest_paid = total_payments - terms.loan_amount
        rounded_total_interest_paid = round(total_interest_paid, 2)
        
        print("The total interest paid for the life of the loan is:", rounded_total_interest_paid)

while True: 
    calculation_selection = input("Welcome to Mortgage Calculator. What would you like to calculate today? (Enter '1' for Monthly PI / Enter '2' for Total interest paid for life of loan): ")

    if calculation_selection == '1':
        interest_rate = float(input("Enter the interest rate (in percentage): "))
        term = int(input("Enter the term in years: "))
        loan_amount = float(input("Enter the loan amount: "))
        total_tax_amount = float(input("Enter the total yearly tax amount (optional, enter 0 if not applicable): "))
        insurance_premium = float(input("Enter the total yearly insurance premium (optional, enter 0 if not applicable): "))
        monthly_pmi_amount = float(input("Enter the monthly PMI (Private Mortgage Insurance) amount (optional, enter 0 if not applicable): "))

        user_terms = Terms(interest_rate, term, loan_amount, total_tax_amount, insurance_premium, monthly_pmi_amount)

        pi_calculation = Monthly_PI_Calculation()
        pi_calculation.calculation(user_terms)

    elif calculation_selection == '2':
        interest_rate = float(input("Enter the interest rate (in percentage): "))
        term = int(input("Enter the term in years: "))
        loan_amount = float(input("Enter the loan amount: "))

        user_terms = Terms(interest_rate, term, loan_amount)

        total_interest = Total_Interest_Paid_for_Life_of_Loan()
        total_interest.calculation(user_terms)
    

    else:
        print("Invalid choice. Please enter either '1' or '2'.")

    another_calculation = input("Would you like to make another calculation? (Enter 'yes' or 'no'): ")
    if another_calculation.lower() != 'yes':
        print("Thank you for using Mortgage Calculator. Goodbye!")
        break


