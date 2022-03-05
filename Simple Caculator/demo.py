#Making a simple calculator using python.

#...A function adding two numbers.
def add(x,y):
    return x + y

#...A function subtraction two numbers.
def subtract(x,y):
    return x - y


#...A function multiplying two numbers.
def multiply(x,y):
    return x * y

#...A function dividing two numbers.
def divide(x,y):
    return x / y

print("select operation.")
print("1.add")    
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    choice =input("Enter option.")

    if choice in ("1","2","3","4"):
      num1 =int(input("First value."))
      num2 =int(input("Second value."))

      if choice == "1":
          print(add(num1,num2))
          pass
      elif choice == "2":
          print(subtract(num1,num2))
          break
      elif choice == "3":
          print(multiply(num1,num2))
          break
      elif choice == "4":
          print(divide(num1,num2))
          break

    else:
        print(" INVALID INPUT. Try again.")
          
def printsalary()
    salary = 12000
    
