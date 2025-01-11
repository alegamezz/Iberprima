import reflex as rx

def product_card(title, description, price, image):
    return rx.card(
        rx.vstack(
            rx.image(
                src=image,
                height="180px",
                width="100%",
                object_fit="cover",
                border_radius="12px 12px 0 0",  # Esquinas redondeadas superiores
            ),
            rx.box(
                rx.heading(title, size="5", color="#333333", margin_bottom="2", justify="center"),  # Tamaño ajustado para encajar mejor
                rx.text(f"${price}", font_size="lg", font_weight="bold", color="#4CAF50", justify="center"),  # Precio destacado en verde
                padding="4",
                text_align="center",
                justify_content="center",
                width="100%",
            ),
            spacing="3",
        ),
        border_radius="12px",  # Esquinas redondeadas en toda la tarjeta
        box_shadow="lg",
        width="250px",  # Ancho fijo
        height="300px",
        bg="white",
        _hover={
            "box_shadow": "xl", 
            "transform": "scale(1.03)", 
            "transition": "transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out"  # Animación suave al entrar y salir
        },
        transition="transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out",  # Suaviza la vuelta al tamaño original
        overflow="hidden",  # Evita que el contenido se desborde
    )
