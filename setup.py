import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description =f.read()

__version__ = "0.0.1"

REPO_NAME = "MAIN-FLASK_APP"
AUTHOR_USER_NAME = "Sambhav"
SRC_REPO = "chat_with_files"
AUTHOR_EMAIL = "wasu9494@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python Flask app",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = "",
    project_urls = {
        "ADO Board": "",
        "BUg Tracker": "",
    
    },
    package_dir={"": "src"},
    pacakages = setuptools.find_packages(where="src")
)