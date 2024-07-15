print("----Mini Calculator----")

num1 = float(input("enter first number here: "))
num2 = float(input("enter second number here: "))

print("press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress  4 for divison \npress 5 for remainder")
choice = int(input("Enter your choice from 1 to 4:"))
if choice== 1:
    print("The addition of two number is " ,num1 + num2)
elif choice == 2:
    print("The substraction of two number is " ,num1 - num2)
elif choice == 3:
    print("The multiplication of two number is " ,num1 * num2)
elif choice == 4:
    print("The division of two number is " ,num1  / num2)
elif choice == 5:
    print("The remainder of two number is " ,num1 % num2)
else:
    print("invalid choice")