import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="winevt_json",
    version="0.0.1",
    author="Rob Noeth",
    author_email="rob.noeth@gmail.com",
    description="A utility to convert windows system event logs into json objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LevelEffect/winevt_json",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
