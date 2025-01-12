import reflex as rx

def msg():
    return rx.box(
        rx.heading("Glutamato Monosódico", id="msg", size="8"),
        rx.text(
            """El glutamato monosódico (MSG) es un potenciador del sabor 
            que se utiliza para realzar el sabor umami en los alimentos...""",
            margin_y="1em",
        ),
        margin_bottom="3em",
        width="100%",
    )