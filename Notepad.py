
"""
price of house is $1m
if buyer have good credit put down 10 percent if  not put down 20
print down payment
"""
good_credit=False
down_payment=int(input("down payment amount:"))
if good_credit is True:
        print("they need to put down 10%")
        print((down_payment)* float(0.1))
else:
        print("they need to put down 20%")
        print((down_payment) * float(0.2))
print (f" Down payment is : ${down_payment}")