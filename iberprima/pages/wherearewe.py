import reflex as rx

from iberprima.components.footer import footer
from iberprima.components.header import header


@rx.page(route="/where", title="Iberprima - Productos", description="Nuestros productos")
def where():
    return rx.vstack(
        header(),
        rx.spacer(),
        footer(),
        height="100vh",
        
    )