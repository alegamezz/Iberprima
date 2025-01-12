import reflex as rx

from iberprima.components.header import header
from iberprima.components.product_card import product_card
from iberprima.components.footer import footer
from iberprima.components.sidebar import sidebar
from iberprima.components.sidebar_link import sidebar_link
from iberprima.pages.about import about
from iberprima.pages.applications import applications
from iberprima.pages.benefits import benefits
from iberprima.pages.certifications import certifications
from iberprima.pages.msg import msg
from iberprima.states import ProductState



@rx.page(route="/products", title="Iberprima - Productos", description="Nuestros productos")
def products():
    return rx.vstack(
        rx.vstack(
            header(),
            width="100%",
        ),
        
        
        # Contenedor principal con flex para sidebar y contenido
        rx.hstack(
            # Contenido principal
            rx.box(
                rx.vstack(
                    # Sección Quiénes Somos
                    about(),
                    # Sección MSG
                    msg(),
                    # Sección Beneficios
                    benefits(),
                    # Sección Aplicaciones
                    applications(),
                    # Sección Certificaciones
                    certifications(),

                    spacing="4",
                    align_items="start",
                    width="100%",
                ),
                flex="1",
                padding="4",
                margin_right=["0px", "0px", "250px", "250px"]  # Espacio para el índice fijo
            ),
            # Sidebar con índice
            sidebar(),

            align_items="start",
            spacing="4",
            width="100%",
            max_width="1200px",
            margin="0 auto",
            right="0",
        ),
        
        rx.spacer(),
        footer(),
        width="100%",
        min_height="100vh",
        align="center",
    )
