import setuptools, json
from setuptools import setup

# This file should not be edited when changing versions, edit the package metadata file
_metadata = json.load(open("msad_query/_metadata.json", "r"))

setup(
    name=_metadata["name"],
    version=_metadata["version"],
    author=_metadata["author"],
    author_email=_metadata["author_email"],
    description=_metadata["description"],
    long_description=open("readme.asciidoc").read(),
    license=open("license.md").read(),
    package_data=_metadata["packageData"],
    include_package_data=True,
    packages=setuptools.find_packages(),
    url=_metadata["url"],
    install_requires=open(_metadata["requirements"], "r").read().splitlines(),
    classifiers=_metadata["classifiers"],
)
