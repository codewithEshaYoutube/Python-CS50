'''
Phone number is requested and give them nums in words
'''
nums=input("Enter your phone number  ")

Numbers_in_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output=""

output="".join(Numbers_in_mapping.get(ch,"!")for ch in nums)
print (output)
