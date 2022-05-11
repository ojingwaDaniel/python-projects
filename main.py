perimeter = ('hours')
calculation_Of_Unit = 24
number = input('Enter a number:\n')
def firstFunction(num_days):
    if num_days > 0 :
     print (f"{num_days} days make {calculation_Of_Unit * num_days} {perimeter}")
    elif num_days == 0:
     print('You entered 0 please enter a positve number to convert')
    else:
        print('you entered a negative number NO conversion for u')
def validation():
   while True:
      if number.isdigit():
        Users_input = int(number)

        calculated_value = firstFunction(int(Users_input))
        print(calculated_value)
      else:
          print('Your input is not  valid')

validation()



























































































