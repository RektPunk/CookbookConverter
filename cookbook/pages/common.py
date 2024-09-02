import reflex as rx

from cookbook.components.jupyter import jupyter
from cookbook.templates import template

BASE_RAW_URL = "assets"  # FIXME: input basic raw path including url


def create_route_component(route: str) -> rx.Component:
    @template(route=route)
    def dynamic_component() -> rx.Component:
        return jupyter(path=f"{BASE_RAW_URL}/{route}.ipynb")

    return dynamic_component
