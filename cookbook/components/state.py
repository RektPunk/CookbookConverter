from typing import Dict

import reflex as rx


class NotebookState(rx.State):
    basic_use: Dict[str, str] = {
        "introduction": "basic_use/introduction",
    }
    advanced_use: Dict[str, str] = {
        "advanced": "advanced_use/advanced",
    }

    @classmethod
    def get_keys(cls):
        return list(cls.__annotations__.keys())

    @classmethod
    def get_values(cls):
        return [getattr(cls, key) for key in cls.get_keys()]
