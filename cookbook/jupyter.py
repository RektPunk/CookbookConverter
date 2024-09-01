import json
from typing import Dict, List, Optional

import reflex as rx
import requests

from cookbook.utils import convert_local_image_paths, format_code_lint, is_url


def _read_jupyter(path: str) -> List[Dict]:
    if is_url(path=path):
        response = requests.get(path)
        notebook = response.json()
    else:
        with open(path, "r", encoding="utf-8") as file:
            notebook = json.load(file)
    return notebook["cells"]


def _render_output(output: Dict) -> rx.Component:
    output_type = output["output_type"]
    if output_type == "stream":
        return rx.text("".join(output.get("text", "")), color="gray")
    elif output_type in {"display_data", "execute_result"}:
        data = output.get("data", {})
        if "text/plain" in data:
            return rx.text("".join(data["text/plain"]))
        if "text/html" in data:
            return rx.html("".join(data["text/html"]))
        if "image/png" in data:
            return rx.image(src=f"data:image/png;base64,{data['image/png']}")
    elif output_type == "error":
        return rx.text("".join(output.get("traceback", [])), color="red")
    return rx.text("Unsupported output type")


def _style_cell(cell: dict, image_base_url: Optional[str]) -> rx.Component:
    cell_type = cell.get("cell_type", "unknown")
    content = "".join(cell.get("source", ""))

    components = []
    if cell_type == "code":
        components.append(
            rx.code_block(
                format_code_lint(content),
                language="python",
                show_line_numbers=True,
                can_copy=True,
                width="100%",
            )
        )
        for output in cell.get("outputs", []):
            components.append(_render_output(output))
    elif cell_type == "markdown":
        components.append(
            rx.markdown(
                convert_local_image_paths(
                    markdown_text=content, image_base_url=image_base_url
                ),
            )
        )
    else:
        components.append(rx.text("Unsupported cell type"))
    return rx.vstack(*components)


def jupyter(path: str, image_base_url: str) -> rx.Component:
    _cells = _read_jupyter(path=path)
    return rx.vstack(
        *[_style_cell(cell=cell, image_base_url=image_base_url) for cell in _cells]
    )
