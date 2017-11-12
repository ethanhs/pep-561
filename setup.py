from distutils.core import setup

setup(
    name="typedpkg",
    url="ethanhs.me",
    author="Ethan Smith",
    author_email="ethan@ethanhs.me",
    version="0.1",
    package_data={"typedpkg": ["py.typed"]},
    packages=["typedpkg"]
)