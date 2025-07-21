FROM python:latest

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 直接 python環境にインストールする。
# 仮想環境切る場合はコメントアウトする
ENV UV_PROJECT_ENVIRONMENT=/usr/local

# Create workspace directory
WORKDIR /app