import json
import os
import uuid

def transform_json(input_json):
    output_json = {
        "authors": [
            "Bastien PAZZAGLIA, Arnaud PISTER"
        ],
        "category": "Artifial Intelligence",
        "description": "Gathering of all opensource LLMs with their scores",
        "name": "openLLM",
        "source": "open_llm_leaderboard",
        "type": "LLMs",
        "uuid": str(uuid.uuid4()),
        "values": []
    }

    for item in input_json:
        transformed_item = {
            "meta": {
                "model": item["Model"],
                "average": item["Average ⬆️"],
                "arc": item["ARC"],
                "hellaswag": item["HellaSwag"],
                "mmlu": item["MMLU"],
                "truthfulqa": item["TruthfulQA"],
                "winogrande": item["Winogrande"],
                "gsm8k": item["GSM8K"],
                "type": item["Type"],
                "architecture": item["Architecture"],
                "weight type": item["Weight type"],
                "precision": item["Precision"],
                "parameters(B)": item["#Params (B)"],
                "model sha": item["Model sha"]
            },
            "description": ", ".join(item["Tags"]),
            "value": item["Model"],
            "uuid": str(uuid.uuid4())  
        }
        output_json["values"].append(transformed_item)

    return output_json

# Load the base JSON (the one with tags)
with open('updated_models.json', 'r') as file:
    original_json = json.load(file)

# Transformed JSON
transformed_json = transform_json(original_json)

# Create a new folder named "clusters" if it does not exist
output_directory = "clusters"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Write the tranformed JSON into a new file in the folder "clusters"
output_file_path = os.path.join(output_directory, 'openLLMsCluster.json')
with open(output_file_path, 'w') as file:
    json.dump(transformed_json, file, indent=4)