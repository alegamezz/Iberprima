import reflex as rx

import reflex as rx

from iberprima.components.sidebar_link import sidebar_link
from iberprima.components.sidebar_sublink import sidebar_sublink


def sidebar():
    """Crea el componente del índice lateral fijo."""
    return rx.box(
        rx.vstack(  
            rx.heading("En esta página", size="3", weight="medium", margin_bottom="1em"),
            sidebar_link("¿Quiénes Somos?", "about"),
            sidebar_link("Glutamato Monosódico", "msg"),
            sidebar_sublink("MSG a lo largo del tiempo", "history"),
            sidebar_link("Beneficios", "benefits"),
            sidebar_link("Aplicaciones", "applications"),
            sidebar_link("Certificaciones", "certifications"),
            sidebar_link("¿Dónde estamos?", "location"),
            width="100%",
            spacing="3",
        ),
        position=["none", "none", "fixed", "fixed"],  # Hidden on mobile, fixed on desktop
        top="10%",  # Centrado verticalmente
        width="220px",  # Ajusta el ancho del índice si es necesario
        right="0",  # Fijar al borde derecho
        padding="1em",  # Espaciado interno opcional
        background_color="white",  # Fondo opcional para visibilidad
        box_shadow="lg",  # Sombra opcional para separar del contenido
        margin_right="4em",  # Espacio adicional para separar del contenido
        display=["none", "none", "block", "block"],

    )
