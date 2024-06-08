import os

# Define the root directory containing all the projects
root_dir = r"D:\Programacion\Curso Maestro de Python"

# Define the desired content for the .gitignore files
gitignore_content = """*
!.gitignore
!Scripts/
!Scripts/main.py
!Scripts/texto.txt
"""

# Traverse all subdirectories in the root directory
for subdir, dirs, files in os.walk(root_dir):
    # Check if the current directory is a .venv directory
    if os.path.basename(subdir) == ".venv":
        gitignore_path = os.path.join(subdir, ".gitignore")
        if os.path.isfile(gitignore_path):
            # Write the desired content to the .gitignore file
            with open(gitignore_path, 'w') as file:
                file.write(gitignore_content)
            print(f"Updated: {gitignore_path}")

print("All .gitignore files have been updated.")
#Script creado por Emanuel Coletti
