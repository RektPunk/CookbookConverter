import os

from cookbook.pages.common import create_route_component

index = create_route_component(route="/", file_path="index.md")

introduction = create_route_component(
    route="introduction", file_path=os.path.join("basic_use", "introduction.ipynb")
)
advanced = create_route_component(
    route="advanced", file_path=os.path.join("advanced_use", "advanced.ipynb")
)
