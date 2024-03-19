import shutil
import os

def create_project_from_template(template_path, new_project_path):
    if os.path.exists(new_project_path):
        print(f"Project already exists at {new_project_path}")
        return

    shutil.copytree(template_path, new_project_path)
    print(f"New project created at {new_project_path}")