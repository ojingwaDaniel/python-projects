# Given two integer numbers return their product only if the product is greater than 1000, else return their sum.
#
num1 = input('Enter a number :')
Num1 = int(num1)
num2 = input('Enter another number :')
Num2 = int(num2)
def check(appreciation):
    if (Num1 * Num2) > 1000:
       print(Num1 + Num2)
    else:
       print(Num1 * Num2)

check('thanks for using our program')
previous_num = 0

for i in range(10):

    sum = previous_num + i
    print(f'Current number {i} Previous Number {previous_num} is {sum}')
    previous_num = i


