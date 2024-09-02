from typing import Dict

from cookbook.components.jupyter import CookBookNotebook


class NotebookState(CookBookNotebook):
    """{text on link: router path}"""

    basic_use: Dict[str, str] = {
        "introduction": "introduction",
    }
    advanced_use: Dict[str, str] = {
        "advanced": "advanced",
    }
