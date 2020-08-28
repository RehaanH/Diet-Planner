import math
import requests
import json

#This class will contain information required to evaluate an individuals suitable calorific intake
class personalCalorieInfo:
    def _init_(self,basalMetabolicRate,exerciseCalories,recommendedIntake,BMI,weightLevel,recommendedWeightChange):
        self.__basalMetabolicRate=basalMetabolicRate
        self.__exerciseCalories=exerciseCalories
        self.__recommendedIntake=recommendedIntake
        self.__BMI=BMI
        self.__weightLevel=weightLevel
        self.__recommendedWeightChange=recommendedWeightChange

    #This method will be used to evaluate an individuals resting metabolism.
    #The weight has to be in kg while height should be in m
    def calculateBMR(self,age,weight,height,gender):
        if gender == 'female':
            self.__basalMetabolicRate =int( 655.1+(9.563*weight)+(1.85*height)-(4.676*age))
        else:
            self.__basalMetabolicRate =int(66.47+(13.75*weight)+(5.003*100*height)-(6.755*age))
        print("You currently burn around ", self.__basalMetabolicRate ," kiloCalories daily without any exercise.\n")

    #Gets the basal Metabolic Rate
    def getBMR(self):
        return self.__basalMetabolicRate

    #Calculates the BMI of an individual and recommended weight change
    def BMIcalculator(self,weight,height):
        self.__BMI = int(weight/pow(height,2))
        #calculating the recommended weight change
        if self.__BMI < 18:
            self.__recommendedWeightChange = int(18*pow(height,2)-weight)
        elif self.__BMI > 24:
            self.__recommendedWeightChange = int(weight-24*pow(height,2))


    #Assesses an individuals BMI
    def assessBMI(self):
        currentBMI = self.__BMI
        if currentBMI <= 15:
            self.__weightLevel = "ST"
            print("You are severely underweight. It is strongly recommended that you increase your daily calorie intake.\n")
            print("While specific values may vary by the individual, it is recommended that you gain about ", self.__recommendedWeightChange, " Kilograms")

        elif currentBMI <= 16:
            self.__weightLevel = "MT"
            print("You are moderately underweight. It is recommended that you increase your daily calorie intake.\n")
            print("While specific values may vary by the individual, it is recommended that you gain about ", self.__recommendedWeightChange, " Kilograms")
        elif currentBMI <= 18:
            self.__weightLevel = "MiT"
            print("You are slightly underweight. You should consider increasing your daily calorie intake. \n ")
            print("While specific values may vary by the individual, it is recommended that you gain about ",  self.__recommendedWeightChange, " Kilograms")
        elif currentBMI <=  24:
            self.__weightLevel = "NORM"
            print("You are in a healthy body mass range! It is recommended that you balance your daily calorie intake.\n")
        elif currentBMI <= 29:
            self.__weightLevel = "PO"
            print("You are slightly overweight. You should consider decreasing your daily calorie intake. \n")
            print("While specific values may vary by the individual, it is recommended that you lose about ",
                  self.__recommendedWeightChange , " Kilograms")
        elif currentBMI <= 34:
            self.__weightLevel = "OI"
            print("You are overweight and at risk of becoming moderately obese. It is recommended that you lower your daily calorie intake. \n")
            print("While specific values may vary by the individual, it is recommended that you lose about ",
                  self.__recommendedWeightChange, " Kilograms")
        elif currentBMI <= 39:
            self.__weightLevel = "OII"
            print("Your weight indicates that you are obese. It is strongly recommended that you lower your daily calorie intake. \n")
            print("While specific values may vary by the individual, it is recommended that you lose about ",
                  self.__recommendedWeightChange, " Kilograms")
        else:
            self.__weightLevel = "OIII"
            print("Your weight indicates that you are severly obese. It is strongly recommended that you lower your daily calorie intake . \n")
            print("You are at significant risk of obesity related deceases. \n")
            print("While specific values may vary by the individual, it is recommended that you lose about ",
                  self.__recommendedWeightChange, " Kilograms")


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

individualMain= personalCalorieInfo()
individualMain.calculateBMR(age,weight,height,sex)
individualMain.BMIcalculator(weight,height)
individualMain.assessBMI()