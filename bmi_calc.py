'''
BMI Calculator

Calculates body mass index from height and weight

Name, height in inches, weight in pounds	

BMI = (weight / height2) * 703

inputs:
- Name
- height in inches
- weight in pounds

process:
- calculate the BMI using the following equation
    -BMI = (weight / height2) * 703

outputs:
- BMI
* note about the way to interprite BMI

'''
# inputs
print("\nBMI is a calculation that helps individuals recognize if they are under, at, or over their healthy weight.")
print("\nTo calculate your BMI, please input the following information\n")
name = input("Name: ")
height = float(input("Height (in): "))
weight = float(input("Weight (lb): "))

# process
BMI = (weight / height ** 2) * 703

# outputs
print(f'\n{name}')
print(f'    - {height}')
print(f'    - {weight}')

print("\nThe following is your BMI score (rounded)")
print(f'{BMI:.3f}\n')