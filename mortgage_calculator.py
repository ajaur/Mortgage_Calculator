print("Welcome to Mortgage Calculator")
#Mortgage Calculator. Will calculate PITI as well as total interest and principal paid for the entirety of the loan. An estimate of montly T&I can also be calculated.
#inputs would be interest rate, loan amount, term, tax amount, insurane amount, and PMI amount.

print("What would you like to calculate today? (Monthly PI/Total interest and principal paid for life of loan)")
class Terms:
    def __init__(self, input_interest_rate, input_term_in_months, input_loan_amount, input_total_tax_amount = 0, input_insurance_premium = 0, input_monthly_PMI_amount = 0):
        self.interest_rate = input_interest_rate
        self.term = input_term_in_months
        self.loan_amount = input_loan_amount
        self.taxes = input_total_tax_amount
        self.insurance = input_insurance_premium
        self.PMI = input_monthly_PMI_amount
        
class Monthly_PI_Calculation:

class Total_PI_Paid_for_Life_of_Loan:

mortgage_one = Terms(2.5, 360, 260000)