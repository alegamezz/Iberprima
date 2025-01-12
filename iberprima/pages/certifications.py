import reflex as rx

def certifications():
    return rx.box(
        rx.heading("Certificaciones", id="certifications", size="8"),
        rx.text(
            """Iberprima cuenta con las siguientes certificaciones de calidad 
            y seguridad alimentaria:""",
            margin_y="1em",
        ),
        rx.unordered_list(
            rx.list_item("ISO 9001:2015"),
            rx.list_item("ISO 22000:2005"),
            rx.list_item("IFS Food"),
            rx.list_item("Halal"),
            rx.list_item("Kosher"),
        ),
        margin_bottom="3em",
        width="100%",
    )