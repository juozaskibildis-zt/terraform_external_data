from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="terraform-external-data",
    version="1.0.2",
    author="Juozas Kibildis",
    author_email="juozas.kibildis@zenitech.co.uk",
    description="Terraform external data package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juozaskibildis-zt/terraform_external_data",
    project_urls={
        "Bug Tracker": "https://github.com/juozaskibildis-zt/terraform_external_data/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)
