import json

def write_json(data: list = [], name: str = "json_data.json"):
    with open(name, "w", encoding="utf-8") as f:

        json_data = json.dumps(data, indent=2)
        f.write(json_data)