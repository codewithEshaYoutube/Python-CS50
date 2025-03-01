"""
logical operators
Example 1: if employee has high income and credit than eligible for loan
"""
high_income=True
high_credit=False
is_adult=True
if high_income and high_credit :
        print("Employee is eligible")
elif not is_adult:
        print("Candidate is underage")
        
else:
        print('not eligible')