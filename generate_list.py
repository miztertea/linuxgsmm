import csv
import requests
import json

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
        "description": "Lorem Ipsum.",
        "logo": f"https://github.com/GameServerManagers/LinuxGSM/blob/master/lgsm/data/gameicons/{row['shortname']}-icon.png?raw=true",
        "image": f"gameservermanagers/gameserver:{row['shortname']}",
        "note": (
            "Yacht App Templates by <a href='https://github.com/SelfhostedPro' target='_blank'>SelfhostedPro</a> based on data provided by <a href='https://www.linuxserver.io' target='_blank'>LinuxServer.io</a>.</p>"
        ),
        "categories": "Game Server",
        "platform": "linux",
        "restart_policy": "unless-stopped",
        "network_mode": "host",
        "volumes": [
            {
                "container": "/data",
                "bind": row["gameservername"]
            }
        ],
        "env": [
            {
                "name": "TZ",
                "label": "TZ",
                "default": "!TZ",
                "description": "Specify a timezone to use for example Europe/Amsterdam"
            }
        ]
    }
    json_data.append(json_element)

# Save the transformed data to a JSON file
output_file = "serverlist.json"
with open(output_file, "w") as f:
    json.dump(json_data, f, indent=4)

print(f"JSON data has been written to {output_file}")
