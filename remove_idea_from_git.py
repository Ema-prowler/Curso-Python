import os
import subprocess

# Define the root directory containing all the projects
root_dir = r"D:\Programacion\Curso Maestro de Python"

# Define the function to run git commands
def run_git_command(repo_dir, command):
    result = subprocess.run(command, cwd=repo_dir, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command in {repo_dir}: {result.stderr}")
    else:
        print(f"Success: {result.stdout}")

# Traverse all subdirectories in the root directory
for subdir, dirs, files in os.walk(root_dir):
    # Check if the current directory is a Git repository
    if '.git' in dirs:
        print(f"Processing Git repository in {subdir}")
        # Remove the .idea directory from Git index
        run_git_command(subdir, "git rm -r --cached .idea")
        # Commit the changes
        run_git_command(subdir, 'git commit -m "Remove .idea directory from Git index"')
        # Push the changes to GitHub
        run_git_command(subdir, "git push origin main")

print("All .idea directories have been removed from the Git index and changes pushed to GitHub.")
# Script creado por Emanuel Coletti
