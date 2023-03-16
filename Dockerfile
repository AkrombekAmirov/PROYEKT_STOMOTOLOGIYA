FROM python:3.9

WORKDIR /code

COPY ./ /code/

RUN --mount=type=cache,target=/root/.cache/pip pip install --upgrade -r requirements.txt

CMD ["python", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]