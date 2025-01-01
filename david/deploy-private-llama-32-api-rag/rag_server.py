import litserve as ls
from fastembed import TextEmbedding

from ingestion import ingest_pdfs
from retriever import Retriever
from prompt_template import qa_prompt_tmpl_str
import transformers
import torch

class DocumentChatAPI(ls.LitAPI):
    def setup(self, device):
        self.model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_id,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map="auto",
        )
        embed_model = TextEmbedding(model_name="nomic-ai/nomic-embed-text-v1.5")
        ingest_pdfs("./data", embed_model)
        self.retriever = Retriever(embed_model)

    def decode_request(self, request):
        return request["query"]

    def predict(self, query):
        context = self.retriever.generate_context(query)
        prompt = qa_prompt_tmpl_str.format(context=context, query=query)

        messages = [{"role": "user", "content": [
            {"type": "text", "text": prompt}
            ]}]

        outputs = self.pipeline(
            messages,
            max_new_tokens=256,
        )
        text = outputs[0]["generated_text"][-1]["content"]
        return text

    def encode_response(self, output):
        return {"output": output}

if __name__ == "__main__":
    api = DocumentChatAPI()
    server = ls.LitServer(api)
    server.run(port=8080)