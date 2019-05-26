from gcloud import storage
import os
import sys

deploy_prefix = None if len(sys.argv)==1 else sys.argv[1]

bucket="{{cookiecutter.gs_bucket}}"

with open("{{cookiecutter.algorithm_name}}/version") as v:
    version = v.read()

version_folder = version if deploy_prefix is None else "{}_{}".format(deploy_prefix, version)

artefact_name = "{{cookiecutter.algorithm_name}}-{}.tar.gz".format(version)
local_artefact = os.path.join("{{cookiecutter.algorithm_name}}","dist",artefact_name)
destination_blob=os.path.join("artefacts","algorithms",version_folder,artefact_name)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

upload_blob(bucket, local_artefact, destination_blob)

