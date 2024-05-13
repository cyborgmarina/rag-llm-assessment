# Use the official Python 3.11 image as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and install poetry
COPY pyproject.toml /app/
RUN pip install poetry

# Install the dependencies
RUN poetry install --no-root

# Langchain
RUN poetry add uvicorn langchain langchain-community langchain-weaviate

# Embedding models dependencies
RUN poetry add spacy
RUN poetry run spacy download pt_core_news_sm 

# Copy the rest of the application code
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

