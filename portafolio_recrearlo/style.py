# estilos con funciones
def def_s_align_text(alineacion):
  return dict(textAlign=alineacion)


def def_s_width(width: str | float):
  return dict(width=f'{width}%')


# alinear texto a la derecha y width de 100
s_tl_w100 = {**def_s_align_text("left"), **def_s_width(100)}

# app (html o body pues)
s_app = dict(bg="#090909")

# btn descarga cv
s_btn_cv = dict(
  bg="#0d6efd",
  color="white",
  **{"_hover":{
    "bg":"white",
    "color":"black"
  }}
)

# contenedor base
s_base = dict(
  bg="black",
  color="white",
  width="1200px",
  padding="20px"
)


# inicio de navbar
s_nav_item_inicio = dict(
  fontSize="1.3rem",
  marginRight="auto",
  **{"_hover": {
    "textDecoration": "none",
  }}
)

# notas navbar
s_nav_item_notas = dict(
  fontSize="1rem",
  color="rgba(255, 255, 255, 0.55)",
  marginLeft="auto",
  **{"_hover": {
    "textDecoration": "none",
    "color": "rgba(255, 255, 255, 0.75)"
  }}
)

# imagen de inicio
s_img_border = dict(
  border="1px solid white",
  borderRadius="0.375rem"
)

# texto del footer
s_heading_footer = dict(
  fontSize="15px",
)

# footer
s_footer = dict()
