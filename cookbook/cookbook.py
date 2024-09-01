import reflex as rx

from cookbook.jupyter import jupyter

BASE_URL: str = "https://github.com/RektPunk/cookbook/blob/main/cookbooks/upstage"
BASE_RAW_URL: str = (
    "https://raw.githubusercontent.com/RektPunk/cookbook/main/cookbooks/upstage"
)

style = {
    rx.button: {
        "font_family": "Comic Sans MS",
        "background_color": "transparent",
        "color": rx.color_mode_cond(light="black", dark="white"),
    },
}


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            jupyter(
                path=f"{BASE_RAW_URL}/Solar-Full-Stack%20LLM-101/01_hello_solar.ipynb",
                image_base_url=f"{BASE_URL}/Solar-Full-Stack%20LLM-101/",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App(style=style)
app.add_page(index)
