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

# Transform the CSV rows into Portainer JSON format
templates = []
for row in csv_reader:
    template = {
        "type": 1,
        "name": row["gamename"],
        "title": row["gameservername"],
        "description": " Dockerized game server by LinuxGSM ",
        "logo": f"https://github.com/GameServerManagers/LinuxGSM/blob/master/lgsm/data/gameicons/{row['shortname']}-icon.png?raw=true",
        "image": f"gameservermanagers/gameserver:{row['shortname']}",
        "restart_policy": "unless-stopped",
        "network_mode": "host",
        "categories": [
            "Game Server"
        ],
        "volumes": [
            {
                "container": "/data",
                "bind": row["gameservername"]
            }
        ],
        "labels": [
            {
                "name": "Owner",
                "value": "LinuxGSMM"
            }
        ],
        "maintainer": " https://github.com/miztertea/linuxgsmm/"
    }
    templates.append(template)

# Create the final Portainer JSON format
portainer_json = {
    "version": "2",
    "templates": templates
}

# Save the transformed data to a JSON file in the parent directory
output_file = os.path.join("..", "portainer.json")
with open(output_file, "w") as f:
    json.dump(portainer_json, f, indent=4)

print(f"Portainer templates JSON data has been written to {output_file}")