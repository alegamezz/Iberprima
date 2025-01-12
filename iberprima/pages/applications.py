import reflex as rx

def applications():
    return rx.box(
        rx.heading("Aplicaciones", id="applications", size="8"),
        rx.text(
            """Nuestros productos son utilizados en una amplia gama 
            de aplicaciones en la industria alimentaria...""",
            margin_y="1em",
        ),
        margin_bottom="3em",
        width="100%",
    )