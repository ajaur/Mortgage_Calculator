print("Welcome to Mortgage Calculator")
#Mortgage Calculator. Will calculate PITI as well as total interest and principal paid for the entirety of the loan. An estimate of montly T&I can also be calculated.
#inputs would be interest rate, loan amount, term, tax amount, insurane amount, and PMI amount.

print("What would you like to calculate today? (Monthly PI/Total interest and principal paid for life of loan)")
class Terms:
    def __init__(self, input_interest_rate_percentage, input_term_in_years, input_loan_amount, input_total_tax_amount = 0, input_insurance_premium = 0, input_monthly_PMI_amount = 0):
        self.interest_rate = input_interest_rate_percentage
        self.term = input_term_in_years
        self.loan_amount = input_loan_amount
        self.taxes = input_total_tax_amount
        self.insurance = input_insurance_premium
        self.PMI = input_monthly_PMI_amount

        
class Monthly_PI_Calculation:
    def __init__(self):
        pass

    def calculation(self, terms):
        monthly_pi = ((terms.interest_rate / 100 / 12) * terms.loan_amount) / (1 - ((1 + (terms.interest_rate / 100 / 12)) ** (-(terms.term) * 12)))
        rounded_monthly_pi = round(monthly_pi, 2)
        print("The monthly Principal and Interest Payment for this loan is ", rounded_monthly_pi)



class Total_PI_Paid_for_Life_of_Loan:
    pass

mortgage_one = Terms(2.5, 30, 260000)

mortgage_two = Terms(3.7, 20, 450000, 10000, 2500, 110)

pi_calculation = Monthly_PI_Calculation()

pi_calculation.calculation(mortgage_one)