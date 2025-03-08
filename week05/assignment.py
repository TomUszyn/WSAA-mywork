import requests
import base64

# GitHub settings
GITHUB_TOKEN = "your_personal_access_token"
REPO_OWNER = "your_username"
REPO_NAME = "your_repository"
FILE_PATH = "path/to/file.txt"
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"

# Headers for authentication
headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

# Get the file
response = requests.get(API_URL, headers=headers)
data = response.json()

if response.status_code == 200:
    content = base64.b64decode(data["content"]).decode("utf-8")
    sha = data["sha"]  # Needed for updating the file

    # Modify the content (replace 'Andrew' with 'YourName')
    modified_content = content.replace("Andrew", "YourName")
    encoded_content = base64.b64encode(modified_content.encode("utf-8")).decode("utf-8")

    # Commit the change
    update_data = {
        "message": "Replaced 'Andrew' with 'YourName'",
        "content": encoded_content,
        "sha": sha,
    }
    update_response = requests.put(API_URL, headers=headers, json=update_data)
    
    if update_response.status_code == 200 or update_response.status_code == 201:
        print("File updated successfully!")
    else:
        print("Error updating file:", update_response.json())
else:
    print("Error fetching file:", data)
