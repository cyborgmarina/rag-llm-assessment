# Machine Learning Engineer (AI Platform) Assessment

## Challenge

Demonstrate skills in applying existing technologies to create a knowledge-based LLM prototype by developing two microservices:

1. A microservice that receives a text document, processes it, and stores it in a Vector Database.
2. An API that, given an input text in the form of a question, searches the knowledge base for relevant context and uses it as input for an LLM to generate a response.

### Important Points to Consider:

- Use proprietary (API) and/or open-source models.
  - Open-source models are strongly encouraged. If not possible due to time or resource constraints, proprietary technologies, such as OpenAI, are acceptable.

- Utilize an open-source Vector Database. 
  - Focus on retrieving the most relevant information given a question to construct the response with the LLM.

- Ensure both APIs and the VectorDB work locally via Docker compose.

### Submission Requirements:

- `docker-compose.yaml` file for reproducibility of the challenge.
- Codes used to generate the test steps (.py), including APIs, infrastructure, and prompts. Provide an executable code structure. `.ipynb` files will not be evaluated.
- `README.md` with project information and step-by-step instructions on how to run it.
- A set of input examples (Postman, cURL, shell scripts, etc.) for testing and reproducibility.

### Load
### Query
1. Make sure jq is installed. You can install it using your package manager, for example:
```sh
sudo apt-get install jq      # On Debian/Ubuntu
sudo yum install jq          # On CentOS/RHEL
brew install jq
```
2. Run the query_knowledge_base.sh script with the query string as an argument:
```sh
./query_knowledge_base.sh "How does Hotmart work?"
```
