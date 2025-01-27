import reflex as rx

from iberprima.states import HeaderState


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
            display=["block", "block", "none"]
        )
def header_link(content, href="#", is_active=False):
    return rx.link(
        content,
        href=href,
        on_click=HeaderState.set_current_path(href),
        style={
            "color": "gray",
            "position": "relative",  # Necesario para posicionar el pseudo-elemento
            "padding_bottom": "4px",
            "_hover": {
                "color": "#CDCDCD",
            },
            "::after": {
                "content": '""',  # El pseudo-elemento
                "position": "absolute",
                "left": "0",
                "right": "0",
                "bottom": "-18px ",  # Desplaza la línea hacia abajo
                "height": "2px",  # Grosor de la línea
                "background_color": rx.cond(
                    is_active,
                    "#ADD8E6",  # Estilo activo
                    "transparent"  # Estilo por defecto
                ),
                "transition": "background-color 0.2s",
            },
            "_hover::after": {
                "background_color": "#CDCDCD",  # Color de la línea al hacer hover
            },
        },
        text_decoration="none",
        weight="regular",
        size="2",
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
                header_link("Sobre nosotros", href="/aboutus", is_active=HeaderState.current_path == "/aboutus"),
                header_link("¿Dónde nos encontramos?", href="/where", is_active=HeaderState.current_path == "/where"),
                header_link("Contacto", href="/contact", is_active=HeaderState.current_path == "/contact"),
                header_link("Transporte", href="/transport", is_active=HeaderState.current_path == "/transport"),
                header_link("MSG", href="/msg", is_active=HeaderState.current_path == "/msg"),
                spacing="3",
                align="center",
                justify="end",
                width="50%",
                display=["none", "none", "flex"],
            ),
            # Mobile menu
            rx.mobile_only(mobile_menu()),
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
        border_bottom="1px solid #e2e8f0",
        top="0",  # Se pega al borde superior de la ventana
        z_index="10",  # Asegura que esté por encima de otros elementos
        align_items="center",
        justify_content="center",
        height="60px",
        width="100%",
        padding="0 2rem",
    )