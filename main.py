from CalorificInformation import personalCalorieInfo
import Exercise

#This is the main file that will run the program

#Getting information from the user and error checking
print("Please fill out the following details for the program to evaluate your current health status")

sex = input("Sex(Male/Female):").lower()
while sex != 'male' and sex != 'female':
    print("Calorific data is currently only available for male or female. Please type in one of the two.")
    sex = input("Sex(Male/Female):").lower()

age = input("Age (in numerical years):")
ageValid = False

while not ageValid:
    numericValid = True
    if not age.isnumeric():
        #Check if the number is a decimal value (which is acceptable)
        try:
            float(age)
        except:
            numericValid=False
            print("Please enter your age in numerals.")
            age = (input("Age (in numerical years):"))

    if numericValid and (not (5 <= float(age) <= 100)):
        ageValid=False
        print("Please enter a value between 5 and 100. This program does not work for individuals outside of this age range.")
        age = (input("Age (in numerical years):"))
    elif numericValid:
        ageValid = True

age = float(age)

height = input("Height (in meters):")
heightValid = False

while not heightValid:
    numericValid = True
    if not height.isnumeric():
         #Check if the number is a decimal value (which is acceptable)
         try:
             float(height)
         except:
             numericValid = False
             print("Please enter your height in numerals.")
             height = input("Height (in meters):")

    if numericValid and (not (0.5 <= float(height) <= 2.5)):
         heightValid = False
         print("Please enter a value between 0.5 and 2.5.")
         height = (input("Height (in meters):"))
    elif numericValid:
        heightValid = True

height = float(height)

weight = input("Weight (in Kilograms):")
weightValid = False

while not weightValid:
     numericValid = True
     if not weight.isnumeric():
         # Check if the number is a decimal value (which is acceptable)
         try:
             float(weight)
         except:
             numericValid = False
             print("Please enter your weight in numerals.")
             weight = (input("weight (in Kilograms):"))

     if numericValid and (not (5<=float(weight)<=200)):
         weightValid = False
         print("Please enter a value between 5 and 200.")
         weight = (input("Weight (in Kilograms):"))
     elif numericValid:
         weightValid = True

weight = float(weight)

individualMain = personalCalorieInfo()
individualMain.calculateBMR(age,weight,height,sex)
individualMain.BMIcalculator(weight,height)
individualMain.assessBMI()