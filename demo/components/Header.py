import reflex as rx # type: ignore

def header():
    """Header component."""
    return rx.box(
        rx.box(
            # rx.image(src="/logo.jpg", width="100px", height="auto"),
            rx.text("Company Logo"),
            font_size="1.5rem",
            font_weight="bold",
            color="#ffffff",
            padding="0.5rem",
        ),
        background_color="#000000",
        width="100%",
        padding="1rem",
        display="flex",
        box_shadow="1px 4px 6px #eeeee4",
        position="sticky",
        top="0",
        z_index="1000",
        marginBottom = "10px"
    )
