import requests
import pytest
URL= "https://api.pokemonbattle.ru/v2"
Token="f173887b05d2d1b88b3fe78261839deb"
header= {"Content-Type" : "application/json","trainer_token":Token }
TRAINER_LEVEL=2
TRAINER_ID=37590

def test_status_code():
    response=requests.get(url=f"{URL}/trainers",params={"trainer_level":TRAINER_LEVEL})
    assert response.status_code==200

def part_of_response():
    response_get=requests.get(url=f"{URL}/trainers",params={"trainer_id":TRAINER_ID})
    assert response_get.json()["data"][0]["id"]==37590
