from typing import Dict, List

import reflex as rx

from cookbook.components.notebook import NotebookState


def footer() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text("GitHub", size="3"),
            href="https://github.com/RektPunk/cookbook-converter",
            color_scheme="gray",
            underline="none",
        ),
        rx.link(
            rx.text("Issue", size="3"),
            href="https://github.com/RektPunk/cookbook-converter/issues",
            color_scheme="gray",
            underline="none",
        ),
        rx.spacer(),
        rx.color_mode.button(style={"opacity": "0.8", "scale": "0.95"}),
        justify="start",
        align="center",
        width="100%",
        padding="0.35em",
    )


def document_link(info: List[str]) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.text(info[0], size="2"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.25rem",
            align="center",
        ),
        href=info[1],
        underline="none",
        weight="medium",
        width="100%",
    )


def accordian_item(
    text: str,
    state,
) -> rx.Component:
    return rx.accordion.item(
        header=rx.hstack(rx.icon("folder", size=20), rx.text(text, size="2")),
        content=rx.vstack(
            rx.foreach(
                state,
                document_link,
            )
        ),
    )


def accordian_items(texts: List[str], states: List[Dict[str, str]]):
    _items = []
    for text, state in zip(texts, states):
        _items.append(accordian_item(text=text, state=state))
    return rx.accordion.root(
        *_items,
        collapsible=True,
        type="multiple",
        variant="ghost",
    )


def render_items() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.hstack(
                rx.icon("home", size=20),
                rx.text("Home", size="3"),
                width="100%",
                padding_x="0.5rem",
                padding_y="0.75rem",
                align="center",
            ),
            href="/",
            underline="none",
            weight="medium",
            width="100%",
        ),
        accordian_items(
            texts=["ChatGPT", "Third party"],
            states=[NotebookState.chatgpt, NotebookState.third_party],
        ),
        spacing="1",
        width="100%",
        align="left",
    )
