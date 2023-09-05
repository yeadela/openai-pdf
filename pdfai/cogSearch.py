
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient 
from azure.search.documents import SearchClient
# from azure.core.exceptions import AzureError  
from azure.search.documents.indexes.models import (
    ComplexField,
    CorsOptions,
    SearchIndex,
    ScoringProfile,
    SearchFieldDataType,
    SimpleField,
    SearchableField
)

service_name = "your-search-service-name"
admin_key = "your-search-service-admin-api-key"

index_name = "your_index_name"

# Create an SDK client
endpoint = "https://{}.search.windows.net/".format(service_name)
admin_client = SearchIndexClient(endpoint=endpoint,
                      index_name=index_name,
                      credential=AzureKeyCredential(admin_key))

search_client = SearchClient(endpoint=endpoint,
                      index_name=index_name,
                      credential=AzureKeyCredential(admin_key))

try:
    result = admin_client.delete_index(index_name)
    print ('Index', index_name, 'Deleted')
except Exception as ex:
    print (ex)
 
# 创建索引
# Specify the index schema
name = index_name
fields = [
        SimpleField(name="HotelId", type=SearchFieldDataType.String, key=True),
        SearchableField(name="HotelName", type=SearchFieldDataType.String, sortable=True),
        SearchableField(name="Description", type=SearchFieldDataType.String, analyzer_name="en.lucene"),
        SearchableField(name="Description_fr", type=SearchFieldDataType.String, analyzer_name="fr.lucene"),
        SearchableField(name="Category", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),

        SearchableField(name="Tags", collection=True, type=SearchFieldDataType.String, facetable=True, filterable=True),

        SimpleField(name="ParkingIncluded", type=SearchFieldDataType.Boolean, facetable=True, filterable=True, sortable=True),
        SimpleField(name="LastRenovationDate", type=SearchFieldDataType.DateTimeOffset, facetable=True, filterable=True, sortable=True),
        SimpleField(name="Rating", type=SearchFieldDataType.Double, facetable=True, filterable=True, sortable=True),

        ComplexField(name="Address", fields=[
            SearchableField(name="StreetAddress", type=SearchFieldDataType.String),
            SearchableField(name="City", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
            SearchableField(name="StateProvince", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
            SearchableField(name="PostalCode", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
            SearchableField(name="Country", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
        ])
    ]
cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)
scoring_profiles = []
suggester = [{'name': 'sg', 'source_fields': ['Tags', 'Address/City', 'Address/Country']}]

# 此 create_index 请求以搜索服务的索引集合为目标，并基于在上一单元格中提供的索引架构创建 SearchIndex
index = SearchIndex(
    name=name,
    fields=fields,
    scoring_profiles=scoring_profiles,
    suggesters = suggester,
    cors_options=cors_options)

try:
    result = admin_client.create_index(index)
    print ('Index', result.name, 'created')
except Exception as ex:
    print (ex)

# 加载文档
documents = [
    {
    "@search.action": "upload",
    "HotelId": "1",
    "HotelName": "Secret Point Motel",
    "Description": "The hotel is ideally located on the main commercial artery of the city in the heart of New York. A few minutes away is Time's Square and the historic centre of the city, as well as other places of interest that make New York one of America's most attractive and cosmopolitan cities.",
    "Description_fr": "L'hôtel est idéalement situé sur la principale artère commerciale de la ville en plein cœur de New York. A quelques minutes se trouve la place du temps et le centre historique de la ville, ainsi que d'autres lieux d'intérêt qui font de New York l'une des villes les plus attractives et cosmopolites de l'Amérique.",
    "Category": "Boutique",
    "Tags": [ "pool", "air conditioning", "concierge" ],
    "ParkingIncluded": "false",
    "LastRenovationDate": "1970-01-18T00:00:00Z",
    "Rating": 3.60,
    "Address": {
        "StreetAddress": "677 5th Ave",
        "City": "New York",
        "StateProvince": "NY",
        "PostalCode": "10022",
        "Country": "USA"
        }
    },
    {
    "@search.action": "upload",
    "HotelId": "2",
    "HotelName": "Twin Dome Motel",
    "Description": "The hotel is situated in a  nineteenth century plaza, which has been expanded and renovated to the highest architectural standards to create a modern, functional and first-class hotel in which art and unique historical elements coexist with the most modern comforts.",
    "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
    "Category": "Boutique",
    "Tags": [ "pool", "free wifi", "concierge" ],
    "ParkingIncluded": "false",
    "LastRenovationDate": "1979-02-18T00:00:00Z",
    "Rating": 3.60,
    "Address": {
        "StreetAddress": "140 University Town Center Dr",
        "City": "Sarasota",
        "StateProvince": "FL",
        "PostalCode": "34243",
        "Country": "USA"
        }
    },
    {
    "@search.action": "upload",
    "HotelId": "3",
    "HotelName": "Triple Landscape Hotel",
    "Description": "The Hotel stands out for its gastronomic excellence under the management of William Dough, who advises on and oversees all of the Hotel's restaurant services.",
    "Description_fr": "L'hôtel est situé dans une place du XIXe siècle, qui a été agrandie et rénovée aux plus hautes normes architecturales pour créer un hôtel moderne, fonctionnel et de première classe dans lequel l'art et les éléments historiques uniques coexistent avec le confort le plus moderne.",
    "Category": "Resort and Spa",
    "Tags": [ "air conditioning", "bar", "continental breakfast" ],
    "ParkingIncluded": "true",
    "LastRenovationDate": "2015-09-20T00:00:00Z",
    "Rating": 4.80,
    "Address": {
        "StreetAddress": "3393 Peachtree Rd",
        "City": "Atlanta",
        "StateProvince": "GA",
        "PostalCode": "30326",
        "Country": "USA"
        }
    },
    {
    "@search.action": "upload",
    "HotelId": "4",
    "HotelName": "Sublime Cliff Hotel",
    "Description": "Sublime Cliff Hotel is located in the heart of the historic center of Sublime in an extremely vibrant and lively area within short walking distance to the sites and landmarks of the city and is surrounded by the extraordinary beauty of churches, buildings, shops and monuments. Sublime Cliff is part of a lovingly restored 1800 palace.",
    "Description_fr": "Le sublime Cliff Hotel est situé au coeur du centre historique de sublime dans un quartier extrêmement animé et vivant, à courte distance de marche des sites et monuments de la ville et est entouré par l'extraordinaire beauté des églises, des bâtiments, des commerces et Monuments. Sublime Cliff fait partie d'un Palace 1800 restauré avec amour.",
    "Category": "Boutique",
    "Tags": [ "concierge", "view", "24-hour front desk service" ],
    "ParkingIncluded": "true",
    "LastRenovationDate": "1960-02-06T00:00:00Z",
    "Rating": 4.60,
    "Address": {
        "StreetAddress": "7400 San Pedro Ave",
        "City": "San Antonio",
        "StateProvince": "TX",
        "PostalCode": "78216",
        "Country": "USA"
        }
    }
]
# 此 upload_documents 请求以 hotels-quickstart 索引的文档集合为目标，将在上一步骤中提供的文档推送到认知搜索索引
try:
    result = search_client.upload_documents(documents=documents)
    print("Upload of new document succeeded: {}".format(result[0].succeeded))
except Exception as ex:
    print (ex.message)
"""
# search all documents，include_total_count=True 以获取结果中所有文档 (4) 的计数。
results = search_client.search(search_text="*", include_total_count=True)

print ('Total Documents Matching Query:', results.get_count())
for result in results:
    print("{}: {}".format(result["HotelId"], result["HotelName"]))

results = search_client.search(search_text="wifi", include_total_count=True, select='HotelId,HotelName,Tags')

print ('Total Documents Matching Query:', results.get_count())
for result in results:
    print("{}: {}: {}".format(result["HotelId"], result["HotelName"], result["Tags"]))

#搜索wifi
results = search_client.search(search_text="wifi", include_total_count=True, select='HotelId,HotelName,Tags')

print ('Total Documents Matching Query:', results.get_count())
for result in results:
    print("{}: {}: {}".format(result["HotelId"], result["HotelName"], result["Tags"]))

#应用筛选表达式，仅返回评分高于 4 的酒店（按降序排列）
results = search_client.search(search_text="hotels", select='HotelId,HotelName,Rating', 
                               filter='Rating gt 4', order_by='Rating desc')

for result in results:
    print("{}: {} - {} rating".format(result["HotelId"], result["HotelName"], result["Rating"]))

#添加 search_fields（一个数组），将查询匹配的范围限制为单一字段。
results = search_client.search(search_text="sublime", search_fields=['HotelName'], select='HotelId,HotelName')

for result in results:
    print("{}: {}".format(result["HotelId"], result["HotelName"]))

'''
 “自动完成”通常在搜索框中使用，以便在用户在搜索框中键入时提供可能的匹配项。

创建索引时,还创建名为“suggest”的建议器作为请求的一部分。 
建议器定义指定哪些字段可用于查找建议器请求的潜在匹配。
 在此示例中，这些字段是“标签”、“地址/城市”、“地址/国家/地区”。 
 若要模拟自动完成,请输入字母“sa”作为字符串的一部分。 SearchClient 的自动完成方法会发回可能的术语匹配
'''
"""
search_suggestion = 'sa'
results = search_client.autocomplete(search_text=search_suggestion, suggester_name="suggest", mode='twoTerms')

print("Autocomplete for:", search_suggestion)
for result in results:
    print (result['text'])