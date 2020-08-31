from CalorificInformation import personalCalorieInfo
from ActivityAnalysis import gymActivities
from ActivityAnalysis import trainingAndSport
from ActivityAnalysis import outdoorActivities
from ActivityAnalysis import homeAndDailyActivities
from ActivityAnalysis import homeRepairActivities
from ActivityAnalysis import occupationalActivities
from KeywordSearch import trieRoot
from KeywordSearch import traverseTrie
from KeywordSearch import findWords


#This is the main file that will run the program

#Getting information from the user and error checking
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

#Accounting for the fact that body mass will affect calorie burn rates
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
        print("Please type in the physical activity you would like to add for the following day.")
        print("Activities from the following categories are available:")
        print("1.Gym Activities (Weight lifting, Aerobics ...)")
        print("2.Training and Sports (Running, Swimming, Archery...)")
        print("3.Outdoor Activities (Gardening, Shoveling Snow...)")
        print("4.Home and Daily Activities (Sleeping, Cooking, Reading...)")
        print("5.Home Repair Activities (Roofing, Paint...)")
        print("6.Occupational Activities (Computer work, Sitting in Class...)")
        print("Type in a number to see all the options listed.")
        print('Type in "Exit" to finish logging activities.')
        searchTerm = input("Search term:")
        status = "list all"
        try:
            float(searchTerm)
        except:
            status = "list results"
            searchTerm = searchTerm.lower().strip()

        if searchTerm == "exit":
            status = "done"

    #Listing all the activity options in this program
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

    #Listing the results of the search query. search methods are in the the KeywordSearch.py file
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
                if choice.lower() =="menu":
                    status = "menu"
                    inputValid = True
                else:
                    print('Type "menu" to go back or type in a numerical value')
                    numeral = False
                    choice = input("Please numerically enter & confirm the number of your selection:")

            #Saving the users choice if it was within the original number of options
            if not inputValid and numeral:
                choice = int(choice)
                if choice in indexCache.keys():
                    inputValid = True
                    #Asking the user for the duration of the activity that they engage in
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


#Printing the final activity details for the day
print("\nHere is a summary of your activities for the day: ")
print("Note- The calories burned are approximations based on your body mass and type of activity")
activityCalories = 0
for activity in chosenActivities:
    if(activity < 100):
        print("\nGym Activities:")
        time = chosenActivities[activity]
        act = list(gymActivities)[activity]
        print(act, ", time engaged:", time, " minutes"
            ", calories burned:", gymActivities[act] * (time/30) )
        activityCalories += (gymActivities[act] * (time/30))

    elif (activity < 200):
        print("\nTraining And Sport:")
        time = chosenActivities[activity]
        act = list(trainingAndSport)[activity-100]
        print(act, ", time engaged:", time, " minutes"
            ", calories burned:", trainingAndSport[act] * (time / 30))
        activityCalories += (trainingAndSport[act] * (time / 30))

    elif (activity < 300):
        print("\nOutdoor Activities:")
        time = chosenActivities[activity]
        act = list(outdoorActivities)[activity-200]
        print(act, ", time engaged:", time, " minutes"
            ", calories burned:", outdoorActivities[act] * (time / 30))
        activityCalories += (outdoorActivities[act] * (time / 30))

    elif (activity < 400):
        print("\nHome And Daily Activities:")
        time = chosenActivities[activity]
        act = list(homeAndDailyActivities)[activity-300]
        print(act, ", time engaged:", time, " minutes"
            ", calories burned:", homeAndDailyActivities[act] * (time / 30))
        activityCalories += (homeAndDailyActivities[act] * (time / 30))

    elif (activity < 500):
        print("\nHome Repair Activities:")
        time = chosenActivities[activity]
        act = list(homeRepairActivities)[activity-400]
        print(act, ", time engaged:", time, " minutes"
            ", calories burned:", homeRepairActivities[act] * (time / 30))
        activityCalories += (homeRepairActivities[act] * (time / 30))

    elif (activity < 600):
        print("\nOccupational Activities:")
        time = chosenActivities[activity]
        act = list(occupationalActivities)[activity-500]

        print(act, ", time engaged:", time, " minutes"
            ", calories burned:", occupationalActivities[act] * (time / 30))
        activityCalories += (occupationalActivities[act] * (time / 30))

print("Approximate overall calorie burnout for the day:", int(activityCalories + individualMain.getBMR()))