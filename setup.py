import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
     
__version__ ="0.0.0"

REPO_NAME = "Text-Summarization-Project"
AUTHOR_USER_NAME = "raghavb4563"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "raghavb4563@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarization Project",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/raghavb4563/Text-Summarization-Project",
    project_urls={
        "Bug Tracker": "https://github.com/raghavb4563/Text-Summarization-Project/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
