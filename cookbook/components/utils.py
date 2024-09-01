import re
from typing import Optional

import black
import isort


def is_url(path) -> bool:
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


def convert_local_image_paths(markdown_text: str, image_base_url: Optional[str]) -> str:
    if image_base_url is None:
        return markdown_text

    local_image_pattern = re.compile(r"!\[([^\]]*)\]\(([^http][^\)]+)\)")

    def _replace_local_path(match):
        alt_text = match.group(1)
        local_path = match.group(2).lstrip("/")
        global_url = f"{image_base_url}{local_path}?raw=true"
        return f"![{alt_text}]({global_url})"

    return local_image_pattern.sub(_replace_local_path, markdown_text)


def format_code_lint(code: str) -> str:
    try:
        isorted_code = isort.code(code=code)
        return black.format_str(isorted_code, mode=black.Mode())
    except Exception:
        return code
