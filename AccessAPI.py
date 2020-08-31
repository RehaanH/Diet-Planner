import requests
import json

# Function which uses the search term to return results from food database API.
def foodSearchResults(foodKeyword):
    results = {}
    url = 'https://api.edamam.com/api/food-database/v2/parser?app_id=1d03b458&app_key=58af9c03362751552e052ce7b7720a61&ingr=' + foodKeyword
    response = requests.get(url)
    # The requests limit has exceeded 10 calls per min if response code is not 200.
    if response.status_code == 500:
        print("The API is having some connectivity issues. Please try again later.")
        return results
    elif not response.status_code == 200:
        print("More than 10 requests per minute have been made.Please try again in a bit.")
        return results

    resultsDict = json.loads(response.text)

    # Adding the name of the search result and the calorific value/category
    for listItem in resultsDict['hints']:
        try:
            listItem['food']['nutrients']['ENERC_KCAL']
        except:
            print("\nSomething went wrong")
            return {}
        try:
            listItem['food']['category']
        except:
            print("\nSomething went wrong")
            return {}

        results[listItem['food']['label']] = (listItem['food']['nutrients']['ENERC_KCAL'], listItem['food']['category'])
    return results

# data = {"quantity": 1,
#       "measureURI": "http://www.edamam.com/ontologies/edamam.owl#Measure_unit",
#        "foodId": "food_bnbh4ycaqj9as0a9z7h9xb2wmgat"}
# data_json = json.dumps(data)
# headers = {'Content-type': 'application/json'}
# response = requests.post('https://api.edamam.com/api/food-database/v2/nutrients?app_id=1d03b458&app_key=58af9c03362751552e052ce7b7720a61', data=data_json, headers=headers)
# print(response)