'''
Phone number is requested and give them nums in words
'''
nums=input("Enter your phone number  ")
Numbers_in_mapping={
        1:"one",
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "Six":6,
        "seven":7,
        "eight":8,
        "nine":9,
        "zero":0,
}
output=""
for ch in nums:
        output+=Numbers_in_mapping.get(ch,"!")
