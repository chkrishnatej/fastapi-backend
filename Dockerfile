FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml poetry.lock* ./

# for poetry
RUN mkdir -p /app/app/
RUN touch /app/app/__init__.py

RUN poetry install -n

RUN poetry show

COPY ./app /app/app