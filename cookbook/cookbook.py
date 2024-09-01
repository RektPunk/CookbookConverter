# flake8: noqa
import reflex as rx

from cookbook import styles
from cookbook.pages import *

app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
)
