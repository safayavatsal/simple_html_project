#deploy.sh

#!/bin/zsh

PROJECT_DIR="simple-html-project"
REPO_URL="https://github.com/safayavatsal/simple_html_project.git"

cd $PROJECT_DIR
if [ -d "$PROJECT_DIR" ]; then
    cd $PROJECT_DIR
    git pull origin main
else
    git clone $REPO_URL
fi

sudo nginx -s reload
