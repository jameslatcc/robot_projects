import requests


def fetch_pokemon_info(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['name']
    else:
        return None

if __name__ == "__main__":
    pokemon_id = input("Enter Pokemon ID: ")
    pokemon_name = fetch_pokemon_info(pokemon_id)
    if pokemon_name:
        print(f"Pokemon Name: {pokemon_name}")
    else:
        print("Pokemon not found.")
