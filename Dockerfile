FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

ENV POETRY_VENV_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root

COPY . .

RUN poetry build && pip install dist/*.whl

RUN mkdir -p /app/data

CMD ["python", "src/video_processor.py"]