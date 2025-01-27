import reflex as rx

from iberprima.components.footer import footer
from iberprima.components.header import header


@rx.page(route="/test", title="Iberprima - Productos", description="Nuestros productos")
def test():
    return rx.vstack(
        header(),
        rx.spacer(),
        footer(),
        height="100vh",
        
    )