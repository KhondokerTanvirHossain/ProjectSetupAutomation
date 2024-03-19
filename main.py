import json
from scripts import project_creator

def main():
    with open('config/config.json', 'r') as f:
        config = json.load(f)

    template_path = config['template_path']
    new_project_path = config['new_project_path']
    project_creator.create_project_from_template(template_path, new_project_path)

if __name__ == "__main__":
    main()