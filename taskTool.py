import requests
import json

# Replace these with your own values
owner = 'your_github_username'
repo = 'your_repository_name'
token = 'your_github_personal_access_token'

# Define the new task data
new_task = {
    'title': 'New Task Title',
    'body': 'This is the description of the new task.',
    'labels': ['bug', 'enhancement']  # Optional: Add labels to the task
}

# Create the new task
url = f'https://api.github.com/repos/{owner}/{repo}/issues'
headers = {'Authorization': f'token {token}'}
response = requests.post(url, headers=headers, data=json.dumps(new_task))

# Check if the task was created successfully
if response.status_code == 201:
    print('Task created successfully!')
    print(response.json())
else:
    print('Failed to create task:')
    print(response.json())
