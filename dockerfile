FROM python:3.10 as base

FROM base as python-deps

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS runtime

WORKDIR /code

COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

COPY . .

EXPOSE 8080

CMD ["streamlit","run", "./src/ui.py", "--server.port", "8080"]