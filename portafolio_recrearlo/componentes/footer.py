import reflex as rx
from portafolio_recrearlo import style

def Footer():
  return rx.hstack(
    rx.heading(
      "Todos los derechos reservados | creado por Yoiner Duran",
      style=style.s_heading_footer
    ),
    style=style.s_footer
  )