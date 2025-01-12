import reflex as rx


def footer():
    return rx.box(
        rx.vstack(
            # Sección principal con las categorías
            rx.flex(
                # Columna: "¿Tienes alguna pregunta o sugerencia?"
                rx.vstack(
                    rx.image(
                        src="/media/logo.png",
                        width="250px",
                        height="auto",
                        padding_left="-1rem",
                    ),
                    rx.vstack(
                        rx.text("¿Tienes alguna pregunta o sugerencia?", font_weight="bold", size="2"),
                        rx.text("Llámanos o usa el formulario siguiente para contactarnos. ¡Gracias!", size="1"),
                        rx.link("Contáctanos", href="#", size="1", color="orange"),
                        width="100%",
                    ),                    
                    
                    align_items="flex-start",
                    width=["100%", "30%"],
                    padding="1rem",
                ),
                # Columna: "Quiénes somos"
                rx.vstack(
                    rx.text("Quiénes somos", font_weight="bold", size="2"),
                    rx.link("Sobre nosotros", href="#", size="1", color="gray"),
                    rx.link("Contáctanos", href="#", size="1", color="orange"),
                    align_items="flex-start",
                    width=["100%", "30%"],
                    padding="1rem",
                ),
                # Columna: "Condiciones"
                rx.vstack(
                    rx.text("Condiciones", font_weight="bold", size="2"),
                    rx.link("Preguntas frecuentes", href="#", size="1", color="gray"),
                    rx.link("Términos y condiciones", href="#", size="1", color="gray"),
                    rx.link("Transporte", href="#", size="1", color="gray"),
                    rx.link("Aviso legal", href="#", size="1", color="gray"),
                    rx.link("Política de privacidad", href="#", size="1", color="gray"),
                    rx.link("Política de cookies", href="#", size="1", color="gray"),
                    rx.link("Política de devoluciones", href="#", size="1", color="gray"),
                    align_items="flex-start",
                    width=["100%", "30%"],
                    padding="1rem",
                ),
                # Espaciado y estilo responsivo
                justify_content="space-between",
                gap="2rem",  # Espaciado entre columnas
                width = "100%",
                flex_direction=["column", "row"]
            ),
            rx.divider(color_scheme="gray"),
            # Sección del copyright (no se modifica)
            rx.box(
                rx.vstack(
                    rx.text(
                        "Copyright © 2025 ",
                        rx.link(
                            "IberPrima",
                            href="/",
                            text_decoration="none",
                        ),
                        " todos los derechos reservados",
                        font_size=["0.7rem", "0.7rem", "0.8rem"],
                        color="#FFFFFF",
                    ),
                    align="center",
                    width="100%",
                ),
                padding_bottom="1rem",
                background="#353838",
                width="100%",
                align_items="center",
                justify_content="center",
            ),
            width="100%",
        ),
        width="100%",
        background="#353838",
        color="white",
        align_items="center",
        justify_content="center",
    )
