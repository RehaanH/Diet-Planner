from CalorificInformation import personalCalorieInfo
from ActivityAnalysis import gymActivities
from ActivityAnalysis import trainingAndSport
from ActivityAnalysis import outdoorActivities
from ActivityAnalysis import homeAndDailyActivities
from ActivityAnalysis import homeRepairActivities
from ActivityAnalysis import occupationalActivities
from ActivityAnalysis import printWorkout
from KeywordSearch import trieRoot
from KeywordSearch import traverseTrie
from KeywordSearch import findWords
from AccessAPI import foodSearchResults

# This is the main file that will run the program

# Getting information from the user and error checking
print("Please fill out the following details for the program to evaluate your current health status")

sex = input("Sex(Male/Female):").lower().strip()
while sex != 'male' and sex != 'female':
    print("Calorific data is currently only available for male or female. Please type in one of the two.")
    sex = input("Sex(Male/Female):").lower().strip()

age = input("Age (in numerical years):")
ageValid = False

while not ageValid:
    numericValid = True
    if not age.isnumeric():
        # Check if the number is a decimal value (which is acceptable)
        try:
            float(age)
        except:
            numericValid=False
            print("Please enter your age in numerals.")
            age = (input("Age (in numerical years):"))

    if numericValid and (not (5 <= float(age) <= 100)):
        ageValid=False
        print("Please enter a value between 5 and 100. "
              "This program does not work for individuals outside of this age range.")
        age = (input("Age (in numerical years):"))
    elif numericValid:
        ageValid = True

age = float(age)

height = input("Height (in meters):")
heightValid = False

while not heightValid:
    numericValid = True
    if not height.isnumeric():
         # Check if the number is a decimal value (which is acceptable)
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

# Accounting for the fact that body mass will affect calorie burn rates
burnModifier = 0
if weight < 65:
    burnModifier = 1
elif weight < 80:
    burnModifier = 1.25
else:
    burnModifier = 1.2

print("\nNow lets start planning your diet and activity levels for the next day.")

status = "menu"
searchTerm = " "
chosenActivities = {}
sumTime = 0

while not status == "done":
    if status == "menu":
        print("\nPlease type in the physical activity you would like to add for the following day.")
        print("Activities from the following categories are available:")
        print("1.Gym Activities (Weight lifting, Aerobics ...)")
        print("2.Training and Sports (Running, Swimming, Archery...)")
        print("3.Outdoor Activities (Gardening, Shoveling Snow...)")
        print("4.Home and Daily Activities (Sleeping, Cooking, Reading...)")
        print("5.Home Repair Activities (Roofing, Paint...)")
        print("6.Occupational Activities (Computer work, Sitting in Class...)")
        print("Type in a number to see all the options listed.")
        print('Type in "Exit" to finish logging activities.')
        searchTerm = input("Search term:").lower().strip()
        status = "list all"
        try:
            float(searchTerm)
        except:
            status = "list results"
            searchTerm = searchTerm.lower().strip()

        if searchTerm == "exit":
            status = "done"

    # Listing all the activity options in this program
    if status == "list all":
        print("\nThis is the entire activities list. The calories listed are values per 30 mins engaged.")
        i = 0
        print("Gym Activities- ")
        for activity in gymActivities:
            i += 1
            print(i,". ", activity,": ", int(gymActivities[activity] * burnModifier))

        print("\nTraining and Sports- ")
        i = 0
        for activity in trainingAndSport:
            i += 1
            print(i, ". ", activity, ": ", int(trainingAndSport[activity] * burnModifier))

        print("\nOutdoor Activities-")
        i = 0
        for activity in outdoorActivities:
            i += 1
            print(i, ". ", activity,": ", int(outdoorActivities[activity] * burnModifier))

        print("\nHome and Daily Activities-")
        i = 0
        for activity in homeAndDailyActivities:
            i += 1
            print(i, ". ", activity, ": ", int(homeAndDailyActivities[activity] * burnModifier))

        print("\nHome Repair Activities-")
        i = 0
        for activity in homeRepairActivities:
            i += 1
            print(i, ". ", activity, ": ", int(homeRepairActivities[activity] * burnModifier))

        print("\nOccupational Activities-")
        i = 0
        for activity in occupationalActivities:
            i += 1
            print(i, ". ", activity, ": ", int(occupationalActivities[activity] * burnModifier))

        print("\n")
        status = "menu"

    # Listing the results of the search query. search methods are in the the KeywordSearch.py file
    if status == "list results":
        print("The following results were found from your search term.")
        print("Please type in the number of the option you want to choose", end=" ")
        print('or type "menu" to go back')

        searchNode = traverseTrie(trieRoot, searchTerm)
        indices = []
        findWords(searchNode, indices)
        indexCache = {}
        i=0

        for index in indices:
            if index < 100:
                i += 1
                print("\nGym Activities- ")
                print(i, ". ", list(gymActivities)[index], ": ",
                      int(gymActivities[list(gymActivities)[index]] * burnModifier))
                indexCache[i] = index
                indices.remove(index)

            elif index < 200:
                i += 1
                print("\nTraining And Sport- ")
                print(i, ". ", list(trainingAndSport)[index-100], ": ",
                      int(trainingAndSport[list(trainingAndSport)[index-100]] * burnModifier))
                indexCache[i] = index
                indices.remove(index)

            elif index < 300:
                i += 1
                print("\nOutdoor Activities- ")
                print(i, ". ", list(outdoorActivities)[index-200], ": ",
                      int(outdoorActivities[list(outdoorActivities)[index-200]] * burnModifier))
                indexCache[i] = index
                indices.remove(index)

            elif index < 400:
                i += 1
                print("\nHome And Daily Activities- ")
                print(i, ". ", list(homeAndDailyActivities)[index-300], ": ",
                      int(homeAndDailyActivities[list(homeAndDailyActivities)[index-300]] * burnModifier))
                indexCache[i] = index
                indices.remove(index)


            elif index < 500:
                i += 1
                print("\nHome Repair Activities- ")
                print(i, ". ", list(homeRepairActivities)[index-400], ": ",
                      int(homeRepairActivities[list(homeRepairActivities)[index-400]] * burnModifier))
                indexCache[i] = index
                indices.remove(index)

            else:
                i += 1
                print("\nOccupational Activities- ")
                print(i, ". ", list(occupationalActivities)[index - 500], ": ",
                      int(occupationalActivities[list(occupationalActivities)[index - 500]] * burnModifier))
                indexCache[i] = index
                indices.remove(index)

        choice = input("\nPlease numerically enter & confirm the number of your selection:")

        inputValid = False
        while not inputValid:
            numeral = True
            try:
                float(choice)
            except:
                if choice.lower().strip() =="menu":
                    status = "menu"
                    inputValid = True
                else:
                    print('Type "menu" to go back or type in a numerical value')
                    numeral = False
                    choice = input("Please numerically enter & confirm the number of your selection:")

            # Saving the users choice if it was within the original number of options
            if not inputValid and numeral:
                choice = int(choice)
                if choice in indexCache.keys():
                    inputValid = True
                    # Asking the user for the duration of the activity that they engage in
                    durationValid = False
                    while not durationValid:
                        durationValid = True
                        duration = input("Please enter the time duration engaged in the activity (minutes):")
                        try:
                            float(duration)
                        except:
                            print("\nPlease enter the number of minutes numerically")
                            durationValid = False

                        if durationValid:
                            duration = float(duration)
                            if (duration + sumTime) > (24*60):
                                durationValid = False
                                print("\nYour total time duration is exceeding the number of minutes in a day!")

                            elif duration > 0 and duration < 1200:
                                durationValid = True
                                status = "menu"
                                sumTime += duration
                                chosenActivities[indexCache[choice]] = duration

                            else:
                                durationValid = False
                                print("\nPlease enter a valid value for the time duration")

                else:
                    print('\nType in a number within the range of options or type "menu"')
                    choice = input("Please numerically enter & confirm the number of your selection:")


# Printing the final activity details for the day
print("\nHere is a summary of your activities for the day: ")
print("Note- The calories burned are approximations based on your body mass and type of activity")
activityCalories = 0
activityCalories = printWorkout(chosenActivities, activityCalories)

overallCalorieBurn = int(activityCalories + individualMain.getBMR())
print("\nApproximate overall calorie burnout for the day:", overallCalorieBurn)

# Calculating the recommended daily calorie intake
recommendedIntake = 0
weightRange = individualMain.getWL()

if weightRange == "PO" or weightRange == "OI" or weightRange == "OII" or weightRange == "OIII":
    recommendedIntake = overallCalorieBurn - 750
    print("If you wish to lose weight, your recommended daily calorie intake is:", recommendedIntake)
elif weightRange == "NORM":
    recommendedIntake = overallCalorieBurn
    print("To maintain your weight, your recommended daily calorie intake is:", recommendedIntake)
else:
    recommendedIntake = overallCalorieBurn + 750
    print("If you wish to gain weight, your recommended daily calorie intake is:", recommendedIntake)


# Letting the user choose their meals for the next day
print("\nNow let's choose your diet for the next day.")
inputStatus = "search"
foodResults = {}
foodChosen = {}
currMealCalories = 0
while not inputStatus == "done":
    # The stage where the user types in the search term
    if inputStatus == "search":
        #Printing out the current meal plan details.
        if not len(foodChosen) == 0:
            print("\nThe current food items you have chosen are:")
            currMealCalories = 0
            for item in foodChosen:
                currMealCalories += foodChosen[item][0]
                print(item, ", calories:", foodChosen[item][0], ", amount:", foodChosen[item][1], "grams ,category:",
                      foodChosen[item][2])
            if currMealCalories > recommendedIntake:
                print("You will be consuming ", currMealCalories - recommendedIntake,
                      " calories more than your recommended daily intake.")
            else:
                print("You will be consuming ", recommendedIntake - currMealCalories,
                      " calories less than your recommended daily intake.")
            print('\nType in "Exit" to finish the program, or')

        searchTerm = input("\nPlease enter a type of food that you would like to consume the next day:").strip().lower()
        if searchTerm == "exit":
            inputStatus = "done"
        else:
            foodResults = foodSearchResults(searchTerm)
            if len(foodResults) == 0:
                print("No results were found for your search. Please try again.")
            else:
                inputStatus = "choose result"

    #The stage where the user chooses from the search results
    if inputStatus == "choose result":
        print("\nPick one of the results from your search term by entering the number numerically.")
        print('Type "back" to go back to your search')
        i = 0
        for food in foodResults:
            i+=1
            print(i, ".", food, ", Category:", foodResults[food][1], ", Calories per 100g:", int(foodResults[food][0]))
        choice = input("Enter the number of your choice:").strip().lower()

        exitChoose = False
        try:
            float(choice)
        except:
            exitChoose = True
            if choice == "back":
                inputStatus = "search"
            else:
                print("Please enter a valid search term")

        if not exitChoose:
            choice = int(choice)
            if choice > 0 and choice <= len(foodResults):
                massValid = False
                while not massValid:
                    massValid = True
                    foodMass = input("How many grams of this item will you consume for your serving?")
                    try:
                        float(foodMass)
                    except:
                        print("Please enter a numerical value.")
                        massValid = False
                    # If all inputs have been valid
                    if massValid and float(foodMass) > 0:
                        massValid = True
                        caloriesFromItem = int(int(foodResults[list(foodResults)[choice-1]][0]) * (float(foodMass)/100))
                        print("You will be consuming ", caloriesFromItem, "calories from this item.")

                        #Warning the user if choosing this item will take their calorie intake above the rec. limit
                        proceed = True
                        if caloriesFromItem + currMealCalories > recommendedIntake:
                            proceedValid = False
                            print("Consuming this item will take you ",
                                  caloriesFromItem + currMealCalories - recommendedIntake,
                                  " above your recommended daily calorie intake.")
                            print('Are you sure you wish to proceed? Type "yes" to confirm, "no" to go back to search.')

                            while not proceedValid:
                                confirmation = input("Confirm:").lower().strip()
                                if confirmation == "no":
                                    proceed = False
                                    inputStatus = "search"
                                    proceedValid = True
                                elif confirmation == "yes":
                                    proceedValid = True
                                else:
                                    print("\nPlease enter either yes or no")

                        if proceed:
                            chosenItem = list(foodResults)[choice-1]
                            # list: calories, mass, category
                            foodChosen[chosenItem] = [caloriesFromItem, foodMass, foodResults[chosenItem][1]]
                            inputStatus = "search"

                    else:
                        print("\nPlease enter a valid number.")
            else:
                print("\nPlease enter a number within the range of choices.")


print("\nHere is a summary of your details for the day:")
print("\nActivity details:")
printWorkout(chosenActivities, 0)

print("\nFood consumption for the day:")
for item in foodChosen:
    print(item, ", calories: ", foodChosen[item][0], ", amount: ", foodChosen[item][1], "grams ,category: ",
          foodChosen[item][2])

print("\nYour approximate overall calorie consumption for the planned day is ", overallCalorieBurn, "calories.")
print("Your recommended daily calorie intake is ", recommendedIntake, "calories.")
print("Your calorie intake for the planned day is ", currMealCalories, "calories.")

