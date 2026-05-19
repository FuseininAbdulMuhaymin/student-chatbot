#Test 1
from binascii import Error


name = str(input('Enter your name:'))
age = int(input('Age :'))
print('Your name is ' + str(name) + '  it left  reach with  ' + str(100 - int(age)) + ' to turn 100 years old')

 
#Test 2

first_number = int(input('Enter first number:'))
second_number = int(input('Enter second number:'))
operator = input('Enter the operator (+, -, *, /):')

if operator == '+':
    calculate = first_number + second_number
elif operator == '-':
    calculate = first_number - second_number
elif operator == '*':
    calculate = first_number * second_number
elif operator == '/' :
    calculate = first_number / second_number


print('The result is: ' + str(calculate))


#Test 3

scores = []
for i in range(5):
    while True:
        try:
            s = float(input(f"Enter score #{i+1}: "))
            break
        except Error:
            print("Please enter a valid number.")
    scores.append(s)

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

print("Scores:", scores)
print("Highest:", highest)
print("Lowest:", lowest)
print(f"Average: {average:.2f}")