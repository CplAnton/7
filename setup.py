import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clean_folder",
    version="1.1.1",
    author="Anton",
    description="doing smth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/clean_folder",
    packages=["clean_folder"],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "clean-folder=clean_folder.sort:main"
        ]
    },
)
