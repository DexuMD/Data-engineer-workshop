FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
WORKDIR /code

COPY pyproject.toml .python-version uv.lock README.md  ./
RUN mkdir src
COPY /src /code/src
RUN uv sync --locked

ENV PATH="/code/.venv/bin:$PATH"
COPY pipeline.py .
ENTRYPOINT ["python","pipeline.py"]