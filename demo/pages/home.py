import reflex as rx # type: ignore

from demo import components

class MyState(rx.State):
    """App state to manage navigation."""
    content: str = "home"  # Initial state

    def set_content(self, value: str):
        """Update the content."""
        self.content = value


def navbar():
    """Navbar component with clickable items that update page content."""
    nav_items = [
        ("Equity Analysis", "equity_analysis"),
        ("Exercise Planning", "exercise_planning"),
        ("Exit Planning", "exit_planning"),
        ("Benchmarking", "benchmarking"),
        ("Financing", "financing"),
        ("Tax Planning", "tax_planning"),
    ]

    return rx.box(
        *[
            rx.link(
                label,
                on_click=MyState.set_content(value),
                class_name="nav-item",
                padding="0.5rem 1rem",
                border_radius="0.25rem",
                _hover={"background_color": "#f0f0f0"},
                font_size="1rem",
                text_decoration="none",
                color="#000000", 
                cursor="pointer",
            )
            for label, value in nav_items
        ],
        display="flex",
        justify_content="space-evenly", 
        align_items="center",
        background_color="#ffffff",
        box_shadow="0 2px 4px rgba(0, 0, 0, 0.1)",
        padding="1rem 2rem",
        border_radius="0.25rem",
        width="100vw",
        max_width="100%",  
        position="sticky",
        top="0",
        z_index="1000",
    )



def content_box():
    """content box that changes based on the selected nav item."""
    return rx.cond(
        MyState.content == "equity_analysis",
        rx.box(
            "Equity Analysis",
            font_size="1.5rem",
            margin="2rem",
        ),
        rx.cond(
            MyState.content == "exercise_planning",
            rx.box(
                "Exercise Planning",
                font_size="1.5rem",
                margin="2rem",
            ),
            rx.cond(
                MyState.content == "exit_planning",
                rx.box(
                    "Exit Planning",
                    font_size="1.5rem",
                    margin="2rem",
                ),
                rx.cond(
                    MyState.content == "benchmarking",
                    rx.box(
                        "Benchmarking",
                        font_size="1.5rem",
                        margin="2rem",
                    ),
                    rx.cond(
                        MyState.content == "financing",
                        rx.box(
                            "Financing",
                            font_size="1.5rem",
                            margin="2rem",
                        ),
                        rx.box(
                            "Tax Planning",
                            font_size="1.5rem",
                            margin="2rem",
                        ),
                    ),
                ),
            ),
        ),
    )


def home_page():
    """Home page with a dynamic navbar and content below."""
    return rx.fragment(
        components.header(),
        navbar(),  # Navbar stays at the top
        content_box(),  # Dynamic content changes based on state
    )