import os
import pinecone

def init():
    os.environ["OPENAI_API_KEY"] ="0fae934ef46b94d1a6a3bb0feecb11a3"
    os.environ["OPENAI_API_BASE"] ="http://flag.smarttrot.com/index.php/api/v1"
    pinecone.init(
    api_key="ec70078b-04f8-4d91-8ebc-98ad36e923c1",
    environment="asia-southeast1-gcp-free"
)
 