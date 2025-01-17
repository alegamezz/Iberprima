import reflex as rx
def header_link(content, href="#"):
    return rx.link(
        content,
        href=href,
        style= {
            "color": "gray",
            "a.rt-Link.css-u82ugq-Component:hover": {
                "color": "#4a4a4a"  # darker gray
            }
        },
        text_decoration="none", 
        weight="regular",
    )


def mobile_menu():
        return rx.menu.root(
            rx.menu.trigger(
                rx.icon_button(
                    "menu",
                    color="gray",
                    box_shadow="0px 4px 6px rgba(0, 0, 0, 0.1)",
                    _hover={
                        "background": "#d3d3d3",  # Un gris claro en hexadecimal
                        "cursor": "pointer",
                        "transition": "background 0.2s ease",  # Transición suave
                    },
                    background="white",
                    border_radius="10px",  # Mayor radio de borde
                ),
            ),
            rx.menu.content(
                rx.menu.item("Opción 1"),
                rx.menu.item("Opción 2"), 
                rx.menu.separator(),
                rx.menu.item("Opción 3"),
            ),
        )


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
                header_link("Inicio", href="/"),
                header_link("Acerca de", href="/about"),
                header_link("Contacto", href="/contact"),        # Nuevo enlace
                spacing="3",  # Espaciado entre enlaces
                align="center",
                justify="end",
                width="50%",  # Ajustar el ancho del contenedor para que no ocupe todo
            ),
            # Mobile menu
            mobile_menu(),
            # Search and icons section
            rx.hstack(
                rx.color_mode.button(
                    aria_label="Switch theme",
                    color="gray",
                    box_shadow="0px 4px 6px rgba(0, 0, 0, 0.1)",
                    _hover={
                        "background": "#d3d3d3",  # Un gris claro en hexadecimal
                        "cursor": "pointer",
                        "transition": "background 0.2s ease",  # Transición suave
                    },
                    background="white",
                    border_radius="10px",  # Mayor radio de borde
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