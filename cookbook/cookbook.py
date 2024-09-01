import reflex as rx

from cookbook.pages import *

style = {
    rx.button: {
        "font_family": "Comic Sans MS",
        "background_color": "transparent",
        "color": rx.color_mode_cond(light="black", dark="white"),
    },
}


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="purple",
    ),
    style=style,
)
