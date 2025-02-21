

class  Solution:
    def roman_to_int(nums):
        roman_map = [("M",1000),("CM",900),("D",500),("CD",400),
                     ("C",100),("XC",90),("L",50),("X",10),("V",5),("IV",4),("I",1)]
        numeral = " "
        for value,symbol in roman_map:
            while nums >=value:
                numeral += symbol
                nums-=value
            return numeral



