def divide(num1, num2):
    return num1 / num2
def multiply(num1, num2):
    return num1 * num2
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2

print("please select operation -\n"  \
      "1.divide\n" \
      "2.multiply\n" \
      "3.add\n" \
      "4.subtract\n")
select = int(input("select operation form 1, 2, 3, 4 :"))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if select == 1:
    print(number_1,"/", number_2,"=",divide(number_1,number_2))
elif select == 2:
 print(number_1,"*", number_2,"=",multiply(number_1,number_2))
elif select == 3:
     print(number_1,"+", number_2,"=",add(number_1,number_2))
elif select == 4:
     print(number_1,"-", number_2,"=",subtract(number_1,number_2))
else:
    print('Invalid input')

