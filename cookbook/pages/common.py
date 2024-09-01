import reflex as rx

from cookbook.components import jupyter
from cookbook.templates import template

BASE_RAW_URL = "https://raw.githubusercontent.com/openai/openai-cookbook/main/examples"


def create_route_component(route: str) -> rx.Component:
    @template(route=route)
    def dynamic_component() -> rx.Component:
        return rx.vstack(
            jupyter(
                path=f"{BASE_RAW_URL}/{route}.ipynb",
            ),
            spacing="3",
            justify="center",
        )

    return dynamic_component
