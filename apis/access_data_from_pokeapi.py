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
user_height = int(pokemon_data['height'])
user_weight = int(pokemon_data['weight'])

user_height_formatted = user_height / 10
user_weight_formatted = user_weight / 10
hp_formatted = int(pokemon_data['stats'][0]['base_stat'])
user_attack = int(pokemon_data['stats'][1]['base_stat'])
user_defense = int(pokemon_data['stats'][2]['base_stat'])

print('')
# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(user_weight_formatted) + "(kgs)")
print('Height: {}'.format(user_height_formatted) + "(m)")
# print('Ability: {}'.format(ability['name']))
print('Health Points: {}'.format(hp_formatted))
print('Attack: {}'.format(user_attack))
print('Defense: {}'.format(user_defense))

# Computer's random choice 1 - 1025
pokemon_id = random.randint(1, 1025)

computer_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
computer_response = requests.get(computer_url)
computer_pokemon_data = json.loads(computer_response.text)
computer_hp_formatted = int(computer_pokemon_data['stats'][0]['base_stat'])
computer_attack = int(computer_pokemon_data['stats'][1]['base_stat'])
computer_defense = int(computer_pokemon_data['stats'][2]['base_stat'])
computer_height = int(computer_pokemon_data['height'])
computer_weight = int(computer_pokemon_data['weight'])

computer_height_formatted = computer_height / 10
computer_weight_formatted = computer_weight / 10

hp = [hp_formatted, computer_hp_formatted]
attack = [user_attack, computer_attack]
defense = [user_defense, computer_defense]
height = [user_height_formatted, computer_height_formatted]
weight = [user_weight_formatted, computer_weight_formatted]

print('')
print('What stat do you pick?')
stat_choice = str(input().lower())
print('')

while stat_choice == 'attack':
    if attack[0] > attack[1]:
        print('You Win')
        break
    elif stat_choice == 'attack' and attack[0] < attack[1]:
        print('You Lose')
        break
    else:
        print("It's a tie")
        break

while stat_choice == 'defense':
    if defense[0] > defense[1]:
        print('You Win')
        break
    elif stat_choice == 'defense' and defense[0] < defense[1]:
        print('You Lose')
        break
    else:
        print("It's a tie")
        break

while stat_choice == 'hp':
    if hp[0] > hp[1]:
        print('You Win')
        break
    elif stat_choice == 'hp' and hp[0] < hp[1]:
        print('You Lose')
        break
    else:
        print("It's a tie")
        break

while stat_choice == 'weight':
    if weight[0] > weight[1]:
        print('You Win')
        break
    elif stat_choice == 'weight' and weight[0] < weight[1]:
        print('You Lose')
        break
    else:
        print("It's a tie")
        break

while stat_choice == 'height':
    if height[0] > height[1]:
        print('You Win')
        break
    elif stat_choice == 'height' and height[0] < height[1]:
        print('You Lose')
        break
    else:
        print("It's a tie")
        break

print('')
print('Name: {}'.format(computer_pokemon_data['name']))
print('Health Points: {}'.format(computer_hp_formatted))
print('Attack: {}'.format(computer_attack))
print('Defense: {}'.format(computer_defense))
print('Weight: {}'.format(computer_weight_formatted) + "(kgs)")
print('Height: {}'.format(computer_height_formatted) + "(m)")
print('  ')


