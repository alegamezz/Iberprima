import reflex as rx

def FeatureCard(icon, title, text, bg_color):
    return rx.card(
        rx.vstack(
            rx.icon(icon, color="yellow.500", box_size="6"),  # Icon color can be adjusted
            rx.heading(title, size="4", margin_y="0.5em"),
            rx.text(text, text_align="center"),
            align_items="center",
            justify_content="center",
            width="100%",
        ),
        padding="2em",
        background=bg_color,
        border_radius="lg",
        shadow="md",
        height="100%",
        _hover={
            "shadow": "lg",
            "transform": "scale(1.05)",
            "transition": "transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out",
        },
    )
