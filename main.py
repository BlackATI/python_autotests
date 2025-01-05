#Импортируем модуль requests
import requests

#Общие переменные
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '668b13bbf501490a9483a235b2e29432'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

#############################################################################################################
#Боди на создание покемона
body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}
#Запрос на создание покемона
response_create_pokemon=requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon)
#Ответ
print (response_create_pokemon.text)
#Получаем id созданного покемона
pokemon_id = response_create_pokemon.json()['id']

#############################################################################################################
#Боди на изменение имени покемона
body_change_name = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}
#Запрос на изменение имени покемона
response_change_name=requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_change_name)
#Ответ
print (response_change_name.text)

#############################################################################################################
#Боди для "Поймать покемона в покебол"
body_add_pokeball = {
    "pokemon_id": pokemon_id
}
#Запрос на создание покемона
response_add_pokeball=requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
#Ответ
print (response_add_pokeball.text)