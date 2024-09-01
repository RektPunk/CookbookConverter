from typing import Callable, Optional

import reflex as rx

from cookbook.components.jupyter import jupyter
from cookbook.templates.sidebar import sidebar

DEFAULT_META = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]


def template(
    route: str,
    title: Optional[str] = None,
    description: Optional[str] = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        _all_meta = [*DEFAULT_META]

        @rx.page(
            route=route,
            title=title or route[1:],
            description=description or "Description",
            meta=_all_meta,
        )
        def templated_page() -> rx.Component:
            return rx.container(
                rx.color_mode.button(position="top-right"),
                rx.hstack(
                    sidebar(),
                    page_content(),
                    direction="column",
                ),
                width="100%",
            )

        return templated_page

    return decorator
