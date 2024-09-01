import reflex as rx

from cookbook.templates import template


@template(route="/")
def index() -> rx.Component:
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content)
