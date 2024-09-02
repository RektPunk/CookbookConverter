import json
import re
from typing import Dict, List, Optional

import black
import isort
import reflex as rx
import requests


def _is_url(path) -> bool:
    url_pattern = re.compile(
        r"^(?:http|ftp)s?://"
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        r"localhost|"
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"
        r"(?::\d+)?"
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return re.match(url_pattern, path) is not None


def _convert_local_image_paths(
    markdown_text: str, image_base_url: Optional[str]
) -> str:
    if image_base_url is None:
        return markdown_text

    local_image_pattern = re.compile(r"!\[([^\]]*)\]\(([^http][^\)]+)\)")

    def _replace_local_path(match):
        alt_text = match.group(1)
        local_path = match.group(2).lstrip("/")
        global_url = f"{image_base_url}{local_path}?raw=true"
        return f"![{alt_text}]({global_url})"

    return local_image_pattern.sub(_replace_local_path, markdown_text)


def _format_code_lint(code: str) -> str:
    try:
        isorted_code = isort.code(code=code)
        return black.format_str(isorted_code, mode=black.Mode())
    except Exception:
        return code


def _read_jupyter(path: str) -> List[Dict]:
    if _is_url(path=path):
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
                _format_code_lint(content),
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
                _convert_local_image_paths(
                    markdown_text=content, image_base_url=image_base_url
                ),
            )
        )
    else:
        components.append(rx.text("Unsupported cell type"))
    return rx.vstack(*components)


def jupyter(path: str, image_base_url: Optional[str] = None) -> rx.Component:
    _cells = _read_jupyter(path=path)
    return rx.vstack(
        *[_style_cell(cell=cell, image_base_url=image_base_url) for cell in _cells],
        width="100%",
    )


class CookBookNotebook(rx.State):
    @classmethod
    def get_keys(cls):
        return list(cls.__annotations__.keys())

    @classmethod
    def get_values(cls):
        return [getattr(cls, key) for key in cls.get_keys()]
