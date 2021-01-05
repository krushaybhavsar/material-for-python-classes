
# instaniating variables depending on user input
x = int(input("First number: "))
y = int(input("Second number: "))

# asking user for operation
operation = int(input("What operation do you want to perform?\n1 ==> addition\n2 ==> subraction\n3 ==> multiplication\n4 ==> division\n>>> "))

# printing value depending on what operation user chose
if operation == 1:
    print(x + y)
elif operation == 2:
    print(x - y)
elif operation == 3:
    print(x * y)
elif operation == 4:
    print(x / y)