from typing import Dict, List

import reflex as rx


class NotebookState(rx.State):
    chatgpt: Dict[str, str] = {
        "introduction_to_gpt4o": "/gpt4o/introduction_to_gpt4o",
    }
    third_party: Dict[str, str] = {
        "GPT_finetuning_with_wandb": "/third_party/GPT_finetuning_with_wandb",
        "How_to_automate_S3_storage_with_functions": "/third_party/How_to_automate_S3_storage_with_functions",
        "Openai_monitoring_with_wandb_weave": "/third_party/Openai_monitoring_with_wandb_weave",
        "Visualizing_embeddings_in_Kangas": "/third_party/Visualizing_embeddings_in_Kangas",
        "Visualizing_embeddings_in_wandb": "/third_party/Visualizing_embeddings_in_wandb",
        "Visualizing_embeddings_with_Atlas": "/third_party/Visualizing_embeddings_with_Atlas",
        "financial_document_analysis_with_llamaindex": "/third_party/financial_document_analysis_with_llamaindex",
    }


def document_link(info: List[str]) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.text(info[0], size="2"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.25rem",
            align="center",
        ),
        href=info[1],
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_item(text: str, icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def accordian_item(
    text: str,
    state,
) -> rx.Component:
    return rx.accordion.item(
        header=rx.hstack(rx.icon("folder"), rx.text(text)),
        content=rx.vstack(
            rx.foreach(
                state,
                document_link,
            )
        ),
    )


def accordian_items(texts: List[str], states: List[Dict[str, str]]):
    _items = []
    for text, state in zip(texts, states):
        _items.append(accordian_item(text=text, state=state))
    return rx.accordion.root(
        *_items,
        collapsible=True,
        type="multiple",
        variant="ghost",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Home", "home", "/"),
        accordian_items(
            texts=["ChatGPT", "Third party"],
            states=[NotebookState.chatgpt, NotebookState.third_party],
        ),
        spacing="1",
        width="100%",
        align="left",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                sidebar_items(),
                spacing="5",
                position="fixed",
                left="0px",
                top="0px",
                z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                align="start",
                height="100%",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(rx.icon("align-justify", size=30)),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(rx.icon("x", size=30)),
                                width="100%",
                            ),
                            sidebar_items(),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("accent", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )
