FROM python:3.12-slim-bullseye as base

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip && pip install poetry
RUN poetry self add poetry-plugin-export
COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes \
    && pip install --no-cache-dir -r requirements.txt


FROM python:3.12-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY --from=base $VIRTUAL_ENV $VIRTUAL_ENV
COPY .env .env
COPY ./app ./app

EXPOSE 8000
#CMD ["uvicorn", "app.application:get_app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "application:get_app"]
