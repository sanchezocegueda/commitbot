# Parameters
FILE_NAME = "logs.md"
MIN_COMMITS = 1
MAX_COMMITS = 10

# Git setup
GITHUB_NAME = "commitbot" # (Optional) replace with your name
GITHUB_EMAIL = "96963333+sanchezocegueda@users.noreply.github.com" # (Required) replace with your email

# Commands
GIT_CONFIG_NAME = ["git", "config", "--global", "user.name"]
GIT_CONFIG_EMAIL = ["git", "config", "--global", "user.email"]
GIT_ADD = ["git", "add"]
GIT_COMMIT = ["git", "commit", "-m"]
GIT_PUSH = ["git", "push"]
ECHO = ["echo"]