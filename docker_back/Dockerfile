# Dockerfile-backend

FROM python:3.11 as init

WORKDIR /app
COPY . .

# Create virtualenv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV

# Install app requirements and reflex inside virtualenv
RUN pip install -r requirements.txt

# Export static copy of frontend to /app/.web/_static
RUN reflex export --backend-only --no-zip

CMD reflex run --env prod --backend-only