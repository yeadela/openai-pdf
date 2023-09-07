from .env import init
from langchain import PromptTemplate
from django.http import JsonResponse
from .azureBlob import AzureBlobStorageClient
from .store import extract_text_from_PDF, add_embedding
import re
def upload(request) :
    # save file to blob
    blob_client: AzureBlobStorageClient = AzureBlobStorageClient() if blob_client is None else blob_client
    # Extract the text from the file
    text= extract_text_from_PDF(request.body.files)
    filename=request.body.filename
    # Remove half non-ascii character from start/end of doc content (langchain TokenTextSplitter may split a non-ascii character in half)
    pattern = re.compile(r'[\x00-\x09\x0b\x0c\x0e-\x1f\x7f\u0080-\u00a0\u2000-\u3000\ufff0-\uffff]')  # do not remove \x0a (\n) nor \x0d (\r)
    converted_text = re.sub(pattern, '', "\n".join(text))

    # Upload the text to Azure Blob Storage
    converted_filename = f"converted/{filename}.txt"
    source_url = blob_client.upload_file(converted_text, f"converted/{filename}.txt", content_type='text/plain; charset=utf-8')

    # print(f"Converted file uploaded to {source_url} with filename {filename}")
    
    # Update the metadata to indicate that the file has been converted
    blob_client.upsert_blob_metadata(filename, {"converted": "true"})

    add_embedding(source_url)

    return converted_filename