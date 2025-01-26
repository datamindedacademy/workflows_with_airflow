FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync --frozen
ENV PATH="/app/.venv/bin:$PATH"