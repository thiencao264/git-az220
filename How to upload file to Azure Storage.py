import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)

#UPLOAD FILE TO AZURE
#=====================================================================
# Create a file in the local data directory to upload and download

upload_file_path = "C:\\Users\\Administrator\\Desktop\\Azure 220 OK\\UploadFile\\TestFileUpload1.txt"



# Azure
# Get this from Settings/Access keys in your Storage account on Azure portal
account_name = STORAGE_00001
connection_string = CONNECTION_STRING

# Source
source_container_name = "sourcecontainer"
source_file_path = "TestFileUpload1.txt"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

source_blob1 = blob_service_client.get_blob_client(source_container_name, source_file_path)
source_blob = (f"https://{account_name}.blob.core.windows.net/{source_container_name}/{source_file_path}")

# If you would like to delete the source file
try:
    remove_blob = blob_service_client.get_blob_client(source_container_name, source_file_path)
    remove_blob.delete_blob()
except:
    print("No file to delete!")


# Upload data to source
with open(upload_file_path, "rb") as data:
    source_blob1.upload_blob(data)
    
print("Upload OK")

#Get the source blob name
sourcefilename = source_blob1.get_blob_properties().name
#Get the last modified time of source bob
last_modified_time = source_blob1.get_blob_properties().last_modified
#Append the last modified time to the source blob name 
targetfilename = sourcefilename + ' ' + str(last_modified_time)



# Target
target_container_name = "targetcontainer"
target_file_path = targetfilename
copied_blob = blob_service_client.get_blob_client(target_container_name, target_file_path)


copied_blob.start_copy_from_url(source_blob)




