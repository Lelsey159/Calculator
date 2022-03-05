# Python program to check if the year is a leap year.

year =int(input("Enter the year."))

if(year % 4 == 0): #and (year % 100 == 0):
    print("Is a leap year.")

elif(year % 4 == 0): #and (year % 100 != 0):
    print("Is a leap year.")

else:
    print("Not a leap year.")
    