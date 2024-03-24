import json
import requests
from bs4 import BeautifulSoup

def fetch_model_tags(model_url):
    try:
        response = requests.get(model_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            tags_container = soup.find("div", class_="mb-3 flex flex-wrap md:mb-4")
            if tags_container:
                return [tag.text.strip() for tag in tags_container.find_all("a", class_="tag")]
            else:
                return []
        elif response.status_code == 404:
            return None  # None indique que le modèle doit être supprimé
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {e}")
        return []

# Chemin vers votre fichier JSON
file_path = 'open-llm-leaderboard.json'

# Charger les données JSON à partir du fichier
with open(file_path, 'r', encoding='utf-8') as file:
    models = json.load(file)

# Mise à jour des modèles avec les tags
updated_models = []
for model in models:
    model_name = model['Model']
    model_url = f"https://huggingface.co/{model_name}"
    print(f"Récupération des tags pour le modèle : {model_name}")
    tags = fetch_model_tags(model_url)

    if tags is None:
        print(f"Modèle {model_name} non trouvé (404), il sera exclu du fichier JSON.")
    else:
        model['Tags'] = tags
        updated_models.append(model)

# Sauvegarder les modèles mis à jour dans un nouveau fichier JSON
updated_file_path = 'updated_models.json'
with open(updated_file_path, 'w', encoding='utf-8') as file:
    json.dump(updated_models, file, indent=4)

print(f"Les modèles mis à jour ont été sauvegardés dans {updated_file_path}.")