import requests
 
# GitHub repository details
username = "ifatha24"
repo_name = "Assignment-2"
file_name = "hello.py"
branch = "main"  # Replace 'main' with your branch name if different
 
# GitHub raw content URL
url = f"https://raw.githubusercontent.com/{username}/{repo_name}/{branch}/{file_name}"
 
try:
    response = requests.get(url)
    if response.status_code == 200:
        print("File Content:")
        print(response.text)
    else:
        print(f"Failed to fetch file. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")