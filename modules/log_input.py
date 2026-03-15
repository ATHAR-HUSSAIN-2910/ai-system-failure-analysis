import json

def load_logs(file_path):
    """
    Load logs from a JSON file and return them as Python objects.
    """

    with open(file_path, "r") as file:
        logs = json.load(file)

    return logs