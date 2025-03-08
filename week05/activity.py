import requests
import json
#from config import config as cfg  # Import API key from config file

# Output filename
filename = "activity.json"

# GitHub API URL for user repositories
url = "https://api.github.com/repos/TomUszyn/computer-infrastructure/activity"

# Get API key from config file
#apikey = cfg["githubkey"]

# Headers for authentication
#headers = {
#    "Authorization": f"token {apikey}",
#    "Accept": "application/vnd.github.v3+json",
#    "User-Agent": "my-github-script"
#}

# Send GET request to GitHub API
response = requests.get(url)

# Print response status code
print(response.status_code)

# Write response to JSON file
with open(filename, "w") as fp:
   repoJSON = response.json()
   json.dump(repoJSON, fp, indent=4)