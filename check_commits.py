import requests
import json
import os

GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "safayavatsal"
REPO_NAME = "simple_html_project"
ACCESS_TOKEN = "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"
PROJECT_DIR = "simple-html-project"

def get_latest_commit_sha():
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/commits"
    headers = {
        "Authorization": f"token {ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    commits = response.json()
    latest_commit_sha = commits[0]['sha']
    return latest_commit_sha

def main():
    sha_file = os.path.join(PROJECT_DIR, 'latest_commit_sha.txt')
    if os.path.exists(sha_file):
        with open(sha_file, 'r') as file:
            last_known_sha = file.read().strip()
    else:
        last_known_sha = ''

    latest_commit_sha = get_latest_commit_sha()
    if last_known_sha != latest_commit_sha:
        with open(sha_file, 'w') as file:
            file.write(latest_commit_sha)
        os.system(f'zsh {os.path.join(PROJECT_DIR, "deploy.sh")}')
    else:
    print("No new commits.")

if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR):
        os.makedirs(PROJECT_DIR)
    main()
