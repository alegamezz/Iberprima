import reflex as rx

from iberprima.components.header import header
from iberprima.components.footer import footer


@rx.page(route="/cookies", title="Iberprima - Política de Cookies", description="Información sobre el uso de cookies en Iberprima")
def cookies():
    return rx.vstack(
        header(),
        rx.box(
            rx.vstack(
                rx.heading("Política de Cookies", size="8"),
                rx.text("INTRODUCCIÓN", font_weight="bold"),
                rx.text(
                    "La web de Iberprima utiliza cookies propias y de terceros. Una cookie es un archivo que se descarga en su "
                    "ordenador al acceder a determinadas páginas web. Las cookies permiten, entre otras finalidades, asegurar el correcto "
                    "funcionamiento de la página, permitir un acceso más rápido a los servicios seleccionados, almacenar y recuperar información "
                    "sobre los hábitos de navegación de un usuario o de su equipo, e incluso reconocer al usuario en función de la información "
                    "contenida y la forma en que utiliza su equipo. Las cookies se asocian únicamente a un usuario anónimo y su ordenador o "
                    "dispositivo, y no proporcionan datos personales salvo consentimiento expreso del usuario."
                ,size="2", weight="regular"),
                rx.text(
                    "El usuario puede, en todo momento, aceptar o rechazar las cookies no estrictamente necesarias a través del panel de ajuste de cookies "
                    "proporcionado en nuestra web. Asimismo, podrá configurar su navegador sin que ello perjudique el acceso a los contenidos. Sin embargo, "
                    "el rechazo de las cookies podría afectar al funcionamiento de la web."
                ,size="2", weight="regular"),
                rx.spacer(),
                rx.text("COOKIES AFECTADAS POR LA NORMATIVA Y COOKIES EXENTAS", font_weight="bold"),
                rx.text(
                    "Según la directiva de la UE, las cookies que requieren consentimiento son las de analítica, publicidad y afiliación, mientras "
                    "que las de carácter técnico y necesarias para el funcionamiento del sitio están exentas."
                ,size="2", weight="regular"),
                rx.spacer(),

                rx.text("TIPO DE COOKIES", font_weight="bold"),
                rx.unordered_list(
                    rx.list_item("Según la entidad que las gestione: Cookies propias y de terceros.",size="2", weight="regular"),
                    rx.list_item("Según el tiempo que permanecen activas: Cookies de sesión y persistentes.",size="2", weight="regular"),
                    rx.list_item(
                        "Según la finalidad: Técnicas, de personalización, de análisis, publicitarias y de afiliación."
                    ,size="2", weight="regular"),
                ),
                rx.spacer(),

                rx.text("TIPO DE COOKIES UTILIZADAS EN ESTE SITIO WEB", font_weight="bold"),
                rx.text("[render_cookies_list]",size="2", weight="regular"),
                rx.text(
                    "Mientras navega, pueden almacenarse cookies de nuestras redes sociales. Consulte la política de cookies de las redes sociales utilizadas."
                ,size="2", weight="regular"),
                rx.text("REVOCACIÓN", font_weight="bold"),
                rx.text(
                    "Puede acceder a la configuración de su navegador para aceptar o rechazar cookies. A continuación, le proporcionamos enlaces "
                    "para configurar los navegadores más comunes:"
                ,size="2", weight="regular"),
                rx.unordered_list(
                    rx.list_item(
                        rx.link("Google Chrome", href="https://support.google.com/chrome/answer/95647", target="_blank")
                    ,size="2", weight="regular"),
                    rx.list_item(
                        rx.link("Microsoft Internet Explorer", href="https://support.microsoft.com/es-es/help/17442/windows-internet-explorer-delete-manage-cookies", target="_blank")
                    ,size="2", weight="regular"),
                    rx.list_item(rx.link("Firefox", href="https://support.mozilla.org/es/kb/habilitar-y-deshabilitar-cookies-sitios-web-rastrear-preferencias", target="_blank"),size="2", weight="regular"),
                    rx.list_item(rx.link("Safari", href="https://support.apple.com/kb/ph21411?locale=es_ES", target="_blank"),size="2", weight="regular"),
                    rx.list_item(rx.link("Opera", href="http://help.opera.com/Windows/12.00/es-ES/cookies.html", target="_blank"),size="2", weight="regular"),
                ),
                rx.spacer(),
                rx.text("DESACTIVACIÓN / ACTIVACIÓN Y ELIMINACIÓN DE COOKIES", font_weight="bold"),
                rx.text(
                    "Para restringir, bloquear o eliminar cookies, puede acceder a la configuración de su navegador. Cada navegador tiene "
                    "diferentes métodos, consulte la función de ayuda para más información. Tenga en cuenta que deshabilitar cookies puede afectar el "
                    "funcionamiento del sitio web."
                ,size="2", weight="regular"),
                rx.spacer(),
                rx.text("INFORMACIÓN RELACIONADA CON EL TRATAMIENTO DE DATOS PERSONALES (ART.13 RGPD)", font_weight="bold"),
                rx.text("Responsable del tratamiento: Iberprima.",size="2", weight="regular"),
                rx.text(
                    "La información recopilada se utiliza para rastrear acciones del usuario, analizar hábitos de navegación y ofrecer publicidad personalizada."
                ,size="2", weight="regular"),
                rx.text(
                    "Legitimación: Su consentimiento otorgado para la utilización de cookies analíticas, comportamentales y publicitarias."
                ,size="2", weight="regular"),
                rx.text(
                    "Plazo de conservación: Según lo indicado en el cuadro sobre el uso de cookies."
                ,size="2", weight="regular"),
                rx.text(
                    "Derechos: Acceso, rectificación, supresión, portabilidad, retirada del consentimiento y oposición al tratamiento. Consulte la "
                    "Agencia Española de Protección de Datos para más información."
                ,size="2", weight="regular"),
                spacing="4",
                align_items="start",
                padding="4",
                text_align="justify",
                align="center",
            ),
            width=["80%", "100%"],
            max_width="800px",
            margin_bottom="1em",
        ),
        
        footer(),
        width="100%",
        align_items="center",
        min_height="100vh",
    )
