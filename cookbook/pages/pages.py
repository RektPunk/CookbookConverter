"""All pages made with .md, .ipynb"""

import os

from .common import create_route_component

index = create_route_component(route="/", file_path="index.md")

introduction = create_route_component(
    route="introduction", file_path=os.path.join("basic_use", "introduction.ipynb")
)
