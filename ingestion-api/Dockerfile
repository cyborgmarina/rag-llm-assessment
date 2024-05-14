FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml /app/
COPY pyproject.toml /app/

RUN pip install poetry
RUN poetry install --no-root

# Download spacy embeddings portuguese model
RUN poetry run spacy download pt_core_news_sm 

COPY . /app

EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

