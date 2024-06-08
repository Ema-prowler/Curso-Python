import os

# Define the root directory containing all the projects
root_dir = r"D:\Programacion\Curso Maestro de Python"

# Define the desired content for the .gitignore files in .venv
venv_gitignore_content = """*
!.gitignore
!Scripts/
!Scripts/main.py
!Scripts/texto.txt
"""

# Define the content to ignore .idea directories
idea_gitignore_content = ".idea/\n"

# Traverse all subdirectories in the root directory
for subdir, dirs, files in os.walk(root_dir):
    # Check if the current directory is a .venv directory
    if os.path.basename(subdir) == ".venv":
        gitignore_path = os.path.join(subdir, ".gitignore")
        if os.path.isfile(gitignore_path):
            # Write the desired content to the .gitignore file in .venv
            with open(gitignore_path, 'w') as file:
                file.write(venv_gitignore_content)
            print(f"Updated: {gitignore_path}")
    
    # Check if we are in a project root directory
    if os.path.basename(subdir) != ".venv" and '.idea' in dirs:
        gitignore_path = os.path.join(subdir, ".gitignore")
        if os.path.isfile(gitignore_path):
            # Read the current content of the .gitignore file
            with open(gitignore_path, 'r') as file:
                gitignore_content = file.read()
            
            # Check if the .idea ignore rule is already present
            if idea_gitignore_content.strip() not in gitignore_content:
                # Append the content to ignore .idea directories to the .gitignore file
                with open(gitignore_path, 'a') as file:
                    file.write(idea_gitignore_content)
                print(f"Appended .idea ignore rule to: {gitignore_path}")
            else:
                print(f".idea ignore rule already present in: {gitignore_path}")
        else:
            # Create a new .gitignore file with the content to ignore .idea directories
            with open(gitignore_path, 'w') as file:
                file.write(idea_gitignore_content)
            print(f"Created and updated: {gitignore_path}")

print("All .gitignore files have been updated.")
# Script creado por Emanuel Coletti v3
