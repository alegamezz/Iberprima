import reflex as rx

from iberprima.components.footer import footer
from iberprima.components.header import header


@rx.page(route="/contact", title="Iberprima - Productos", description="Nuestros productos")
def contact():
    return rx.vstack(
        header(),
        rx.spacer(),
        footer(),
        height="100vh",
        
    )