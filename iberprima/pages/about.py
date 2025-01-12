import reflex as rx

from iberprima.components.feature_card import FeatureCard

def about():
    return rx.box(
        
        # Header section
        rx.heading("¿Quiénes Somos?", id="about", size="8", mb="6"),
        
        # Main intro text
        rx.text(
            """Iberprima es una empresa familiar con más de 25 años de experiencia en la 
            distribución de aditivos alimentarios. Desde 1998, nos hemos dedicado a ofrecer 
            productos de la más alta calidad a la industria alimentaria española.""",
            margin_y="1em",
            color="gray.700",
        ),
        
        # Key points in a grid using the reusable component
        rx.grid(
            FeatureCard(
                icon="check",
                title="Experiencia",
                text="Más de dos décadas sirviendo a la industria alimentaria con excelencia.",
                bg_color="#F3E5F5",  # Azul claro
            ),
            FeatureCard(
                icon="heart",
                title="Valores Familiares",
                text="Empresa familiar comprometida con el servicio personalizado y la confianza.",
                bg_color="#E8F5E9",  # Verde claro
            ),
            FeatureCard(
                icon="star",
                title="Calidad",
                text="Productos certificados que cumplen con los más altos estándares internacionales.",
                bg_color="#FFFDE7",  # Amarillo claro
            ),
            columns="3",
            spacing="4",
            margin_y="3em",
        ),
        
        # Mission statement
        rx.card(
            rx.heading("Nuestra Misión", size="5", mb="4"),
            rx.text(
                """Proporcionar soluciones innovadoras y sostenibles en aditivos alimentarios, 
                manteniendo siempre los más altos estándares de calidad y servicio al cliente.""",
                color="gray.700",
            ),
            background="#E3F2FD",  # Azul claro
            padding="2em",
            border_radius="xl",
            margin_y="2em",
        ),
        margin_top="2em",
        margin_bottom="3em",
        width="100%",
    )
