import reflex as rx
from reflex.components.component import NoSSRComponent
import reflex_map as rxm

def location():
    longitude = -5.9859
    latitude = 37.3725

 
    return rx.vstack(
        rx.heading("¿Dónde estamos?", id="location", size="8"),
        rx.text("Nos encontramos en la siguiente dirección: " ),
        rx.text.em("Calle de la Ciencia, 2, 41092 Sevilla", style={"font-size": "1em"}),
        rx.card(
            rxm.map(
                initialViewState=dict(
                    longitude=longitude,
                    latitude=latitude,     
                    zoom=14,       
                ),
                mapStyle="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",
            ),
            width="800px",
            height="300px",
            border_radius="5px", 
            
        ),
    )