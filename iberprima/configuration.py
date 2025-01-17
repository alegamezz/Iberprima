import reflex as rx

class Config(rx.Config):
    pass

config = Config(
    app_name="map_app",
    db_url="sqlite:///reflex.db",
    frontend_packages=[
        "react-leaflet",
        "leaflet"
    ],
    env=rx.Env.DEV,
)