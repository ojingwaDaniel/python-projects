perimeter = ('hours')
calculation_Of_Unit = 24

def firstFunction(num_days):
    if num_days > 0 :
        print(f"{num_days} days make {calculation_Of_Unit * num_days} {perimeter}")

def validation_and_execution():
    try:
        Users_input_number = int(num_of_days_element)
        if Users_input_number > 0 :
            calculated_value = firstFunction(Users_input_number)
            return (calculated_value)
        elif Users_input_number == 0:
            return ('You entered 0 please enter a positive number to convert')
        else:
            return ('you entered a negative number NO conversion for u')
    except ValueError:
        return ('you entered an invalid number')
users_input = ''
while users_input != 'exit':
    users_input = input('Enter a list a number of days separated by spaces and i will convert it for u :\n')
    for num_of_days_element in users_input.split():
        validation_and_execution()


























































































