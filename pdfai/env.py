import os
import pinecone

def init():
    os.environ["OPENAI_API_KEY"] ="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"
    pinecone.init(
    api_key="ec70078b-04f8-4d91-8ebc-98ad36e923c1",
    environment="asia-southeast1-gcp-free"
)
 