import os
from pathlib import Path
import logging

# Logging String Configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "KidneyDiseaseClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)

    # --- THIS IS THE FIX ---
    # Only create the directory if file_dir is not an empty string
    if file_dir and not os.path.exists(file_dir):
        os.makedirs(file_dir)
        logging.info(f"Created directory: {file_dir}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass  # Create an empty file
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")