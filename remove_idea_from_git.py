import os
import subprocess

# Define the root directory containing all the projects
root_dir = r"D:\Programacion\Curso Maestro de Python"

# Define the function to run git commands
def run_git_command(command, cwd):
    result = subprocess.run(command, cwd=cwd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command '{command}' in {cwd}: {result.stderr}")
    else:
        print(f"Success running '{command}' in {cwd}: {result.stdout}")

# Check if the root directory is a Git repository
if not os.path.isdir(os.path.join(root_dir, '.git')):
    print(f"No .git directory found in {root_dir}. Please ensure this is a Git repository.")
else:
    # Traverse only the first-level subdirectories in the root directory
    for project_dir in os.listdir(root_dir):
        full_project_path = os.path.join(root_dir, project_dir)
        if os.path.isdir(full_project_path):
            idea_dir = os.path.join(full_project_path, '.idea')
            if os.path.isdir(idea_dir):
                print(f"Processing .idea directory in {full_project_path}")
                # Change to the project directory
                os.chdir(full_project_path)
                # Remove the .idea directory from Git index
                run_git_command("git rm -r --cached .idea", full_project_path)
                # Commit the changes
                run_git_command('git commit -m "Remove .idea directories from Git index"', full_project_path)
                # Push the changes to GitHub
                run_git_command("git push origin main", full_project_path)
                # Change back to the root directory
                os.chdir(root_dir)
            else:
                print(f"No .idea directory found in {full_project_path}")

print("All .idea directories have been processed.")
# Script creado por Emanuel Coletti v4
