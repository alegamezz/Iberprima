import reflex as rx
from iberprima.states import BenefitsState

def benefit_card():
    current_benefit = BenefitsState.benefits[BenefitsState.current_index]
    
    return rx.box(
        rx.box(
            rx.button(
                "←",
                on_click=BenefitsState.prev_benefit,
                is_disabled=BenefitsState.current_index == 0,
                size="1",
                color_scheme="gray",
                border_radius="50%",
                box_shadow="md",
                position="absolute",
                left="1rem",
                top="50%",
                transform="translateY(-50%)",
                z_index="1",
                height="30px",
                width="30px",
            ),
            rx.button(
                "→",
                on_click=BenefitsState.next_benefit,
                size="1",
                color_scheme="gray",
                border_radius="50%",
                box_shadow="md",
                position="absolute",
                right="1rem",
                top="50%",
                transform="translateY(-50%)",
                z_index="1",
                height="30px",
                width="30px",
            ),
            rx.heading(
                current_benefit["title"],
                color="white", 
                size="8",
                mb="2",
                weight="bold",
            ),
            rx.text(
                current_benefit["description"],
                color="white",
                font_size="1.1em",
                weight="medium",
                position="absolute",
                bottom="2rem",
                right="2rem"
            ),
            padding="2rem",
            border_radius="10px",
            height="100%",
            width="100%",
            position="relative",
            transform=rx.cond(
                BenefitsState.is_visible,
                "translateX(0)",
                "translateX(100%)"
            ),  # Usar rx.cond para la condición reactiva
            transition="transform 0.5s ease-in-out",  # Animación de transición
        ),
        background=f"center/cover url('{current_benefit['image']}')",
        width="100%",
        height="250px", 
        border_radius="10px",
        position="relative",
        overflow="hidden",
        box_shadow="rgba(0, 0, 0, 0.35) 0px 5px 15px",
        margin_top="2em",
    )


def benefits():
    return rx.box(
        rx.heading("Beneficios", id="benefits", size="8", mb="6"),
        benefit_card(),
        rx.moment(
            interval=4000,
            on_change=[
                lambda: BenefitsState.set_visible(False),  # Ocultar antes de cambiar
                lambda: BenefitsState.next_benefit(),      # Cambiar el beneficio
                lambda: BenefitsState.set_visible(True),   # Mostrar con transición
            ],
            display="none",
        ),
        margin_bottom="3em",
        width="100%",
        align="center",
        justify="center",
    )
