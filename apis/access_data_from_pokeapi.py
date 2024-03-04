import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

# Ask the user to choose a pokemon
print('Enter your pokemon:')
# for pokemon in pokemon_list:
# print(pokemon['name'])

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
# abilities = pokemon_data['abilities'][0]
# ability = abilities['ability']

# to format height and weight properly
# height = int(pokemon_data['height'])
# weight = int(pokemon_data['weight'])
#
# height_formatted = height / 10
# weight_formatted = weight / 10
hp_formatted = int(pokemon_data['stats'][0]['base_stat'])
attack = int(pokemon_data['stats'][1]['base_stat'])
defense = int(pokemon_data['stats'][2]['base_stat'])

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
# print('Weight: {}'.format(weight_formatted) + "(kgs)")
# print('Height: {}'.format(height_formatted) + "(m)")
# print('Ability: {}'.format(ability['name']))
print('Health Points: {}'.format(hp_formatted))
print('Attack: {}'.format(attack))
print('Defense: {}'.format(defense))

# Computer's random choice 1 - 1025
pokemon_id = random.randint(1, 1025)

computer_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
computer_response = requests.get(computer_url)
computer_pokemon_data = json.loads(computer_response.text)
computer_hp_formatted = int(computer_pokemon_data['stats'][0]['base_stat'])
computer_attack = int(computer_pokemon_data['stats'][1]['base_stat'])
computer_defense = int(computer_pokemon_data['stats'][2]['base_stat'])

print('')
print('Name: {}'.format(computer_pokemon_data['name']))
print('Health Points: {}'.format(computer_hp_formatted))
print('Attack: {}'.format(computer_attack))
print('Defense: {}'.format(computer_defense))
print('  ')

if computer_attack > hp_formatted:
    print('You lose')
elif computer_attack < hp_formatted and attack > computer_hp_formatted:
    print('You win')
else:
    print("It's a tie")
