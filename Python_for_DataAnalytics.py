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
data_science_jobs = [
    {'job_title': 'Data Scientist', 'job_skills': "['Python', 'SQL', 'Machine Learning']", 'job_date': '2023-05-12'},
    {'job_title': 'Machine Learning Engineer', 'job_skills': "['Python', 'TensorFlow', 'Deep Learning']", 'job_date': '2023-05-15'},
    {'job_title': 'Data Analyst', 'job_skills': "['SQL', 'R', 'Tableau']", 'job_date': '2023-05-10'},
    {'job_title': 'Business Intelligence Developer', 'job_skills': "['SQL', 'PowerBI', 'Data Warehousing']", 'job_date': '2023-05-08'},
    {'job_title': 'Data Engineer', 'job_skills': "['Python', 'Spark', 'Hadoop']", 'job_date': '2023-05-18'},
    {'job_title': 'AI Specialist', 'job_skills': "['Python', 'PyTorch', 'AI Ethics']", 'job_date': '2023-05-20'},
    {'job_title': 'Data Science Intern', 'job_skills': "['Python', 'Pandas', 'Data Visualization']", 'job_date': '2023-06-01'},
    {'job_title': 'Deep Learning Engineer', 'job_skills': "['Python', 'Keras', 'Neural Networks']", 'job_date': '2023-06-05'},
    {'job_title': 'Big Data Engineer', 'job_skills': "['Java', 'Hadoop', 'Spark']", 'job_date': '2023-06-10'},
    {'job_title': 'Quantitative Analyst', 'job_skills': "['Python', 'R', 'Statistics']", 'job_date': '2023-06-15'},
    {'job_title': 'Cloud Data Engineer', 'job_skills': "['AWS', 'Python', 'Data Pipeline']", 'job_date': '2023-06-18'},
    {'job_title': 'Business Intelligence Analyst', 'job_skills': "['Power BI', 'SQL', 'Data Analysis']", 'job_date': '2023-06-20'},
    {'job_title': 'AI Research Scientist', 'job_skills': "['Python', 'TensorFlow', 'Natural Language Processing']", 'job_date': '2023-06-25'},
    {'job_title': 'Data Analytics Manager', 'job_skills': "['SQL', 'Leadership', 'Data Modeling']", 'job_date': '2023-07-01'},
    {'job_title': 'Data Visualization Engineer', 'job_skills': "['JavaScript', 'D3.js', 'Tableau']", 'job_date': '2023-07-05'}
]
from datetime import datetime
print(datetime.now())
type((data_science_jobs[0]))

