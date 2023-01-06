print("Welcome to BMI calculator")
print()
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

print()


BMI = weight / height ** 2
BMI = float("{:.1f}".format(BMI))
if BMI < 18.5:
    print(f"Your BMI is {BMI} kg/m^2, you are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {BMI} kg/m^2, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI} kg/m^2, you are slightly Overweight.")
elif BMI >= 30 and BMI < 35:
    print(f"Your BMI is {BMI} kg/m^2, you are Obese.")
else:
    print(f"Your BMI is {BMI} kg/m^2, you are clinically Obese")
