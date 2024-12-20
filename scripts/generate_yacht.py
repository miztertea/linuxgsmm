import csv
import requests
import json
import os

# Define the URL of the CSV file
csv_url = "https://raw.githubusercontent.com/GameServerManagers/LinuxGSM/refs/heads/master/lgsm/data/serverlist.csv"

# Fetch and process the CSV file
response = requests.get(csv_url)
response.raise_for_status()  # Ensure the request was successful

# Parse the CSV content
csv_reader = csv.DictReader(response.text.splitlines())

# Transform the CSV rows into JSON format
json_data = []
for row in csv_reader:
    json_element = {
        "type": 1,
        "title": row["gamename"],
        "name": row["gameservername"],
        "description": " Dockerized game server by LinuxGSM ",
        "logo": f"https://github.com/GameServerManagers/LinuxGSM/blob/master/lgsm/data/gameicons/{row['shortname']}-icon.png?raw=true",
        "image": f"gameservermanagers/gameserver:{row['shortname']}",
        "note": f"Server config files located <a href='https://github.com/GameServerManagers/Game-Server-Configs/tree/main/{row['shortname']}' target='_blank' rel='noopener noreferrer' />here</a>.",
        "categories": ["Game Server"],
        "platform": "linux",
        "restart_policy": "unless-stopped",
        "network_mode": "host",
        "volumes": [
            {
                "container": "/data",
                "bind": row["gameservername"]
            }
        ]
    }
    json_data.append(json_element)

# Save the transformed data to a JSON file in the parent directory
output_file = os.path.join("..", "yacht.json")
with open(output_file, "w") as f:
    json.dump(json_data, f, indent=4)

print(f"JSON data has been written to {output_file}")
