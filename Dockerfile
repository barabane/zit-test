FROM python:3.12

RUN mkdir /project

WORKDIR /project

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "localhost", "--port", "7777"]