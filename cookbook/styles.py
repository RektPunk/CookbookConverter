import reflex as rx

border = f"1px solid {rx.color('gray', 5)}"
sidebar_width = "32em"
sidebar_content_width = "16em"
max_width = "1480px"
template_page_style = {
    "padding_top": ["1em", "1em", "2em"],
    "padding_x": ["auto", "auto", "2em"],
}
template_content_style = {
    "padding": "1em",
    "margin_bottom": "2em",
    "min_height": "90vh",
}
base_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
]
base_style = {
    "font_family": "Inter",
    rx.button: {
        "font_family": "Comic Sans MS",
        "background_color": "transparent",
        "color": rx.color_mode_cond(light="black", dark="white"),
    },
}
