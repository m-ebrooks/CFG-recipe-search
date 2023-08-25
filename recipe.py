# Option [2]
# Project Brief: Search
# In this project you'll create a program to search for recipes based on an ingredient.

# Required Tasks
# These are the required tasks for this project.
# You should aim to complete these tasks before adding your own ideas to the project.
# 1. Read the Edamam API documentation ★ https://developer.edamam.com/edamam-docs-recipe-api
# 2. Ask the user to enter an ingredient that they want to search for
# 3. Create a function that makes a request to the Edamam API with the required ingredient as part of the search query
#    (also include your Application ID and Application Key)
# 4. Get the returned recipes from the API response
# 5. Display the recipes for each search result


import requests

HEALTH_LABELS = ['dairy-free', 'gluten-free', 'vegan', 'vegetarian', 'low-sugar', 'paleo', 'pescatarian']


def recipe_search(ingredient, health):
    # Register to get an APP ID and key https://developer.edamam.com/
    # Got the app_id and app_key from https://developer.edamam.com/edamam-docs-recipe-api#/
    app_id = 'bb59c101'
    app_key = 'eb6e3441a61423d433d73956269bc0d9'
    if not health:
        result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient,app_id,app_key))
        data = result.json()
        return data['hits']
    elif health:
        diet_req = input(f'Pick your requirement from the list below:\n{HEALTH_LABELS}\n')
        if diet_req in HEALTH_LABELS:
            result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}'.format(ingredient, app_id, app_key, diet_req))
            data = result.json()
            return data['hits']
        elif not diet_req:
            result = requests.get(
                'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
            data = result.json()
            return data['hits']
        else:
            return False


def ingredients(ingredientLines, file):
    # Split the ingredient list across multiple lines
    ingredient_list = ''
    for ingredient_line in ingredientLines:
        ingredient_list = ingredient_list + " \n" + ingredient_line
    # Print ingredient list
    print(ingredient_list)
    # Write ingredient list to file
    file.write(ingredient_list)


def check_dietary_requirements(user_input):
    # Checks if user has a dietary requirement.
    if user_input == 'N' or user_input == 'n':
        return False
    elif user_input == 'Y' or user_input == 'y':
        return True


class Style:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def run():
    # Ask user to enter an ingredient
    ingredient = input('Enter an ingredient: ')
    if not ingredient:
        print('Invalid input')

    else:
        check_dietary_req = input('Have you got a dietary requirement? y/n\n')
        health = check_dietary_requirements(check_dietary_req)
        # Initialise the results list in case none are returned
        results = []
        results = recipe_search(ingredient, health)
        print()

        if not results:
            # Print message in red, when no results are returned
            print(Style.RED + 'No results found for "{}"'.format(ingredient) + Style.END)

        else:
            # print(results)
            with open("recipes.txt", "w+") as file:

                for result in results:
                    recipe = result['recipe']

                    # Print the recipe label in bold
                    print(Style.BOLD + recipe['label'] + Style.END)
                    # Print the recipe URL
                    print(recipe['url'])

                    # Write recipe label to file
                    file.write("\n")
                    file.write(recipe['label'])
                    # Write recipe URL to file
                    file.write("\n")
                    file.write(recipe['url'])

                    # Print the ingredients list across multiple lines and write to file
                    ingredients(recipe['ingredientLines'], file)
                    print('\n')
                    file.write("\n")


            # Print message in green, where the file where the results have been written
            print(Style.GREEN + 'These results can also be found in "recipes.txt"' + Style.END)

run()