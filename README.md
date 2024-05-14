# Machine Learning Engineer (AI Platform) Assessment

## Quickstart
1. Get an API key from [Open Router](https://openrouter.ai/) as it hosts free versions of open source models, in this case, llama3-8b. 
2. Copy `.env.example ` to `.env` in root directory of the project, and change API_KEY on `.env` accordingly:
```bash
API_KEY="<api-key-from-open-router>"
```
3. aSpin up APIs and vectorstore containers using *docker-compose*:
	```bash
	docker-compose up --build
	```
4. **cURL to send example.txt file, split into chunks and add chunks as documents on vectorstore**:
```bash
curl -X POST "http://localhost:8001/api/document" -F "file=@example.txt"
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
- CHAT_MODEL, BASE_URL and API_KEY environment variables can be changed on `.env` file if provider has OpenAI-compatible endpoints. For `llama3-8b`, I would recommend hosted APIs like **OpenRouter** and **Groq** or [Ollama](https://ollama.com/) for locally running open source models.
### Tuning Text Splitting
- CHUNK_SIZE and CHUNK_OVERLAP parameters can be changed on `.env` :
  ```bash
  CHUNK_SIZE=1000 
  CHUNK_OVERLAP=20
  ```
