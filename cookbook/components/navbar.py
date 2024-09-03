"""Navbar component for the app."""

from typing import Dict, List

import reflex as rx

from .. import styles
from ..backend.table_state import NotebookState


def document_link(info: List[str]) -> rx.Component:
    return rx.link(
        rx.text(info[0], size="2"),
        href=info[1],
        underline="none",
        weight="medium",
        width="100%",
    )


def accordian_item(
    text: str,
    state: Dict[str, str],
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


def render_accordian_items() -> rx.Component:
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
            texts=["basic_use", "acvanced"],
            states=[NotebookState.basic_use, NotebookState.advanced_use],
        ),
        spacing="1",
        width="100%",
        align="left",
    )


def navbar_footer() -> rx.Component:
    """Navbar footer.

    Returns:
        The navbar footer component.
    """
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


def navbar_button() -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon("align-justify"),
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.hstack(
                        rx.spacer(),
                        rx.drawer.close(rx.icon(tag="x")),
                        justify="end",
                        width="100%",
                    ),
                    rx.divider(),
                    render_accordian_items(),
                    rx.spacer(),
                    navbar_footer(),
                    spacing="4",
                    width="100%",
                ),
                top="auto",
                left="auto",
                height="100%",
                width="20em",
                padding="1em",
                bg=rx.color("gray", 1),
            ),
            width="100%",
        ),
        direction="right",
    )


def navbar() -> rx.Component:
    """The navbar.

    Returns:
        The navbar component.
    """

    return rx.el.nav(
        rx.hstack(
            # The logo.
            rx.color_mode_cond(
                rx.image(src="/reflex_black.svg", height="1em"),
                rx.image(src="/reflex_white.svg", height="1em"),
            ),
            rx.spacer(),
            navbar_button(),
            align="center",
            width="100%",
            padding_y="1.25em",
            padding_x=["1em", "1em", "2em"],
        ),
        display=["block", "block", "block", "block", "block", "none"],
        position="sticky",
        background_color=rx.color("gray", 1),
        top="0px",
        z_index="5",
        border_bottom=styles.border,
    )
