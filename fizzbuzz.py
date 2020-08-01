num1 = [3, 6, 9, 12, 15]
num2 = [5, 10, 15, 20, 25]
num1.extend(num2)
#print(three)

def Fizzbuzz(num1, num2):
    if ((num1 % 5 == 0) and (num1 % 3 == 0)):
        print("Fizzbuzz")
    elif (num1 % 5 == 0):
        print("Buzz")
    elif (num1 % 3 == 0):
        print("Fizz")
    else:
        print("Not divisible")

Fizzbuzz(num1, num2)

