import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s: %(message)s:]')

project_name = "mai_nahi_bataunga"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/facade/__init__.py",
    f"src/{project_name}/facade/model_callpy",
    f"src/{project_name}/file_upload/__init__.py",
    f"src/{project_name}/file_upload/upload_file.py",
    f"src/{project_name}/prompts/__init__.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    ".gitignore"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath, "w") as f:
            pass
        logging.info(f"Creating empth file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")