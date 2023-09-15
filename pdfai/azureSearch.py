import os
import json
from langchain.schema import Document
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient,SearchIndexerClient # for create index , we did this by portal
from azure.search.documents import SearchClient
from langchain.embeddings import OpenAIEmbeddings
from azure.search.documents.models import Vector
from azure.search.documents.indexes.models import (
    IndexingSchedule,
    SearchIndex,
    SearchIndexer,
    SearchIndexerDataContainer,
    SearchField,
    SearchFieldDataType,
    SearchableField,
    SemanticConfiguration,
    SimpleField,
    PrioritizedFields,
    SemanticField,
    SemanticSettings,
    VectorSearch,
    VectorSearchAlgorithmConfiguration,
    SearchIndexerDataSourceConnection
)
from .formRecognize import generate_embeddings

service_name = "star5search"
admin_key = "utPRwPzFAkvxgVAUwNXLQL2HhDvZ1QJOM9EiCkRxS4AzSeAknfs0"

index_name = "star5searchindex"

# Create an SDK client
endpoint = "https://{0}.search.windows.net/".format(service_name)

def vector_search(query):
    search_client = SearchClient(endpoint, index_name, AzureKeyCredential(admin_key))  
    results = search_client.search(  
        search_text="",  
        vector=Vector(value=generate_embeddings(query), k=3),  
        include_total_count=True, query_type="full",semantic_configuration_name="my-semantic-cfg"
       # select=["title", "content", "category"] 
    )
    return results
# admin_client = SearchIndexClient(endpoint=endpoint,
#                       index_name=index_name,
#                       credential=AzureKeyCredential(admin_key))
# semantic_config = SemanticConfiguration(
#     name="my-semantic-config",
#     prioritized_fields=PrioritizedFields(
#         title_field=SemanticField(field_name="title"),
#         prioritized_keywords_fields=[SemanticField(field_name="category")],
#         prioritized_content_fields=[SemanticField(field_name="content")]
#     )
# )
# semantic_settings = SemanticSettings(configuration=[semantic_config])

# # Create the search index with the semantic settings
# index = SearchIndex(name=index_name, fields=fields,
#                     vector_search=vector_search, semantic_settings=semantic_settings)
# result = index_client.create_or_update_index(index)
# print(f' {result.name} created')
# def _create_datasource():
#     # Here we create a datasource. 
#     ds_client = SearchIndexerClient(endpoint, AzureKeyCredential(admin_key))
#     container = SearchIndexerDataContainer(name="AzureServices")
#     data_source_connection = SearchIndexerDataSourceConnection(
#         name="cosmosdb-tutorial-indexer", type="cosmosdb", connection_string=cosmosdb_connection_str, container=container
#     )
#     data_source = ds_client.create_or_update_data_source_connection(data_source_connection)
#     return data_source

# ds_name = _create_datasource().name

# indexer = SearchIndexer(
#         name="cosmosdb-tutorial-indexer",
#         data_source_name=ds_name,
#         target_index_name=index_name)


# run indexer to get data from db to index
indexer_client = SearchIndexerClient(endpoint, AzureKeyCredential(admin_key))
#indexer_client.create_or_update_indexer(indexer)  # create the indexer

result = indexer_client.get_indexer("star5-cosmosdb-indexer")
print(result)

# Run the indexer we just created.
indexer_client.run_indexer(result.name)

#-------------------------------------
search_client = SearchClient(endpoint=endpoint,
                      index_name=index_name,
                      credential=AzureKeyCredential(admin_key))

#delete index first, then you can create again
#deleteIndex()

results = vector_search("How many shares Jake have?")
# results2 = search_client.autocomplete(search_text="shares",suggester_name="testdbtable")


# results = search_client.search(search_text="name", filter="keyvalue.shares eq 200",include_total_count=True
#                             #    vector=np.array(OpenAIEmbeddings().embed_query("list all records whose shares > 200"), dtype=np.float32).tolist()
#                                )
# for result in results2:
#     print (result['text'],"===",result)
# print("-------------------------------")
print ('Total Documents Matching Query:', results.get_count(), results)
for result in results:
    #print(result)
    print("{}: {}".format(result["name"], result["shares"]))



# def deleteIndex():
#     try:
#         result = admin_client.delete_index(index_name)
#         print ('Index', index_name, 'Deleted')
#     except Exception as ex:
#         print (ex)