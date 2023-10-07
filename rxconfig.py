import reflex as rx

config = rx.Config(
  app_name="portafolio_recrearlo",
  loglevel="info",
  api_url="https://reflex-portafolioyoiner.azurewebsites.net:8000"
)
# docker build -t reflex-portafolio-back:latest .
# docker build -t reflex-portafolio-front:latest .
# back docker run -d -p 8000:8000 --name app reflex-portafolio-back:latest
# back docker run -d -p 3000:3000 --name app reflex-portafolio-front:latest
# docker run -d -p 3000:3000 -p 8000:8000 --name app reflex-portafolio:latest
#  docker logs id_generado_run