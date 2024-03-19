import unittest
import os
import shutil
import sys

from scripts import project_creator

class TestProjectCreator(unittest.TestCase):
    def setUp(self):
        self.template_path = "templates/spring-boot-templates/application"
        self.new_project_path = "test-directory"

        # Ensure the new project directory is clean before each test
        if os.path.exists(self.new_project_path):
            shutil.rmtree(self.new_project_path)

    def test_create_project_from_template(self):
        project_creator.create_project_from_template(self.template_path, self.new_project_path)
        self.assertTrue(os.path.exists(self.new_project_path))
    
    def tearDown(self):
        if os.path.exists(self.new_project_path):
            shutil.rmtree(self.new_project_path)

if __name__ == "__main__":
    unittest.main()