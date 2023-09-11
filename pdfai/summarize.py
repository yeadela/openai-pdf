from .env import init
from langchain import PromptTemplate
# Loaders
from langchain.schema import Document
from langchain.document_loaders import PyPDFLoader
# Splitters
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Model
from langchain.chat_models import ChatOpenAI

# Embedding Support
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Summarizer we'll use for Map Reduce
from langchain.chains.summarize import load_summarize_chain

# Data Science
import numpy as np
from sklearn.cluster import KMeans
import os

from django.http import JsonResponse
def summarize(request) :
    init()
    current_path = os.path.abspath(os.path.dirname(__file__))
    filePath=current_path+"/sicence.pdf"
    loader = PyPDFLoader(filePath)
    pages = loader.load()


    # Combine the pages, and replace the tabs with spaces
    text = ""

    for page in pages:
        text += page.page_content
        
    text = text.replace('\t', ' ')
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", "\t"], chunk_size=10000, chunk_overlap=3000)

    docs = text_splitter.create_documents([text])
    num_documents = len(docs)

    embeddings = OpenAIEmbeddings()

    vectors = embeddings.embed_documents([x.page_content for x in docs])
    # Assuming 'embeddings' is a list or array of 1536-dimensional embeddings

    # Choose the number of clusters, this can be adjusted based on the book's content.
    # I played around and found ~10 was the best.
    # Usually if you have 10 passages from a book you can tell what it's about
    num_clusters = 3

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42).fit(vectors)
    # Find the closest embeddings to the centroids

    # Create an empty list that will hold your closest points
    closest_indices = []

    # Loop through the number of clusters you have
    for i in range(num_clusters):
        
        # Get the list of distances from that particular cluster center
        distances = np.linalg.norm(vectors - kmeans.cluster_centers_[i], axis=1)
        
        # Find the list position of the closest one (using argmin to find the smallest distance)
        closest_index = np.argmin(distances)
        
        # Append that position to your closest indices list
        closest_indices.append(closest_index)
    selected_indices = sorted(closest_indices)
    llm3 = ChatOpenAI(temperature=0,
                 max_tokens=1000,
                 model='gpt-3.5-turbo'
                )
    map_prompt = """
        You will be given a single passage of a book. This section will be enclosed in triple backticks (```)
        Your goal is to give a summary of this section so that a reader will have a full understanding of what happened.
        Your response should be at least three paragraphs and fully encompass what was said in the passage.

        ```{text}```
        FULL SUMMARY:
        """
    map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text"])
    map_chain = load_summarize_chain(llm=llm3,
                             chain_type="stuff",
                             prompt=map_prompt_template)
    selected_docs = [docs[doc] for doc in selected_indices]
    # Make an empty list to hold your summaries
    summary_list = []

    # Loop through a range of the lenght of your selected docs
    for i, doc in enumerate(selected_docs):
        # Go get a summary of the chunk
        chunk_summary = map_chain.run([doc])       
        # Append that summary to your list
        summary_list.append(chunk_summary)       
        print (f"Summary #{i} (chunk #{selected_indices[i]}) - Preview: {chunk_summary[:250]} \n")
    summaries = "\n".join(summary_list)

    # Convert it back to a document
    #summaries = Document(page_content=summaries)

    #print (f"Your total summary has {llm3.get_num_tokens(summaries.page_content)} tokens")
    return JsonResponse({"data":summaries})