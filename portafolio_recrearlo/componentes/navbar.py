import reflex as rx
from portafolio_recrearlo import style


def NavBar():
  return rx.hstack(
    rx.link(
      "Inicio", 
      href="/", 
      style=style.s_nav_item_inicio
    ),
    rx.link(
      "Notas", 
      href="#",
      style=style.s_nav_item_notas
    ),
    style=style.s_navbar
  )
