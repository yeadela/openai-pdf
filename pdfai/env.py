import os
import pinecone

def init():
    os.environ["OPENAI_API_KEY"] ="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"
    pinecone.init(
    api_key="ec70078b-04f8-4d91-8ebc-98ad36e923c1",
    environment="asia-southeast1-gcp-free"
)
 