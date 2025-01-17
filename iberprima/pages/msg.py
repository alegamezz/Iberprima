import reflex as rx

from iberprima.states import MsgState


def msg():
    return rx.vstack(
        # Título principal
        rx.heading("Glutamato Monosódico", size="8", mb="4"),
        
        # Contenedor para imagen y texto
        rx.hstack(
            # Columna izquierda con texto
            rx.vstack(
                rx.text(
                    """Desde su descubrimiento en 1908 por el científico japonés Kikunae Ikeda, 
                    el glutamato monosódico (MSG) ha desempeñado un papel fundamental en la 
                    industria alimentaria global. Fue creado para capturar el sabor umami, un gusto esencial presente 
                    en alimentos como tomates y queso parmesano.""",
                    flex="1",
                    margin_y="1em",
                    color="gray.700",
                ),
                 rx.text(
                    """En las décadas de 1970 y 1980, el MSG ganó notoriedad debido a un fenómeno 
                    llamado 'Síndrome del restaurante chino', una serie de síntomas atribuidos 
                    erróneamente al consumo de este aditivo. Sin embargo, estudios científicos 
                    recientes han desmentido esos mitos, confirmando que el MSG es seguro cuando 
                    se consume en cantidades moderadas.""",
                    margin_y="1em",
                    color="gray.700",

                ),
            ),
            
            
            # Imagen central

            rx.image(
                src="/media/msg_ikeda.jpg", 
                width="20%",
                height="auto",
                margin_left="2em",
                margin_top="1em",
                box_shadow="rgba(0, 0, 0, 0.15) 0px 15px 30px -10px",
                transition="all 0.3s ease-in-out",  # Agrega una transición suave
                _hover={"transform": "scale(1.1)"},  # Efecto de zoom al pasar el cursor
                border_radius="10%",
                

            ),

            
            
            align="start",
            spacing="4",
        ),
        
       

        
        rx.text(
            """Hoy en día, el MSG es utilizado en todo el mundo como un aditivo clave para realzar el 
            sabor de alimentos procesados, sopas, salsas y snacks.""",
            margin_y="1em",
            color="gray.700",

        ),
        
        # Título para la gráfica
        rx.heading("Glutamato Monosódico a lo Largo del Tiempo", size="5", mt="6", mb="4"),
        rx.card(
             # Gráfica de líneas usando recharts
            rx.recharts.line_chart(
                rx.recharts.line(
                    data_key="popularity",
                    type_="monotone",
                    stroke=rx.color("blue", 9),
                    stroke_width=2,
                ),
                rx.recharts.x_axis(
                    data_key="year",
                    label={"value": "Año", "position": "bottom"}
                ),
                rx.recharts.y_axis(
                    label={"value": "Popularidad (%)", "angle": -90, "position": "left"}
                ),
                rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
                rx.recharts.graphing_tooltip(
                    separator=" - ",  
                    content_style={   
                        "backgroundColor": rx.color("accent", 4),
                        "borderRadius": "4px",
                        "padding": "8px",
                    },
                    wrapper_style={   
                        "backgroundColor": rx.color("accent", 3),
                        "borderRadius": "8px",
                        "padding": "10px",
                    },
                    
                    

                ),
                data=MsgState.msg_data,
                width="100%",
                height=300,
                margin={
                    "top": 20,
                    "right": 20,
                    "left": 20,
                    "bottom": 20,
                },
            ),
            margin_top="2em",
            margin_bottom="2em",    
            background="#F5F5F5",
            width="80%",
        ),
       
        
        # Texto final para reflexionar
        rx.text(
            """La gráfica muestra cómo el MSG ha enfrentado altibajos a lo largo de su historia. 
            Desde su auge inicial en el siglo XX hasta su caída durante los años 70 y 80 debido a mitos, 
            y su reciente resurgimiento gracias a la ciencia moderna.""",
            margin_y="1em",
            color="gray.700",
        ),
        
        margin_bottom="3em",
        width="100%",
        text_align="justify",
    )