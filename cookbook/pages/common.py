import reflex as rx

from cookbook.components import jupyter
from cookbook.templates import template

BASE_RAW_URL = "https://raw.githubusercontent.com/openai/openai-cookbook/main/examples"


def create_route_component(route: str) -> rx.Component:
    @template(route=route)
    def dynamic_component() -> rx.Component:
        return jupyter(path=f"{BASE_RAW_URL}/{route}.ipynb")

    return dynamic_component
