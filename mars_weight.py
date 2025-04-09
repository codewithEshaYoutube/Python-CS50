# defining constant as mars multiple
MARS_MULTIPLE = 0.378


def main():
    # declaring Variable and getting input from user
    earth_mass = input("what is your weight on earth? ")

    # the input in string to float is called typecasting
    earth_mass_float = float(earth_mass)

    # Defining Mars weight calculation formula and assigning variable
    mars_mass = (MARS_MULTIPLE * earth_mass_float)

    # printing string concatenation (combining two strings into one)
    print("this is equivalent weight on Mars" + str(mars_mass))


if __name__ == "__main__":
    main()


