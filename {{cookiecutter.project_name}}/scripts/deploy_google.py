from gcloud import storage
import sys
import os
import config_google as c

deploy_prefix = None if len(sys.argv)==1 else sys.argv[1]

def upload_blob(bucket_name, source_file_name, artefact_path, artefact_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    destination_blob_name = os.path.join(artefact_path, artefact_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

upload_blob(
    c.gs_bucket,
    c.local_artefact,
    c.storage_artefact_path(deploy_prefix),
    c.artefact_name)
