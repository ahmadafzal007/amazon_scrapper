import json
import os

def save_to_json(query, products):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{query}.json")

    with open(file_path, 'w') as file:
        json.dump([product.to_dict() for product in products], file, indent=4)