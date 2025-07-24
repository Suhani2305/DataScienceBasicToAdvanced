# name = input("Enter your name: ")
# print("Hello " + name)


"""PersonA = input("Enter the name of Person A: ")
PersonB = input("Enter the name of Person B: ")

AgeA = int(input("Enter the age of Person A: "))
AgeB = int(input("Enter the age of Person B: "))

if AgeA < AgeB:
    print(PersonA + " is younger than " + PersonB)
else:
    print(PersonA + " is older than " + PersonB)
""" 


# assignment : write a code by taking input off weight and height of a person and calculate its BMI index 


height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)
print("Your BMI is: {:.2f}".format(bmi))
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")