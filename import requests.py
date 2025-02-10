import requests

# Replace with your repository details and personal access token
owner = 'niladri-115'
repo = 'valentiles-proposal'
token = 'your_personal_access_token'

url = f"https://api.github.com/repos/{owner}/{repo}/stats/code_frequency"
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github+json'
}

response = requests.get(url, headers=headers)
data = response.json()

print(data)
