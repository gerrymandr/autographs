
from setuptools import setup
from graph_tools import VERSION

reqs = [
    "networkx",
    "numpy"
]

setup(
    name="graph_tools",
    description="A collection of tools to make graph stuff easy",
    author="Metric Geometry and Gerrymandering Group",
    author_email="gerrymandr@gmail.com",
    url="https://github.com/gerrymandr/graph_tools",
    packages=["graph_tools"],
    version=VERSION
)
