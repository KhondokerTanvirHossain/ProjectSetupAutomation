import shutil
import os

def create_project_from_template(template_path, new_project_path):
    template_name = os.path.basename(template_path)
    new_project_path = os.path.join(new_project_path, template_name)

    if os.path.exists(new_project_path):
        shutil.rmtree(new_project_path)

    shutil.copytree(template_path, new_project_path)
    print(f"New project created at {new_project_path}")