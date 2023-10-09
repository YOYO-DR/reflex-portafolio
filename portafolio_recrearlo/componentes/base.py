import reflex as rx
from portafolio_recrearlo import style
from portafolio_recrearlo.componentes.footer import Footer
from portafolio_recrearlo.componentes.navbar import NavBar

def Base(content):
  return rx.center(
    rx.vstack(
      NavBar(),
      content,
      Footer(),
      style=style.s_base
    ),
  )