# CI-CD-pipeline
https://github.com/safayavatsal/simple_html_project.git

# CI/CD Pipeline with Bash, Python, and Cron Jobs

This project demonstrates a simple CI/CD pipeline setup using Bash, Python, and cron jobs on macOS with Nginx managed by Homebrew.

## Project Structure

- `index.html`: Simple HTML project.
- `check_commits.py`: Python script to check for new commits.
- `deploy.sh`: Deployment script to update the Nginx server.
- `latest_commit_sha.txt`: File to store the latest commit SHA.

## Instructions

### Task 1: Set Up a Simple HTML Project

1. Create a simple HTML file:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple HTML Project</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
    </html>
    ```

2. Initialize a Git repository and push to GitHub.

### Task 2: Set Up Local Nginx Instance on macOS using zsh Terminal

1. Install Homebrew (if not already installed).
2. Install Nginx using Homebrew with `brew install nginx`.
3. Start Nginx with `sudo brew services start nginx`.
4. Stop Nginx (if needed) with `sudo brew services stop nginx`.
5. Restart Nginx with `sudo brew services restart nginx`.

### Task 3: Write a Python Script to Check for New Commits

1. Create `check_commits.py` to check for new commits using the GitHub API.

### Task 4: Write a zsh Script to Deploy the Code

1. Create `deploy.sh` to clone the latest code and restart Nginx.

### Task 5: Set Up a Cron Job to Run the Python Script

1. Create a cron job to run `check_commits.py` every minute.

### Task 6: Test the Setup

1. Make a new commit and verify the changes are automatically deployed.

## GitHub Repository

Link: [simple_html_project](https://github.com/safayavatsal/simple_html_project.git)
