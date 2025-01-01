# Deploy Private Llama 3.2 API RAG
This is a Lightning Studio Template example in :
https://lightning.ai/lightning-ai/studios/deploy-a-private-llama-3-2-rag-api?section=featured

## Fast Execution

Spin up the container and execute the python rag_server to run the uvicorn server

```
mkdir qdrant_storage
docker compose up

# Place contents to data/ folder (a pdf)
python rag_server.py
``` 

Then go to notebook `server_request.ipynb` to run a request. 

## Conda Env
r_apirag