import reflex as rx

def header():
    return rx.box(
        rx.flex(
            # Logo section
            rx.image(
                src="/media/logo.png",
                alt="Logo",
                width=["100px", "150px"],
                height="auto",
            ),
            # Navigation menu
            rx.hstack(
                rx.link("Sobre nosotros", href="/about", color="gray", _hover={"color": "purple"}),
                rx.link("Contacto", href="/contact", color="gray", _hover={"color": "purple"}),
                rx.link("Servicios", href="/services", color="gray", _hover={"color": "purple"}),  # Nuevo enlace
                rx.link("Blog", href="/blog", color="gray", _hover={"color": "purple"}),          # Nuevo enlace
                spacing="3",  # Espaciado entre enlaces
                align="center",
                justify="end",
                width="50%",  # Ajustar el ancho del contenedor para que no ocupe todo
            ),
            # Search and icons section
            rx.hstack(
                rx.color_mode.button(
                    aria_label="Switch theme",
                    color="gray",
                    box_shadow="0px 4px 6px rgba(0, 0, 0, 0.1)",
                    _hover={"background": "gray", "cursor": "pointer"},
                ),
                spacing="2",  # Espaciado entre íconos si añades más
                height="100%",
                align="center",
            ),
            justify="between",
            align="center",
            width="100%",
            height="100%",
        ),
        background="white",
        border_bottom="1px solid #e2e8f0",
        position="sticky",  # Fija el header mientras se desliza
        top="0",  # Se pega al borde superior de la ventana
        z_index="10",  # Asegura que esté por encima de otros elementos
        display="flex",
        align_items="center",
        justify_content="center",
        height="60px",
        width="100%",
        padding="0 2rem",
    )