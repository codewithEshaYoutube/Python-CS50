course = ("This is python code")
price=44
#methods
print(len(course))
print(len(course))
print(course.upper())
print(course.lower())
print(course.find("is"))

print(course.replace("is","is best"))
#operator
print('is' in course)
#old string method
print(course, "price is ",[price],' USD')
#formatted strings
print(f'{course}  price is [{price}] USD')