import reflex as rx

from cookbook import styles
from cookbook.components.bar.utils import footer, render_items


def sidebar() -> rx.Component:
    return rx.flex(
        rx.vstack(
            render_items(),
            rx.spacer(),
            footer(),
            justify="end",
            align="end",
            width=styles.sidebar_content_width,
            height="100dvh",
            padding="1em",
        ),
        display=["none", "none", "none", "none", "flex"],
        max_width=styles.sidebar_width,
        width="auto",
        height="100%",
        position="sticky",
        justify="end",
        top="0px",
        left="0px",
        flex="1",
        bg=rx.color("gray", 2),
    )
