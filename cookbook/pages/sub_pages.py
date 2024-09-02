from cookbook.pages.common import create_route_component

introduction = create_route_component(
    route="introduction", file_path="basic_use/introduction.ipynb"
)
advanced = create_route_component(
    route="advanced", file_path="advanced_use/advanced.ipynb"
)
