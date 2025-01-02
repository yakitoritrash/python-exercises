def is_leap_year():
    year = int(input("What year do you want to check? \n"))
    if year%4 == 0 and year%100 != 100 or year%400 == 0:
        print("True")
    else:
        print("False")

is_leap_year()
