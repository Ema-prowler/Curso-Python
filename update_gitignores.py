import os

# Define el contenido deseado para los archivos .gitignore en .venv
venv_gitignore_content = """*
!.gitignore
!Scripts/
!Scripts/main.py
!Scripts/texto.txt
"""

# Define el contenido para ignorar los directorios .idea
idea_gitignore_content = ".idea/\n"

def actualizar_gitignore(root_dir):
    # Recorre todos los subdirectorios en el directorio raíz
    for subdir, dirs, files in os.walk(root_dir):
        # Comprueba si el directorio actual es un directorio .venv
        if os.path.basename(subdir) == ".venv":
            gitignore_path = os.path.join(subdir, ".gitignore")
            if os.path.isfile(gitignore_path):
                # Escribe el contenido deseado en el archivo .gitignore en .venv
                with open(gitignore_path, 'w') as file:
                    file.write(venv_gitignore_content)
                print(f"Actualizado: {gitignore_path}")
        
        # Comprueba si estamos en un directorio raíz del proyecto
        if os.path.basename(subdir) != ".venv" and '.idea' in dirs:
            gitignore_path = os.path.join(subdir, ".gitignore")
            if os.path.isfile(gitignore_path):
                # Lee el contenido actual del archivo .gitignore
                with open(gitignore_path, 'r') as file:
                    gitignore_content = file.read()
                
                # Comprueba si la regla para ignorar .idea ya está presente
                if idea_gitignore_content.strip() not in gitignore_content:
                    # Añade el contenido para ignorar los directorios .idea al archivo .gitignore
                    with open(gitignore_path, 'a') as file:
                        file.write(idea_gitignore_content)
                    print(f"Regla para ignorar .idea añadida a: {gitignore_path}")
                else:
                    print(f"La regla para ignorar .idea ya está presente en: {gitignore_path}")
            else:
                # Crea un nuevo archivo .gitignore con el contenido para ignorar los directorios .idea
                with open(gitignore_path, 'w') as file:
                    file.write(idea_gitignore_content)
                print(f"Creado y actualizado: {gitignore_path}")

    print("Todos los archivos .gitignore han sido actualizados.")

if __name__ == "__main__":
    # Obtén el directorio donde está ubicado el script
    root_dir = os.path.dirname(os.path.abspath(__file__))

    actualizar_gitignore(root_dir)
    print("Script creado por Emanuel Coletti v4")
