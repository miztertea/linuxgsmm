
# LinuxGSM to Portainer Application Templates

This project processes the `serverlist.csv` file from [LinuxGSM](https://github.com/GameServerManagers/LinuxGSM) and transforms it into a JSON format that is compatible with [Portainer](https://www.portainer.io/). The generated JSON file provides default options for each game server, making it easy to deploy game servers directly from the Portainer App Templates interface.

## Aim of the Project

The primary goal of this project is to simplify the deployment of Dockerized game servers by:
- Ingesting the `serverlist.csv` provided by LinuxGSM.
- Formatting the data into a JSON template that Portainer can read.
- Providing default configurations for each game server to streamline deployment.

This enables users to quickly deploy game servers using the Portainer App Templates UI.

## Usage Instructions

### Adding Templates to Portainer

#### Option 1: Via Portainer Web UI
1. Log into your Portainer web interface.
2. Navigate to **Settings → App Templates**.
3. Update the template URL to point to our `portainer.json` file:
   ```
   https://raw.githubusercontent.com/miztertea/linuxgsmm/refs/heads/main/portainer.json
   ```
4. Go to **Home → App Templates**. You should see all available game servers.
5. Click a template to deploy the corresponding game server.


### Generating your own JSON File
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Run the script to generate the JSON file for Portainer:
   ```bash
   python generate_portainer.py
   ```

3. The generated file, `portainer.json`, will be saved in the parent directory of the script.

## Contributions
Contributions are welcome! If you have ideas for improving this project or encounter issues, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Happy gaming!
