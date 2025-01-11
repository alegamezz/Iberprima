import reflex as rx

class Product(rx.Base):
    """The product model."""
    name: str
    price: float 
    image: str