"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from portafolio_recrearlo import style
from portafolio_recrearlo.componentes.base import Base

import reflex as rx


class State(rx.State):
  pass


def index() -> rx.Component:
  return Base(
    rx.vstack(
      rx.hstack(
        rx.image(
          src="https://djangoyoiner.blob.core.windows.net/portafolio/static/portfolio/perfil.jpg",
          style=style.s_img_border
        ),
        rx.vstack(
          rx.heading(
            "Hola, me llamo Yoiner",
            style=style.s_tl_w100
          ),
          rx.heading(
            "Soy aprendiz en ser desarrollador Fullstack",
            style=[style.s_tl_w100]
          ),
          rx.text("Soy estudiante de Servicio Nacional de Aprendizaje SENA, donde estoy cursando Analisis y Desarrollo de Sistemas de Información (ADSI). Además, me he dedicado a aprender de forma autodidacta Frontend y Backend utilizando tecnologías como HTML, CSS, Bootstrap y JavaScript para Frontend, y Python con los Frameworks Django y Django Rest para la creación de API REST en el Backend. También tengo experiencia en el manejo de bases de datos con MySQL."),
          rx.text("Durante mi aprendizaje, he realizado diversos proyectos personales con el objetivo de mejorar mis habilidades en el ámbito Fullstack. Estoy entusiasmado por aplicar mis conocimientos en diferentes contextos, ya sea trabajando para una empresa o colaborando en proyectos. Mi objetivo es adquirir experiencia en el mercado laboral y seguir perfeccionando mis habilidades."),
          rx.link(
            rx.button(
              "Descargar CV",
              style=style.s_btn_cv
            ),
            href="https://djangoyoiner.blob.core.windows.net/portafolio/static/portfolio/cv.pdf",
            color="rgb(107,99,246)", 
            button=True,
            style=dict(marginRight="auto")
            )
        )
      ),
    )
  )


# Add state and page to the app.
app = rx.App()
app.style = style.s_app
app.add_page(index)
app.compile()
