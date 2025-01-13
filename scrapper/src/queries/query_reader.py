import json

def read_queries(file_path):
    try:
        with open(file_path, 'r') as file:
            queries = json.load(file)
            if not isinstance(queries, list):
                raise ValueError("Input file must contain a list of queries.")
            return queries
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error reading queries file: {e}")