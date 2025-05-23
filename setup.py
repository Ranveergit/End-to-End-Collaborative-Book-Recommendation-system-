from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Based collaborative Books Recommender System"
AUTHOR_USER_NAME = "Ranveer"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Ranveer",
    description="it is a ML Based collaborative Books Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ranveergit/End-To-End-collaborative-Book-recommendation-system",
    author_email="ranveermanyumat@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
