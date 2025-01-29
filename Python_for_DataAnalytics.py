print("I am a Data Nerd")
#  Commenting we use "#"

"""
This is for multi line comments use delimiters


"""
#Numeric Functions
print(1*4)
print(4*6)
print(4*6+6)#Bodmas Rule  (Bracket of Division,Multiplication,addition,Substraction)


#Vairables
salary = 10000
print(salary)
print("salary")
base_salary = 10000
bonus_rate = 1.7
Total_salary = (base_salary)*(1+ bonus_rate)
print(Total_salary)
"""
Runtime result:
The slowest run took 16.13 times longer than the fastest. This could mean that an intermediate result is being cached.
327 µs ± 216 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

"""
type(Total_salary)
title = "Dick Johnson Is Dead"
print(title)
type(title)
help (int)
patient_name = "Zahid"
patient_age = 25
patient_is_new = True
patient_health_is_critical = True
def print_patient_details():
  print(f"Patient Details:")
  print(f"Patient Name:{patient_name}")
  print(f"Patient Age:{patient_age}")
  print(f"Patient Is New:{patient_is_new}")
  print(f"Patient Health is critical:{patient_health_is_critical} ")




print_patient_details()

# Numeric Modules
salary_employee =[22,45,789,789,888]
import statistics
print(statistics.mean(salary_employee))
print(statistics.mode(salary_employee))
print(statistics.median(salary_employee))