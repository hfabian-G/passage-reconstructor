import json
from pathlib import Path
from datetime import datetime

def log(file_path: str, json_message: json):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.touch() 
    json_message['timestamp'] = datetime.now().isoformat()
    try:
        with open(file_path,'r') as file:
            data_list = json.load(file) 
    except (json.JSONDecodeError):
        data_list = []

    data_list.append(json_message)

    with open(file_path, 'w') as file:
        json.dump(data_list, file, indent = 2)