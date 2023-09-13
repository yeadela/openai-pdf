import os
import pinecone

def init():
    os.environ["OPENAI_API_KEY"] ="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"
    pinecone.init(
    api_key="ec70078b-04f8-4d91-8ebc-98ad36e923c1",
    environment="asia-southeast1-gcp-free"
)
 