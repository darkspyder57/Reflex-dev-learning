"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx # type: ignore
from . import pages



def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        pages.home_page()
    )

style = {
    "font_family": "Arial",
    "font_size": "16px",
    "background_color" : "#ffffff",
    "margin" : "0px",
}

app = rx.App(style=style)
app.add_page(index)
