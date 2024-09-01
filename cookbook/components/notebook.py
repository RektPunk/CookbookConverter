from typing import Dict

import reflex as rx


class NotebookState(rx.State):
    chatgpt: Dict[str, str] = {
        "introduction_to_gpt4o": "/gpt4o/introduction_to_gpt4o",
    }
    third_party: Dict[str, str] = {
        "GPT_finetuning_with_wandb": "/third_party/GPT_finetuning_with_wandb",
        "How_to_automate_S3_storage_with_functions": "/third_party/How_to_automate_S3_storage_with_functions",
    }
