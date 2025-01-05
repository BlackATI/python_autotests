#Импротируем модули requests и pytest
import requests
import pytest

#Общие переменные
URL = 'https://api.pokemonbattle.ru/v2'
TRAINER_ID = '13197'

#Тест на проверку статус кода 200
def test_status_code():
    response = requests.get(url = f'{URL}/pokemons')
    assert response.status_code == 200

#Тест на проверку trainer_id
def test_trainer_id():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.json()['data'][0]['trainer_id'] == TRAINER_ID