# Machine Learning Engineer (AI Platform) Assessment

## Quickstart
1. Get an API key from[Open Router](https://openrouter.ai/) as it hosts free version of open source models, in this case, llama3-8b. 
2. Set environment variables for Open Router's API: 
```bash
export ASSESSMENT_CHAT_MODEL="meta-llama/llama-3-8b-instruct:free"
export ASSESSMENT_BASE_URL="https://openrouter.ai/api/v1"
export ASSESSMENT_API_KEY="<api-key-from-open-router>"
```
	    ***Any other OpenAI-compatible provider can be used,** 
3. Spin up APIs and vectorstore containers using *docker-compose*:
	```bash
	docker-compose up --build
	```
4. **cURL to send example.txt file, split into chunks and add chunks as documents on vectorstore**:
```bash
curl -X POST "http://localhost:8001/api/document" -F "file=@example.txt
``` 
5. **cURL to send a question to the knowledge base and receive both context used and LLM-generated response:**
 ```bash
 curl -X POST "http://localhost:8002/api/retrieval" \
-H "Content-Type: application/json" \
-d '{"question": "Como funciona a plataforma?"}'
```
## Technical Overview
- **Open-source** models for embeddings and LLMs: *spaCy* and *llama3-8b* (hosted or local).
- **FastAPI** for both APIs: *ingestion-api* (document ingestion) and *retrieval-api* (retrieval  augmented generation).
- **Weaviate** as vector store database.
- **Docker** for containers and **Docker Compose** for orchestration.
- **OpenAI-Compatible** implementation, meaning any hosted or local provider that exposes a OpenAI-compatible endpoint can be used.

## Experimenting and optimizing

### Swap models and providers
- ASSESSMENT_CHAT_MODEL, ASSESSMENT_BASE_URL and ASSESSMENT_API_KEY environment variables can be changed if provider has OpenAI-compatible endpoints. For `llama3-8b`, I would recommend hosted APIs like **OpenRouter** and **Groq** or [Ollama](https://ollama.com/) for locally running open source models.
### Tuning Text Splitting
- CHUNK_SIZE and CHUNK_OVERLAP parameters can be changed through environment variables:
  ```bash
  docker compose down -v
  CHUNK_SIZE=1000 CHUNK_OVERLAP=20 docker-compose up --build
  ```
