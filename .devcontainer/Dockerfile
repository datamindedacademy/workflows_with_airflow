FROM mcr.microsoft.com/devcontainers/python:3.13-bookworm

# use this Dockerfile to install additional tools you might need, e.g.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# Remove Yarn repo with expired GPG key
RUN rm -f /etc/apt/sources.list.d/yarn.list

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync --frozen
ENV PATH="/app/.venv/bin:$PATH"