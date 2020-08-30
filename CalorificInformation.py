import math

#This class will contain information required to evaluate an individuals suitable calorific intake and BMI
class personalCalorieInfo:
    def __init__(self,):
        self.__basalMetabolicRate = 0
        self.__exerciseCalories = 0
        self.__recommendedIntake = 0
        self.__BMI = 0
        self.__weightLevel = 0
        self.__recommendedWeightChange = 0

    #This method will be used to evaluate an individuals resting metabolism.
    #The weight has to be in kg while height should be in m
    def calculateBMR(self,age,weight,height,gender):
        if gender == 'female':
            self.__basalMetabolicRate =int( 655.1+(9.563*weight)+(1.85*height)-(4.676*age))
        else:
            self.__basalMetabolicRate =int(66.47+(13.75*weight)+(5.003*100*height)-(6.755*age))
        print("\nYou currently burn around ", self.__basalMetabolicRate ," kiloCalories daily without any exercise.\n")

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

