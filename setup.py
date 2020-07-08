import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oca", # Replace with your own username
    version="0.0.1",
    author="oca",
    author_email="author@example.com",
    description="The OCA Django app",
    include_package_data=True,
    long_description_content_type="text/markdown",
    url="https://github.com/geosolutions-it/resiliencemada_oca",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)