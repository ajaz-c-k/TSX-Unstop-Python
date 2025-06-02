def leap_year(year):
    if year%4==0 and year%100!=0:
        print("This is a leap year.")
        return True
    elif year%400==0:
        print("This is a leap year.")
        return True
    else:
        print("This is not a leap year. Oops!")
        return False

a=int(input("Enter A year to check whether it is leap year or not :"))

leap_year(a)
