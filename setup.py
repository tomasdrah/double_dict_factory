import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="double_dict_factory",
    version="0.0.1",
    author="tomasdrah",
    author_email="tomasdrah@seznam.cz",
    description="Structure for double indexing objects with the use of factories for creation and removal",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/tomasdrah/double_dict_factory",
    project_urls={
        "Bug Tracker": "https://github.com/tomasdrah/double_dict_factory/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['double_dict_factory'],
    # install_requires=['requests'],
    python_requires=">=3.10",
)
