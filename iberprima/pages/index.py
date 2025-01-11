import reflex as rx

@rx.page(route="/", title="Iberprima", description="Welcome to Iberprima")
def index():
    return rx.box(
        # Contenedor de la imagen de fondo
        rx.box(
            background="center/cover url('/media/peakpx.jpg')",
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
            z_index="-2",  # Coloca la imagen detrás de las partículas
        ),
        # Contenedor de partículas
        rx.box(
            id="particles-container",  # Contenedor de partículas
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
            z_index="-1",  # Las partículas van sobre la imagen
        ),
        rx.script(src="/particles.min.js"),  # Biblioteca de partículas
        rx.script(src="/particles-config.js"),  # Configuración personalizada
        # Contenido principal
        rx.vstack(
            rx.image(
                src="/media/logo.png",
                width="350px",
                height="auto",
            ),
            rx.text("Líderes en la distribucción de glutamato monosódico", color="gray"),
            rx.hstack(
                rx.button("Consultar productos", 
                          on_click=rx.redirect("/products"),
                          color_scheme="grass", 
                          variant="soft", 
                          width="180px"),
                rx.button("Contacto", variant="soft", width="180px"),
                spacing="4",
            ),
            spacing="4",
            align="center",
            padding="10",
            justify_content="center",
            align_items="center",
            height="100vh",
        ),
        width="100%",
        height="100vh",
        color="white",
    )
