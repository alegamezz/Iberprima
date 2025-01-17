import reflex as rx

def sidebar_sublink(text: str, section_id: str):
    """Genera un enlace estilizado para la barra lateral."""
    return rx.link(
        text,
        href=f"/products/#{section_id}",
        weight="medium",
        color_scheme="gray",
        text_decoration="none",
        size="1",
        margin_left="2em",
    )