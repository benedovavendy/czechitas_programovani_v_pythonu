import requests
import json

# první část úkolu
number_of_facts = int(input('Zadej počet faktů, který chceš zobrazit: '))

response = requests.get(f'https://cat-fact.herokuapp.com/facts/random?amount={number_of_facts}', timeout=5)
data = response.json()

texty_faktu = []
cislo_faktu = 0
for fakt in data:
    cislo_faktu += 1
    texty_faktu.append(f'{cislo_faktu}. {fakt['text']}')

with open('czechitas_programovani_v_pythonu/ukoly/kocici_fakta.json', mode = 'w', encoding='utf-8') as output_file:
    json.dump(texty_faktu, output_file, indent=4)

# druhá část úkolu
try:
    response = requests.get(f'https://cat-fact.herokuapp.com/facts/random?amount={number_of_facts +20}', timeout=0.001)
    data = response.json()
except requests.exceptions.Timeout:
    print(f'Jste příliš nedočkaví!')