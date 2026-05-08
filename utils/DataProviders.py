import json

# JSON Data Provider
def read_json_data(filepath):
    with open(filepath, 'r') as f:
        data_list = json.load(f)  # List of dicts
    return [(item,) for item in data_list]  # Wrap each dict as a tuple


