import os

import reflex as rx

from cookbook.components.jupyter import jupyter
from cookbook.templates import template

BASE_RAW_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "notebooks"
)  # FIXME: input basic raw path including url


def create_route_component(route: str, file_path: str) -> rx.Component:
    @template(route=route)
    def dynamic_component() -> rx.Component:
        _file_path = os.path.join(BASE_RAW_PATH, file_path)
        if file_path.endswith(".ipynb"):
            return jupyter(path=_file_path)

        if file_path.endswith(".md"):
            with open(_file_path, encoding="utf-8") as file:
                content = file.read()
            return rx.markdown(content)

        return rx.markdown("")

    return dynamic_component
