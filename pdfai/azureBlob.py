import os
from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient,  generate_blob_sas, generate_container_sas, ContentSettings

class AzureBlobStorageClient:
    def __init__(self, account_name: str = None, account_key: str = None, container_name: str = None):

        self.account_name : str = account_name if account_name else os.getenv('BLOB_ACCOUNT_NAME')
        self.account_key : str = account_key if account_key else os.getenv('BLOB_ACCOUNT_KEY')
        self.connect_str : str = f"DefaultEndpointsProtocol=https;AccountName={self.account_name};AccountKey={self.account_key};EndpointSuffix=core.windows.net"
        self.container_name : str = container_name if container_name else os.getenv('BLOB_CONTAINER_NAME')
        self.blob_service_client : BlobServiceClient = BlobServiceClient.from_connection_string(self.connect_str)

    def delete_file(self, file_name):
        blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=file_name)
        blob_client.delete_blob()

    def upload_file(self, bytes_data, file_name, content_type='application/pdf'):
        # Create a blob client using the local file name as the name for the blob
        blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=file_name)
        # Upload the created file
        blob_client.upload_blob(bytes_data, overwrite=True, content_settings=ContentSettings(content_type=content_type))
        # Generate a SAS URL to the blob and return it
        return blob_client.url + '?' + generate_blob_sas(self.account_name, self.container_name, file_name,account_key=self.account_key,  permission="r", expiry=datetime.utcnow() + timedelta(hours=3))

    def upsert_blob_metadata(self, file_name, metadata):
        blob_client = BlobServiceClient.from_connection_string(self.connect_str).get_blob_client(container=self.container_name, blob=file_name)
        # Read metadata from the blob
        blob_metadata = blob_client.get_blob_properties().metadata
        # Update metadata
        blob_metadata.update(metadata)
        # Add metadata to the blob
        blob_client.set_blob_metadata(metadata= blob_metadata)

    def get_container_sas(self):
        # Generate a SAS URL to the container and return it
        return "?" + generate_container_sas(account_name= self.account_name, container_name= self.container_name,account_key=self.account_key,  permission="r", expiry=datetime.utcnow() + timedelta(hours=1))
