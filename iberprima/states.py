import reflex as rx

from iberprima.models import Product



class ProductState(rx.State):
    products_list: list[Product] = [
        Product(
            name="Glutamáto monosódico Primario",
            price=100,
            image="https://www.cocinista.es/download/bancorecursos/ingredientes/ingrediente-glutamato-monosodico-MSG.jpg"
        ),
        Product(
            name="Ácido cítrico anhidro",
            price=120,
            image="https://www.equisalud.com/wp-content/uploads/2017/04/Acido-citrico-anhidro.webp"
        ),
        Product(
            name="Bicarbonato de sodio alimenticio",
            price=80,
            image="https://image.made-in-china.com/202f0j00mNvaJQSySkzP/Food-Grade-Sodium-Bicarbonate-with-99-Purity.webp"
        ),
        Product(
            name="Sorbato de potasio",
            price=150,
            image="https://quimicaindustrial.cl/wp-content/uploads/2021/01/Sorbato-de-Potasio.jpg"
        ),
        Product(
            name="Pectina de frutas",
            price=200,
            image="https://100x100ingredients.com/wp-content/uploads/2023/02/321.png"
        ),
        Product(
            name="Goma xantana",
            price=180,
            image="https://blogscdn.thehut.net/wp-content/uploads/sites/450/2018/08/15093916/goma-xantana.jpg"
        ),
        Product(
            name="Caseinato de calcio",
            price=250,
            image="https://www.hsnstore.com/media/catalog/product/cache/2/image/9df78eab33525d08d6e5fb8d27136e95/c/a/calcium-caseinate-powder-hsn.webp"
        ),
        Product(
            name="Alginato de sodio",
            price=220,
            image="https://www.micosmeticacasera.es/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/s/o/sodio-alginato.jpg"
        ),
        Product(
            name="Lecitina de soja",
            price=90,
            image="https://www.gastronomiavasca.net/uploads/image/file/5218/w700_Lecitina_de_soja_.jpg"
        ),
    ]

class MsgState(rx.State):
   msg_data: list[dict] = [
        {"year": "1908", "popularity": 10, "desc": "Descubrimiento del MSG"},
        {"year": "1940", "popularity": 50, "desc": "Expansión comercial"}, 
        {"year": "1970", "popularity": 90, "desc": "Máxima popularidad"},
        {"year": "1990", "popularity": 50, "desc": "Controversias"},
        {"year": "2000", "popularity": 70, "desc": "Estudios científicos"},
        {"year": "2020", "popularity": 100, "desc": "Aceptación global"}
    ]


class BenefitsState(rx.State):
    benefits: list[dict] = [
        {"title": "Mejora el sabor", "description": "Mejora el sabor de los alimentos", "image": "/media/benefits/sabor.jpg"},
        {"title": "Reduce sodio", "description": "Reduce el contenido de sodio", "image": "/media/benefits/sodio.jpg"},
        {"title": "Económico", "description": "Económicamente eficiente", "image": "/media/benefits/economico.jpg"},
        {"title": "Durabilidad", "description": "Aumenta la durabilidad de los alimentos", "image": "/media/benefits/durabilidad.jpg"},
        {"title": "Palatabilidad", "description": "Aumenta la palatabilidad de los alimentos", "image": "/media/benefits/palatibidad.jpg"},
        {"title": "Sabor umami", "description": "Potencia el sabor umami", "image": "/media/benefits/umami.jpg"},
        {"title": "Textura", "description": "Mejora la textura de los alimentos", "image": "/media/benefits/textura.jpg"},
    ]
    
    current_index: int = 0
    is_visible: bool = True  # Nuevo estado para controlar visibilidad

    @property
    def total_benefits(self) -> int:
        return len(self.benefits)

    @rx.event
    def next_benefit(self):
        self.set_visible(False)  # Ocultar antes de cambiar
        self.current_index = (self.current_index + 1) % self.total_benefits
        self.set_visible(True)   # Mostrar con nueva información

    @rx.event
    def prev_benefit(self):
        self.set_visible(False)  # Ocultar antes de cambiar
        self.current_index = (self.current_index - 1) % self.total_benefits
        self.set_visible(True)   # Mostrar con nueva información

    @rx.event
    def set_visible(self, visible: bool):
        self.is_visible = visible
