import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terraform-external-data",
    version="1.0.1",
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
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
