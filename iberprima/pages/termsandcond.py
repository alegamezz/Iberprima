import reflex as rx

from iberprima.components.footer import footer
from iberprima.components.header import header

@rx.page(route="/terms", title="Términos y Condiciones", description="Condiciones de uso de FactorChem")
def termsandcond():
    return rx.vstack(
        header(),
        rx.box(
            rx.vstack(
                rx.heading("Terminos y condiciones", size="8"),
                rx.heading("Introducción" , size="6"),
                rx.text(
                                    """Al visitar nuestro sitio y/o comprar uno de nuestros productos, participas en nuestro “Servicio” y aceptas los siguientes términos y condiciones (“Términos de Servicio”, “Términos”), incluidos todos los términos y condiciones adicionales y las políticas a las que se hace referencia en el presente documento y/o disponible a través de hipervínculos. Estas Condiciones de Servicio se aplican a todos los usuarios del sitio, incluyendo sin limitación a usuarios que sean navegadores, proveedores, clientes, comerciantes, y/o colaboradores de contenido.
                
                Por favor, lee estos Términos de Servicio cuidadosamente antes de acceder o utilizar nuestro sitio web. Al acceder o utilizar cualquier parte del sitio, estás aceptando los Términos de Servicio. Si no estás de acuerdo con todos los términos y condiciones de este acuerdo, entonces no deberías acceder a la página web o usar cualquiera de los servicios.
                
                Cualquier función nueva y/o producto que se añadan a la tienda actual, también estarán sujetas a los Términos de Servicio. Puedes revisar la versión actualizada de los Términos de Servicio, en cualquier momento en esta página. Nos reservamos el derecho de actualizar, cambiar o reemplazar cualquier parte de los Términos de Servicio mediante la publicación de actualizaciones y/o cambios en nuestro sitio web.
                
                Es tu responsabilidad leer esta página periódicamente para verificar los cambios.
                
                Tú uso continuo o el acceso al sitio web después de la publicación de cualquier cambio constituye la aceptación de dichos cambios."""
                ,size="1",),
                rx.heading("Sección 1", size="5"),
                rx.text(
                    """Al utilizar este sitio, declaras que tienes al menos la mayoría de edad en tu estado o provincia de residencia, o que tienes la mayoría de edad en tu estado o provincia de residencia y que nos has dado tu consentimiento para permitir que cualquiera de tus dependientes menores use este sitio.

                    No puedes usar nuestros productos con ningún propósito ilegal o no autorizado tampoco puedes, en el uso del Servicio, violar cualquier ley en tu jurisdicción (incluyendo pero no limitado a las leyes de derecho de autor).

                    No debes transmitir gusanos, virus o cualquier código de naturaleza destructiva.

                    El incumplimiento o violación de cualquiera de estos Términos darán lugar al cese inmediato de tus Servicios"""
                ),
                rx.text("COOKIES AFECTADAS POR LA NORMATIVA Y COOKIES EXENTAS", font_weight="bold"),
                rx.text(
                    "Según la directiva de la UE, las cookies que requieren consentimiento son las de analítica, publicidad y afiliación, mientras "
                    "que las de carácter técnico y necesarias para el funcionamiento del sitio están exentas."
                ),
                rx.text("TIPO DE COOKIES", font_weight="bold"),
                rx.unordered_list(
                    rx.list_item("Según la entidad que las gestione: Cookies propias y de terceros."),
                    rx.list_item("Según el tiempo que permanecen activas: Cookies de sesión y persistentes."),
                    rx.list_item(
                        "Según la finalidad: Técnicas, de personalización, de análisis, publicitarias y de afiliación."
                    ),
                ),
                rx.text("TIPO DE COOKIES UTILIZADAS EN ESTE SITIO WEB", font_weight="bold"),
                rx.text("[render_cookies_list]"),
                rx.text(
                    "Mientras navega, pueden almacenarse cookies de nuestras redes sociales. Consulte la política de cookies de las redes sociales utilizadas."
                ),
                rx.text("REVOCACIÓN", font_weight="bold"),
                rx.text(
                    "Puede acceder a la configuración de su navegador para aceptar o rechazar cookies. A continuación, le proporcionamos enlaces "
                    "para configurar los navegadores más comunes:"
                ),
                rx.unordered_list(
                    rx.list_item(
                        rx.link("Google Chrome", href="https://support.google.com/chrome/answer/95647", target="_blank")
                    ),
                    rx.list_item(
                        rx.link("Microsoft Internet Explorer", href="https://support.microsoft.com/es-es/help/17442/windows-internet-explorer-delete-manage-cookies", target="_blank")
                    ),
                    rx.list_item(rx.link("Firefox", href="https://support.mozilla.org/es/kb/habilitar-y-deshabilitar-cookies-sitios-web-rastrear-preferencias", target="_blank")),
                    rx.list_item(rx.link("Safari", href="https://support.apple.com/kb/ph21411?locale=es_ES", target="_blank")),
                    rx.list_item(rx.link("Opera", href="http://help.opera.com/Windows/12.00/es-ES/cookies.html", target="_blank")),
                ),
                rx.text("DESACTIVACIÓN / ACTIVACIÓN Y ELIMINACIÓN DE COOKIES", font_weight="bold"),
                rx.text(
                    "Para restringir, bloquear o eliminar cookies, puede acceder a la configuración de su navegador. Cada navegador tiene "
                    "diferentes métodos, consulte la función de ayuda para más información. Tenga en cuenta que deshabilitar cookies puede afectar el "
                    "funcionamiento del sitio web."
                ),
                rx.text("INFORMACIÓN RELACIONADA CON EL TRATAMIENTO DE DATOS PERSONALES (ART.13 RGPD)", font_weight="bold"),
                rx.text("Responsable del tratamiento: Iberprima."),
                rx.text(
                    "La información recopilada se utiliza para rastrear acciones del usuario, analizar hábitos de navegación y ofrecer publicidad personalizada."
                ),
                rx.text(
                    "Legitimación: Su consentimiento otorgado para la utilización de cookies analíticas, comportamentales y publicitarias."
                ),
                rx.text(
                    "Plazo de conservación: Según lo indicado en el cuadro sobre el uso de cookies."
                ),
                rx.text(
                    "Derechos: Acceso, rectificación, supresión, portabilidad, retirada del consentimiento y oposición al tratamiento. Consulte la "
                    "Agencia Española de Protección de Datos para más información."
                ),
                 rx.spacer(),
                 align="center",
                spacing="4",
                align_items="start",
                padding="4",
               
            ),
            width="100%",
            max_width="800px",
            margin_bottom="1em",
        ),
        footer(),
        width="100%",
        min_height="100vh",
    )
