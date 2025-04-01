mars_multiple=0.397
def mass_converter():
    weight_on_Earth=input("What is your weight at Mars? ")
    weight_on_Earth_int=int(weight_on_Earth)
    weigth_on_Mars=weight_on_Earth_int  * mars_multiple
    print(f"This is  your weight on  Mars {weigth_on_Mars}")


if __name__=="__main__":
    mass_converter()
                                 

