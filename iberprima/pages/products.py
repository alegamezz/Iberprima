import reflex as rx

from iberprima.components.product_card import product_card
from iberprima.components.footer import footer
from iberprima.states import ProductState





@rx.page(route="/products", title="Iberprima - Productos", description="Nuestros productos")
def products():
    return rx.vstack(
        
        # Contenido principal de la página
        rx.vstack(
            rx.spacer(),
            rx.heading("Nuestros productos", size="8", color="white", mb="8"),
            rx.spacer(),
            rx.flex(
                rx.foreach(
                    ProductState.products_list,
                    lambda product: product_card(
                        product["name"], 
                        "", 
                        product["price"], 
                        product["image"]
                    )
                ),
                spacing="4",
                width="100%",
                wrap="wrap",  # Allows items to wrap to next line
                justify="center"
            ),
            align="center",
            padding="8",
        ),
        rx.spacer(),
        # Pie de página
        footer(),
        # Configuración del fondo
        background="center/cover url('/media/peakpx.jpg')",
        width="100%",
        min_height="100vh",
        color="white",
        align="center",
    )
